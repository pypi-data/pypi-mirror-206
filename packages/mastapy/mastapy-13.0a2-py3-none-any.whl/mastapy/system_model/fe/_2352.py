"""_2352.py

DegreeOfFreedomBoundaryConditionAngular
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.fe import _2351
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DEGREE_OF_FREEDOM_BOUNDARY_CONDITION_ANGULAR = python_net_import('SMT.MastaAPI.SystemModel.FE', 'DegreeOfFreedomBoundaryConditionAngular')


__docformat__ = 'restructuredtext en'
__all__ = ('DegreeOfFreedomBoundaryConditionAngular',)


class DegreeOfFreedomBoundaryConditionAngular(_2351.DegreeOfFreedomBoundaryCondition):
    """DegreeOfFreedomBoundaryConditionAngular

    This is a mastapy class.
    """

    TYPE = _DEGREE_OF_FREEDOM_BOUNDARY_CONDITION_ANGULAR

    class _Cast_DegreeOfFreedomBoundaryConditionAngular:
        """Special nested class for casting DegreeOfFreedomBoundaryConditionAngular to subclasses."""

        def __init__(self, parent: 'DegreeOfFreedomBoundaryConditionAngular'):
            self._parent = parent

        @property
        def degree_of_freedom_boundary_condition(self):
            return self._parent._cast(_2351.DegreeOfFreedomBoundaryCondition)

        @property
        def degree_of_freedom_boundary_condition_angular(self) -> 'DegreeOfFreedomBoundaryConditionAngular':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DegreeOfFreedomBoundaryConditionAngular.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Angle' is the original name of this property."""

        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @angle.setter
    def angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Angle = value

    @property
    def torque(self) -> 'float':
        """float: 'Torque' is the original name of this property."""

        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @torque.setter
    def torque(self, value: 'float'):
        self.wrapped.Torque = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'DegreeOfFreedomBoundaryConditionAngular._Cast_DegreeOfFreedomBoundaryConditionAngular':
        return self._Cast_DegreeOfFreedomBoundaryConditionAngular(self)
