"""_405.py

KlingelnbergCycloPalloidHypoidGearRating
"""
from mastapy.gears.gear_designs.klingelnberg_hypoid import _972
from mastapy._internal import constructor
from mastapy.gears.rating.klingelnberg_conical import _408
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergHypoid', 'KlingelnbergCycloPalloidHypoidGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearRating',)


class KlingelnbergCycloPalloidHypoidGearRating(_408.KlingelnbergCycloPalloidConicalGearRating):
    """KlingelnbergCycloPalloidHypoidGearRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_RATING

    class _Cast_KlingelnbergCycloPalloidHypoidGearRating:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearRating to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearRating'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(self):
            return self._parent._cast(_408.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def conical_gear_rating(self):
            from mastapy.gears.rating.conical import _535
            
            return self._parent._cast(_535.ConicalGearRating)

        @property
        def gear_rating(self):
            from mastapy.gears.rating import _357
            
            return self._parent._cast(_357.GearRating)

        @property
        def abstract_gear_rating(self):
            from mastapy.gears.rating import _350
            
            return self._parent._cast(_350.AbstractGearRating)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(self) -> 'KlingelnbergCycloPalloidHypoidGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_972.KlingelnbergCycloPalloidHypoidGearDesign':
        """KlingelnbergCycloPalloidHypoidGearDesign: 'KlingelnbergCycloPalloidHypoidGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearRating._Cast_KlingelnbergCycloPalloidHypoidGearRating':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearRating(self)
