"""_957.py

StraightBevelGearMeshDesign
"""
from typing import List

from mastapy.gears.gear_designs.straight_bevel import _958, _956, _959
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1175
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.StraightBevel', 'StraightBevelGearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearMeshDesign',)


class StraightBevelGearMeshDesign(_1175.BevelGearMeshDesign):
    """StraightBevelGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_DESIGN

    class _Cast_StraightBevelGearMeshDesign:
        """Special nested class for casting StraightBevelGearMeshDesign to subclasses."""

        def __init__(self, parent: 'StraightBevelGearMeshDesign'):
            self._parent = parent

        @property
        def bevel_gear_mesh_design(self):
            return self._parent._cast(_1175.BevelGearMeshDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1188
            
            return self._parent._cast(_1188.AGMAGleasonConicalGearMeshDesign)

        @property
        def conical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.conical import _1149
            
            return self._parent._cast(_1149.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(self):
            from mastapy.gears.gear_designs import _944
            
            return self._parent._cast(_944.GearMeshDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def straight_bevel_gear_mesh_design(self) -> 'StraightBevelGearMeshDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def straight_bevel_gear_set(self) -> '_958.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'StraightBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_gears(self) -> 'List[_956.StraightBevelGearDesign]':
        """List[StraightBevelGearDesign]: 'StraightBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshed_gears(self) -> 'List[_959.StraightBevelMeshedGearDesign]':
        """List[StraightBevelMeshedGearDesign]: 'StraightBevelMeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelGearMeshDesign._Cast_StraightBevelGearMeshDesign':
        return self._Cast_StraightBevelGearMeshDesign(self)
