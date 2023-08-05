"""_961.py

StraightBevelDiffGearMeshDesign
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.straight_bevel_diff import _962, _960, _963
from mastapy.gears.gear_designs.bevel import _1175
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.StraightBevelDiff', 'StraightBevelDiffGearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearMeshDesign',)


class StraightBevelDiffGearMeshDesign(_1175.BevelGearMeshDesign):
    """StraightBevelDiffGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_DESIGN

    class _Cast_StraightBevelDiffGearMeshDesign:
        """Special nested class for casting StraightBevelDiffGearMeshDesign to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearMeshDesign'):
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
        def straight_bevel_diff_gear_mesh_design(self) -> 'StraightBevelDiffGearMeshDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_performance_torque(self) -> 'float':
        """float: 'PinionPerformanceTorque' is the original name of this property."""

        temp = self.wrapped.PinionPerformanceTorque

        if temp is None:
            return 0.0

        return temp

    @pinion_performance_torque.setter
    def pinion_performance_torque(self, value: 'float'):
        self.wrapped.PinionPerformanceTorque = float(value) if value else 0.0

    @property
    def straight_bevel_diff_gear_set(self) -> '_962.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'StraightBevelDiffGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_diff_gears(self) -> 'List[_960.StraightBevelDiffGearDesign]':
        """List[StraightBevelDiffGearDesign]: 'StraightBevelDiffGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_meshed_gears(self) -> 'List[_963.StraightBevelDiffMeshedGearDesign]':
        """List[StraightBevelDiffMeshedGearDesign]: 'StraightBevelDiffMeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelDiffGearMeshDesign._Cast_StraightBevelDiffGearMeshDesign':
        return self._Cast_StraightBevelDiffGearMeshDesign(self)
