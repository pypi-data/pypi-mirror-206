"""_372.py

WormGearSetRating
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.worm import _954
from mastapy.gears.rating.worm import _370, _369
from mastapy.gears.rating import _359
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Worm', 'WormGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetRating',)


class WormGearSetRating(_359.GearSetRating):
    """WormGearSetRating

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_RATING

    class _Cast_WormGearSetRating:
        """Special nested class for casting WormGearSetRating to subclasses."""

        def __init__(self, parent: 'WormGearSetRating'):
            self._parent = parent

        @property
        def gear_set_rating(self):
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
        def worm_gear_set_rating(self) -> 'WormGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearSetRating.TYPE'):
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
    def worm_gear_set(self) -> '_954.WormGearSetDesign':
        """WormGearSetDesign: 'WormGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratings(self) -> 'List[_370.WormGearRating]':
        """List[WormGearRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gear_ratings(self) -> 'List[_370.WormGearRating]':
        """List[WormGearRating]: 'WormGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_mesh_ratings(self) -> 'List[_369.WormGearMeshRating]':
        """List[WormGearMeshRating]: 'WormMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'WormGearSetRating._Cast_WormGearSetRating':
        return self._Cast_WormGearSetRating(self)
