"""_534.py

ConicalGearMeshRating
"""
from typing import List

from mastapy.gears.load_case.conical import _882
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.conical import _540
from mastapy.gears.rating import _356
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshRating',)


class ConicalGearMeshRating(_356.GearMeshRating):
    """ConicalGearMeshRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_RATING

    class _Cast_ConicalGearMeshRating:
        """Special nested class for casting ConicalGearMeshRating to subclasses."""

        def __init__(self, parent: 'ConicalGearMeshRating'):
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
        def zerol_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.zerol_bevel import _365
            
            return self._parent._cast(_365.ZerolBevelGearMeshRating)

        @property
        def straight_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.straight_bevel import _391
            
            return self._parent._cast(_391.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(self):
            from mastapy.gears.rating.straight_bevel_diff import _394
            
            return self._parent._cast(_394.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.spiral_bevel import _398
            
            return self._parent._cast(_398.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _401
            
            return self._parent._cast(_401.KlingelnbergCycloPalloidSpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _404
            
            return self._parent._cast(_404.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_conical import _407
            
            return self._parent._cast(_407.KlingelnbergCycloPalloidConicalGearMeshRating)

        @property
        def hypoid_gear_mesh_rating(self):
            from mastapy.gears.rating.hypoid import _434
            
            return self._parent._cast(_434.HypoidGearMeshRating)

        @property
        def bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.bevel import _549
            
            return self._parent._cast(_549.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _560
            
            return self._parent._cast(_560.AGMAGleasonConicalGearMeshRating)

        @property
        def conical_gear_mesh_rating(self) -> 'ConicalGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_load_case(self) -> '_882.ConicalMeshLoadCase':
        """ConicalMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_mesh_load_case(self) -> '_882.ConicalMeshLoadCase':
        """ConicalMeshLoadCase: 'ConicalMeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalMeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def meshed_gears(self) -> 'List[_540.ConicalMeshedGearRating]':
        """List[ConicalMeshedGearRating]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearMeshRating._Cast_ConicalGearMeshRating':
        return self._Cast_ConicalGearMeshRating(self)
