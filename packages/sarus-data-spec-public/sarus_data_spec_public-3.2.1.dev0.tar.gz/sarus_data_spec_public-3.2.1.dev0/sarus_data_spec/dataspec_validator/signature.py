from __future__ import annotations

from enum import Enum, auto
import typing as t

import pyarrow as pa

from sarus_data_spec.arrow.admin_utils import (
    async_admin_data,
    validate_admin_data,
)
from sarus_data_spec.dataspec_validator.parameter_kind import (
    DATASET,
    DATASPEC,
    PEP,
    PEP_DATASET,
    SCALAR,
    STATIC,
    ParameterCondition,
    is_accepted,
)
from sarus_data_spec.manager.ops.processor.external.utils import (
    static_arguments,
)
import sarus_data_spec.protobuf as sp
import sarus_data_spec.typing as st


class DefautValue(Enum):
    NO_DEFAULT = auto()


class SarusParameter:
    def __init__(
        self,
        name: str,
        annotation: t.Any,
        default: t.Any = DefautValue.NO_DEFAULT,
        condition: ParameterCondition = STATIC | DATASPEC,
        predicate: t.Callable[[t.Any], bool] = lambda _: True,
    ):
        self.name = name
        self.condition = condition
        self.annotation = annotation
        self.default = default
        self.predicate = predicate


class SarusSignature:
    """A Signature is a list of Parameters."""

    def __init__(self, *parameters: SarusParameter):
        self._parameters = list(parameters)
        self._parameter_map = {param.name: param for param in parameters}

    def parameters(self) -> t.List[SarusParameter]:
        return self._parameters

    def __getitem__(self, name: str) -> SarusParameter:
        return self._parameter_map[name]

    def _bind_external(
        self,
        transform: st.Transform,
        *ds_args: st.DataSpec,
        **ds_kwargs: st.DataSpec,
    ) -> SarusBoundSignature:
        # Deserialize arguments
        py_args, py_kwargs, ds_args_pos, ds_types = static_arguments(transform)
        if len(ds_types) != len(ds_args) + len(ds_kwargs):
            raise ValueError(
                "Incorrect number of types specified in the external protobuf."
            )
        pos_values = {pos: val for pos, val in zip(ds_args_pos, ds_args)}
        pos_args = {**pos_values, **py_args}

        kwargs = {**py_kwargs, **ds_kwargs}
        args = [pos_args[i] for i in range(len(pos_args))]
        args_types = [ds_types.get(pos) for pos in range(len(args))]
        kwargs_types = {name: ds_types.get(name) for name in kwargs.keys()}

        # Pair arguments serialized in protobuf with the signature's
        # parameters
        bound_args = [
            SarusBoundArgument(self.parameters()[i], arg, args_types[i])
            for i, arg in enumerate(args)
        ]

        bound_kwargs = [
            SarusBoundArgument(
                param, kwargs[param.name], kwargs_types[param.name]
            )
            for param in self.parameters()
            if param.name in kwargs
        ]

        bound_arguments = bound_args + bound_kwargs
        bound_args_names = [bound_arg.name() for bound_arg in bound_arguments]
        if len(set(bound_args_names)) != len(bound_args_names):
            raise ValueError(
                "An argument was specified more than "
                "once in an external transform."
            )

        # Fill in default arguments
        default_bound_args = [
            SarusBoundArgument(param, param.default)
            for param in self.parameters()
            if param.name not in bound_args_names
            and param.default != DefautValue.NO_DEFAULT
        ]
        bound_arguments += default_bound_args

        if len(bound_arguments) != len(self.parameters()):
            raise ValueError(
                "Invalid number of parameters serialized in external"
                f" transform. Expected {len(self.parameters())}, "
                f"got {len(bound_arguments)}."
            )

        # reorder arguments
        arg_map = {arg.name(): arg for arg in bound_arguments}
        bound_arguments = [arg_map[param.name] for param in self.parameters()]

        return SarusBoundSignature(bound_arguments)

    def bind_dataspec(self, dataspec: st.DataSpec) -> SarusBoundSignature:
        if not dataspec.is_transformed():
            raise ValueError("Cannot bind a non transformed dataspec.")

        transform = dataspec.transform()
        ds_args, ds_kwargs = dataspec.parents()
        return self.bind(transform, *ds_args, **ds_kwargs)

    def bind(
        self,
        transform: st.Transform,
        *ds_args: st.DataSpec,
        **ds_kwargs: st.DataSpec,
    ) -> SarusBoundSignature:
        """Deserialize protobuf, get parent dataspecs
        Create bound arguments from the static or dynamic arguments and from
        the parameters Raise an error if there is a mismatch.
        """
        if not transform.is_external():
            raise NotImplementedError(
                "Binding standard signature not implemented yet."
            )
        else:
            return self._bind_external(transform, *ds_args, **ds_kwargs)

    def make_dp(self) -> SarusSignature:
        """Creates a DP Signature from the current one by adding extra
        parameters."""
        return SarusSignature(
            *self._parameters,
            SarusParameter(
                name="budget",
                annotation=sp.Scalar.PrivacyParameters,
                condition=SCALAR,
            ),
            SarusParameter(
                name="seed",
                annotation=int,
                condition=SCALAR,
            ),
        )


class SarusBoundArgument:
    """A BoundArgument is a triplet (parameter, value, kind).

    Args:
        parameter (SarusParameter):
            The Sarus parameter describing what is accepted.
        value (t.Union[st.DataSpec, t.Any]):
            The value as defined by the computation graph.
        kind (t.Optional[str]):
            The Python type a Dataset should be casted to.
    """

    dataset_types = {
        str(_type): t.cast(t.Type, _type)
        for _type in t.get_args(st.DatasetCastable)
    }

    def __init__(
        self,
        parameter: SarusParameter,
        value: t.Union[st.DataSpec, t.Any],
        kind: t.Optional[str] = None,
    ):
        self.parameter = parameter
        self._value = value
        self.kind = kind

    def name(self) -> str:
        return self.parameter.name

    def static_value(self) -> t.Any:
        return self._value

    def python_type(self) -> t.Optional[str]:
        return self.kind

    def parameter_kind(self) -> ParameterCondition:
        """Return the value type associated with the Parameter."""
        if isinstance(self.static_value(), st.DataSpec):
            dataspec = t.cast(st.DataSpec, self.static_value())
            if dataspec.prototype() == sp.Dataset:
                dataset = t.cast(st.Dataset, dataspec)
                if dataset.is_pep():
                    return PEP_DATASET
                else:
                    return DATASET
            else:
                return SCALAR
        else:
            return STATIC

    def pep_token(self) -> t.Optional[str]:
        parameter_kind = self.parameter_kind()
        if PEP.isin(parameter_kind):
            dataset = t.cast(st.Dataset, self.static_value())
            return dataset.pep_token()
        else:
            return None

    def is_pep(self) -> bool:
        return self.pep_token() is not None

    def is_public(self) -> bool:
        parameter_kind = self.parameter_kind()
        if STATIC.isin(parameter_kind):
            return True
        elif DATASPEC.isin(parameter_kind):
            dataspec = t.cast(st.DataSpec, self.static_value())
            return dataspec.is_public()
        else:
            raise ValueError(
                f"Cannot determine if {parameter_kind} is public."
            )

    def static_validation(self) -> None:
        """Check that the argument is compatible with the parameter"""
        parameter_kind = self.parameter_kind()
        if not is_accepted(self.parameter.condition, parameter_kind):
            raise TypeError(
                f"Expected parameter {self.name()} to be "
                f"{str(self.parameter.condition)}, got {str(parameter_kind)}"
            )

        if DATASET.isin(parameter_kind):
            if self.kind is None:
                raise ValueError(
                    f"Parameter {self.name()} is a Dataset, but no type "
                    "to cast to is defined."
                )

            if self.kind not in self.dataset_types:
                raise ValueError(
                    f"Parameter {self.name()} is a Dataset "
                    f"and cannot be casted to type {self.kind}. "
                    f"Expected one of {list(self.dataset_types.keys())}"
                )

        if STATIC.isin(parameter_kind):
            value = self.static_value()
            if not self.parameter.predicate(value):
                raise ValueError(
                    f"Got invalid value `{value}` for "
                    f"parameter `{self.name()}`"
                )

    async def dynamic_validation(self) -> None:
        ...

    async def collect(self) -> t.Any:
        """Evaluate the argument before calling the data function."""
        parameter_kind = self.parameter_kind()
        if DATASET.isin(parameter_kind):
            dataset = t.cast(st.Dataset, self.static_value())
            if self.kind is None:
                raise ValueError(
                    f"Parameter {self.name()} is a Dataset, but no type "
                    "to cast to is defined."
                )
            return dataset.to(self.dataset_types[self.kind])
        elif SCALAR.isin(parameter_kind):
            scalar = t.cast(st.Scalar, self.static_value())
            return scalar.value()
        else:
            return self.static_value()

    async def admin_data(self) -> t.Optional[pa.Table]:
        if not self.is_pep():
            return None

        dataset = t.cast(st.Dataset, self.static_value())
        return await async_admin_data(dataset)


class SarusBoundSignature:
    """A BoundSignature is a list of BoundArguments."""

    def __init__(self, arguments: t.List[SarusBoundArgument]):
        self.arguments = arguments
        self._argument_map = {arg.name(): arg for arg in self.arguments}
        self.static_validation()

    def is_dp(self) -> bool:
        return "budget" in self._argument_map and "seed" in self._argument_map

    def __getitem__(self, name: str) -> SarusBoundArgument:
        return self._argument_map[name]

    def static_validation(self) -> None:
        """Check that the arguments have the correct dataspec type."""
        for arg in self.arguments:
            arg.static_validation()

    async def dynamic_validation(self) -> None:
        """Compare the values with the annotations.

        TODO: Not used yet. Annotations needs to be curated to
        remove ForwardRefs.
        """
        for arg in self.arguments:
            await arg.dynamic_validation()

    def static_kwargs(self) -> t.Dict[str, t.Any]:
        """Return non evaluated arguments."""
        return {
            arg.parameter.name: arg.static_value() for arg in self.arguments
        }

    def static_args(self) -> t.List[t.Any]:
        """Return non evaluated arguments."""
        return [arg.static_value() for arg in self.arguments]

    async def collect_kwargs(self) -> t.Dict[str, t.Any]:
        """Evaluate arguments for calling the data function."""
        return {
            arg.parameter.name: await arg.collect() for arg in self.arguments
        }

    async def collect_args(self) -> t.List[t.Any]:
        """Evaluate arguments for calling the data function."""
        return [await arg.collect() for arg in self.arguments]

    async def collect_kwargs_method(
        self,
    ) -> t.Tuple[t.Any, t.Dict[str, t.Any]]:
        """Evaluate the arguments but separate the first argument from the
        rest. This is useful to evaluate a method.
        """
        first_value = await self.arguments[0].collect()
        other_values = {
            arg.parameter.name: await arg.collect()
            for arg in self.arguments[1:]
        }
        return first_value, other_values

    def pep_token(self) -> t.Optional[str]:
        """Compute the PEP token of the inputs.

        A PEP token exists if:
          - all input dataspecs are PEP or PUBLIC
          - there must be at least one input PEP dataspec
          - if there are more that one input PEP dataspecs, all PEP inputs must
            have the same token
        """
        if not all(
            [arg.is_public() or arg.is_pep() for arg in self.arguments]
        ):
            return None

        tokens = [arg.pep_token() for arg in self.arguments]
        unique_tokens = set([token for token in tokens if token is not None])
        if len(unique_tokens) != 1:
            return None
        else:
            return unique_tokens.pop()

    async def admin_data(self) -> pa.Table:
        """Return the admin data of the inputs."""
        protected_entities = [
            await arg.admin_data() for arg in self.arguments if arg.is_pep()
        ]
        return validate_admin_data(protected_entities)


def extended_is_instance(obj: t.Any, kind: t.Type) -> bool:
    """Extended version of isinstance that also checks composite types."""
    if t.get_origin(kind) is None:
        if isinstance(kind, t.ForwardRef):
            return False
        else:
            return isinstance(obj, kind)
    elif t.get_origin(kind) == t.Union:
        return any(
            extended_is_instance(obj, subkind) for subkind in t.get_args(kind)
        )
    elif t.get_origin(kind) == t.Optional:
        (subkind,) = t.get_args(kind)
        return obj is None or extended_is_instance(obj, subkind)
    elif t.get_origin(kind) in [t.List, list]:
        return isinstance(obj, list)
    else:
        raise NotImplementedError(
            f"Dynamic type checking not implemented for {kind}."
        )
