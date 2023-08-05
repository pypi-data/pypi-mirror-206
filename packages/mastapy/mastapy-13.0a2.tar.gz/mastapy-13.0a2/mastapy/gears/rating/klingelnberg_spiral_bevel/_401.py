"""_401.py

KlingelnbergCycloPalloidSpiralBevelGearMeshRating
"""
from typing import List

from mastapy.gears.rating.klingelnberg_conical.kn3030 import _415
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _969
from mastapy.gears.rating.klingelnberg_spiral_bevel import _402
from mastapy.gears.rating.klingelnberg_conical import _407
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergSpiralBevel', 'KlingelnbergCycloPalloidSpiralBevelGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearMeshRating',)


class KlingelnbergCycloPalloidSpiralBevelGearMeshRating(_407.KlingelnbergCycloPalloidConicalGearMeshRating):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_RATING

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshRating to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelGearMeshRating'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(self):
            return self._parent._cast(_407.KlingelnbergCycloPalloidConicalGearMeshRating)

        @property
        def conical_gear_mesh_rating(self):
            from mastapy.gears.rating.conical import _534
            
            return self._parent._cast(_534.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(self):
            from mastapy.gears.rating import _356
            
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
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def kn3030_klingelnberg_mesh_single_flank_rating(self) -> '_415.KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating':
        """KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating: 'KN3030KlingelnbergMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KN3030KlingelnbergMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_969.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearMeshDesign: 'KlingelnbergCycloPalloidSpiralBevelGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_ratings(self) -> 'List[_402.KlingelnbergCycloPalloidSpiralBevelGearRating]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearRating]: 'KlingelnbergCycloPalloidSpiralBevelGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearMeshRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshRating(self)
