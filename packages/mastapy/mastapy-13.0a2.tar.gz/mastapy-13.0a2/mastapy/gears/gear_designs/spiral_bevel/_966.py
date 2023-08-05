"""_966.py

SpiralBevelGearSetDesign
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.spiral_bevel import _964, _965
from mastapy.gears.gear_designs.bevel import _1176
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.SpiralBevel', 'SpiralBevelGearSetDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetDesign',)


class SpiralBevelGearSetDesign(_1176.BevelGearSetDesign):
    """SpiralBevelGearSetDesign

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_DESIGN

    class _Cast_SpiralBevelGearSetDesign:
        """Special nested class for casting SpiralBevelGearSetDesign to subclasses."""

        def __init__(self, parent: 'SpiralBevelGearSetDesign'):
            self._parent = parent

        @property
        def bevel_gear_set_design(self):
            return self._parent._cast(_1176.BevelGearSetDesign)

        @property
        def agma_gleason_conical_gear_set_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1189
            
            return self._parent._cast(_1189.AGMAGleasonConicalGearSetDesign)

        @property
        def conical_gear_set_design(self):
            from mastapy.gears.gear_designs.conical import _1150
            
            return self._parent._cast(_1150.ConicalGearSetDesign)

        @property
        def gear_set_design(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearSetDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def spiral_bevel_gear_set_design(self) -> 'SpiralBevelGearSetDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_number_of_teeth_for_recommended_tooth_proportions(self) -> 'int':
        """int: 'MinimumNumberOfTeethForRecommendedToothProportions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumNumberOfTeethForRecommendedToothProportions

        if temp is None:
            return 0

        return temp

    @property
    def gears(self) -> 'List[_964.SpiralBevelGearDesign]':
        """List[SpiralBevelGearDesign]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gears(self) -> 'List[_964.SpiralBevelGearDesign]':
        """List[SpiralBevelGearDesign]: 'SpiralBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_meshes(self) -> 'List[_965.SpiralBevelGearMeshDesign]':
        """List[SpiralBevelGearMeshDesign]: 'SpiralBevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpiralBevelGearSetDesign._Cast_SpiralBevelGearSetDesign':
        return self._Cast_SpiralBevelGearSetDesign(self)
