"""_406.py

KlingelnbergCycloPalloidHypoidGearSetRating
"""
from typing import List

from mastapy.gears.gear_designs.klingelnberg_hypoid import _974
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.klingelnberg_hypoid import _405, _404
from mastapy.gears.rating.klingelnberg_conical import _409
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergHypoid', 'KlingelnbergCycloPalloidHypoidGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetRating',)


class KlingelnbergCycloPalloidHypoidGearSetRating(_409.KlingelnbergCycloPalloidConicalGearSetRating):
    """KlingelnbergCycloPalloidHypoidGearSetRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_RATING

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetRating:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetRating to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearSetRating'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(self):
            return self._parent._cast(_409.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def conical_gear_set_rating(self):
            from mastapy.gears.rating.conical import _537
            
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
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(self) -> 'KlingelnbergCycloPalloidHypoidGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_974.KlingelnbergCycloPalloidHypoidGearSetDesign':
        """KlingelnbergCycloPalloidHypoidGearSetDesign: 'KlingelnbergCycloPalloidHypoidGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_ratings(self) -> 'List[_405.KlingelnbergCycloPalloidHypoidGearRating]':
        """List[KlingelnbergCycloPalloidHypoidGearRating]: 'KlingelnbergCycloPalloidHypoidGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_mesh_ratings(self) -> 'List[_404.KlingelnbergCycloPalloidHypoidGearMeshRating]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshRating]: 'KlingelnbergCycloPalloidHypoidMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetRating(self)
