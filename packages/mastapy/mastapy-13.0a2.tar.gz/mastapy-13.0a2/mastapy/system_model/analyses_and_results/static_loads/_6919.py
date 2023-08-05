"""_6919.py

SpiralBevelGearSetLoadCase
"""
from typing import List

from mastapy.system_model.part_model.gears import _2523
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6917, _6918, _6794
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpiralBevelGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetLoadCase',)


class SpiralBevelGearSetLoadCase(_6794.BevelGearSetLoadCase):
    """SpiralBevelGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_LOAD_CASE

    class _Cast_SpiralBevelGearSetLoadCase:
        """Special nested class for casting SpiralBevelGearSetLoadCase to subclasses."""

        def __init__(self, parent: 'SpiralBevelGearSetLoadCase'):
            self._parent = parent

        @property
        def bevel_gear_set_load_case(self):
            return self._parent._cast(_6794.BevelGearSetLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6780
            
            return self._parent._cast(_6780.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6812
            
            return self._parent._cast(_6812.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6859
            
            return self._parent._cast(_6859.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6916
            
            return self._parent._cast(_6916.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6771
            
            return self._parent._cast(_6771.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.PartLoadCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_load_case(self) -> 'SpiralBevelGearSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2523.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_6917.SpiralBevelGearLoadCase]':
        """List[SpiralBevelGearLoadCase]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gears_load_case(self) -> 'List[_6917.SpiralBevelGearLoadCase]':
        """List[SpiralBevelGearLoadCase]: 'SpiralBevelGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_meshes_load_case(self) -> 'List[_6918.SpiralBevelGearMeshLoadCase]':
        """List[SpiralBevelGearMeshLoadCase]: 'SpiralBevelMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase':
        return self._Cast_SpiralBevelGearSetLoadCase(self)
