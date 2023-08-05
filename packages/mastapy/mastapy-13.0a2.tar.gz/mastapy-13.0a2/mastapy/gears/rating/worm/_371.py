"""_371.py

WormGearSetDutyCycleRating
"""
from mastapy.gears.rating import _358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Worm', 'WormGearSetDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetDutyCycleRating',)


class WormGearSetDutyCycleRating(_358.GearSetDutyCycleRating):
    """WormGearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_DUTY_CYCLE_RATING

    class _Cast_WormGearSetDutyCycleRating:
        """Special nested class for casting WormGearSetDutyCycleRating to subclasses."""

        def __init__(self, parent: 'WormGearSetDutyCycleRating'):
            self._parent = parent

        @property
        def gear_set_duty_cycle_rating(self):
            return self._parent._cast(_358.GearSetDutyCycleRating)

        @property
        def abstract_gear_set_rating(self):
            from mastapy.gears.rating import _351
            
            return self._parent._cast(_351.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def worm_gear_set_duty_cycle_rating(self) -> 'WormGearSetDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearSetDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'WormGearSetDutyCycleRating._Cast_WormGearSetDutyCycleRating':
        return self._Cast_WormGearSetDutyCycleRating(self)
