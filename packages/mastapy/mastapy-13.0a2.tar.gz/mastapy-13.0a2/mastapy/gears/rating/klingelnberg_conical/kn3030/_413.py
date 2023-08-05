"""_413.py

KlingelnbergCycloPalloidHypoidGearSingleFlankRating
"""
from mastapy._internal import constructor
from mastapy.gears.rating.klingelnberg_conical.kn3030 import _412
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergConical.KN3030', 'KlingelnbergCycloPalloidHypoidGearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSingleFlankRating',)


class KlingelnbergCycloPalloidHypoidGearSingleFlankRating(_412.KlingelnbergCycloPalloidConicalGearSingleFlankRating):
    """KlingelnbergCycloPalloidHypoidGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SINGLE_FLANK_RATING

    class _Cast_KlingelnbergCycloPalloidHypoidGearSingleFlankRating:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSingleFlankRating to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearSingleFlankRating'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_single_flank_rating(self):
            return self._parent._cast(_412.KlingelnbergCycloPalloidConicalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(self):
            from mastapy.gears.rating import _360
            
            return self._parent._cast(_360.GearSingleFlankRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_single_flank_rating(self) -> 'KlingelnbergCycloPalloidHypoidGearSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def tangential_speed(self) -> 'float':
        """float: 'TangentialSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearSingleFlankRating._Cast_KlingelnbergCycloPalloidHypoidGearSingleFlankRating':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSingleFlankRating(self)
