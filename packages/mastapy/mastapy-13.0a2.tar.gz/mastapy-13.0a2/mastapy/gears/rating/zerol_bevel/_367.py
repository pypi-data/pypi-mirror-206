"""_367.py

ZerolBevelGearSetRating
"""
from typing import List

from mastapy.gears.gear_designs.zerol_bevel import _949
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.zerol_bevel import _366, _365
from mastapy.gears.rating.bevel import _551
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.ZerolBevel', 'ZerolBevelGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetRating',)


class ZerolBevelGearSetRating(_551.BevelGearSetRating):
    """ZerolBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_RATING

    class _Cast_ZerolBevelGearSetRating:
        """Special nested class for casting ZerolBevelGearSetRating to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearSetRating'):
            self._parent = parent

        @property
        def bevel_gear_set_rating(self):
            return self._parent._cast(_551.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _562
            
            return self._parent._cast(_562.AGMAGleasonConicalGearSetRating)

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
        def zerol_bevel_gear_set_rating(self) -> 'ZerolBevelGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def zerol_bevel_gear_set(self) -> '_949.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'ZerolBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gear_ratings(self) -> 'List[_366.ZerolBevelGearRating]':
        """List[ZerolBevelGearRating]: 'ZerolBevelGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_mesh_ratings(self) -> 'List[_365.ZerolBevelGearMeshRating]':
        """List[ZerolBevelGearMeshRating]: 'ZerolBevelMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating':
        return self._Cast_ZerolBevelGearSetRating(self)
