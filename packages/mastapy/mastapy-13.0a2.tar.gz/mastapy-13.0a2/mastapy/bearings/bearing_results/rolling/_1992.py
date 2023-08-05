"""_1992.py

LoadedCylindricalRollerBearingDutyCycle
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2008
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CYLINDRICAL_ROLLER_BEARING_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedCylindricalRollerBearingDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedCylindricalRollerBearingDutyCycle',)


class LoadedCylindricalRollerBearingDutyCycle(_2008.LoadedNonBarrelRollerBearingDutyCycle):
    """LoadedCylindricalRollerBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_CYLINDRICAL_ROLLER_BEARING_DUTY_CYCLE

    class _Cast_LoadedCylindricalRollerBearingDutyCycle:
        """Special nested class for casting LoadedCylindricalRollerBearingDutyCycle to subclasses."""

        def __init__(self, parent: 'LoadedCylindricalRollerBearingDutyCycle'):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(self):
            return self._parent._cast(_2008.LoadedNonBarrelRollerBearingDutyCycle)

        @property
        def loaded_rolling_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results import _1944
            
            return self._parent._cast(_1944.LoadedRollingBearingDutyCycle)

        @property
        def loaded_non_linear_bearing_duty_cycle_results(self):
            from mastapy.bearings.bearing_results import _1941
            
            return self._parent._cast(_1941.LoadedNonLinearBearingDutyCycleResults)

        @property
        def loaded_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results import _1933
            
            return self._parent._cast(_1933.LoadedBearingDutyCycle)

        @property
        def loaded_cylindrical_roller_bearing_duty_cycle(self) -> 'LoadedCylindricalRollerBearingDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedCylindricalRollerBearingDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def permissible_continuous_axial_load_safety_factor(self) -> 'float':
        """float: 'PermissibleContinuousAxialLoadSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleContinuousAxialLoadSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedCylindricalRollerBearingDutyCycle._Cast_LoadedCylindricalRollerBearingDutyCycle':
        return self._Cast_LoadedCylindricalRollerBearingDutyCycle(self)
