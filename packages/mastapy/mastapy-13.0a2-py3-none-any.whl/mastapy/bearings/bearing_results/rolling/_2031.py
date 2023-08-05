"""_2031.py

LoadedTaperRollerBearingDutyCycle
"""
from mastapy.bearings.bearing_results.rolling import _2008
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TAPER_ROLLER_BEARING_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedTaperRollerBearingDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedTaperRollerBearingDutyCycle',)


class LoadedTaperRollerBearingDutyCycle(_2008.LoadedNonBarrelRollerBearingDutyCycle):
    """LoadedTaperRollerBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_TAPER_ROLLER_BEARING_DUTY_CYCLE

    class _Cast_LoadedTaperRollerBearingDutyCycle:
        """Special nested class for casting LoadedTaperRollerBearingDutyCycle to subclasses."""

        def __init__(self, parent: 'LoadedTaperRollerBearingDutyCycle'):
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
        def loaded_taper_roller_bearing_duty_cycle(self) -> 'LoadedTaperRollerBearingDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedTaperRollerBearingDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle':
        return self._Cast_LoadedTaperRollerBearingDutyCycle(self)
