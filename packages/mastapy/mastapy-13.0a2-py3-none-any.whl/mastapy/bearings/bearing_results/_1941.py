"""_1941.py

LoadedNonLinearBearingDutyCycleResults
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1933
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_LINEAR_BEARING_DUTY_CYCLE_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedNonLinearBearingDutyCycleResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedNonLinearBearingDutyCycleResults',)


class LoadedNonLinearBearingDutyCycleResults(_1933.LoadedBearingDutyCycle):
    """LoadedNonLinearBearingDutyCycleResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_LINEAR_BEARING_DUTY_CYCLE_RESULTS

    class _Cast_LoadedNonLinearBearingDutyCycleResults:
        """Special nested class for casting LoadedNonLinearBearingDutyCycleResults to subclasses."""

        def __init__(self, parent: 'LoadedNonLinearBearingDutyCycleResults'):
            self._parent = parent

        @property
        def loaded_bearing_duty_cycle(self):
            return self._parent._cast(_1933.LoadedBearingDutyCycle)

        @property
        def loaded_rolling_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results import _1944
            
            return self._parent._cast(_1944.LoadedRollingBearingDutyCycle)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _1977
            
            return self._parent._cast(_1977.LoadedAxialThrustCylindricalRollerBearingDutyCycle)

        @property
        def loaded_ball_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _1984
            
            return self._parent._cast(_1984.LoadedBallBearingDutyCycle)

        @property
        def loaded_cylindrical_roller_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _1992
            
            return self._parent._cast(_1992.LoadedCylindricalRollerBearingDutyCycle)

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _2008
            
            return self._parent._cast(_2008.LoadedNonBarrelRollerBearingDutyCycle)

        @property
        def loaded_taper_roller_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _2031
            
            return self._parent._cast(_2031.LoadedTaperRollerBearingDutyCycle)

        @property
        def loaded_non_linear_bearing_duty_cycle_results(self) -> 'LoadedNonLinearBearingDutyCycleResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedNonLinearBearingDutyCycleResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def total_power_loss(self) -> 'float':
        """float: 'TotalPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults':
        return self._Cast_LoadedNonLinearBearingDutyCycleResults(self)
