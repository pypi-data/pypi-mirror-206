"""_369.py

WormGearMeshRating
"""
from typing import List

from mastapy.gears.gear_designs.worm import _953
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _370
from mastapy.gears.rating import _356
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Worm', 'WormGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearMeshRating',)


class WormGearMeshRating(_356.GearMeshRating):
    """WormGearMeshRating

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_RATING

    class _Cast_WormGearMeshRating:
        """Special nested class for casting WormGearMeshRating to subclasses."""

        def __init__(self, parent: 'WormGearMeshRating'):
            self._parent = parent

        @property
        def gear_mesh_rating(self):
            return self._parent._cast(_356.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(self):
            from mastapy.gears.rating import _349
            
            return self._parent._cast(_349.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def worm_gear_mesh_rating(self) -> 'WormGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worm_gear_mesh(self) -> '_953.WormGearMeshDesign':
        """WormGearMeshDesign: 'WormGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def cast_to(self) -> 'WormGearMeshRating._Cast_WormGearMeshRating':
        return self._Cast_WormGearMeshRating(self)
