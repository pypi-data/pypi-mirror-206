"""_409.py

KlingelnbergCycloPalloidConicalGearSetRating
"""
from mastapy._internal import constructor
from mastapy.gears.rating.conical import _537
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergConical', 'KlingelnbergCycloPalloidConicalGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearSetRating',)


class KlingelnbergCycloPalloidConicalGearSetRating(_537.ConicalGearSetRating):
    """KlingelnbergCycloPalloidConicalGearSetRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_RATING

    class _Cast_KlingelnbergCycloPalloidConicalGearSetRating:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetRating to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearSetRating'):
            self._parent = parent

        @property
        def conical_gear_set_rating(self):
            return self._parent._cast(_537.ConicalGearSetRating)

        @property
        def gear_set_rating(self):
            from mastapy.gears.rating import _359
            
            return self._parent._cast(_359.GearSetRating)

        @property
        def abstract_gear_set_rating(self):
            from mastapy.gears.rating import _351
            
            return self._parent._cast(_351.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _403
            
            return self._parent._cast(_403.KlingelnbergCycloPalloidSpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _406
            
            return self._parent._cast(_406.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(self) -> 'KlingelnbergCycloPalloidConicalGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> 'str':
        """str: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearSetRating._Cast_KlingelnbergCycloPalloidConicalGearSetRating':
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetRating(self)
