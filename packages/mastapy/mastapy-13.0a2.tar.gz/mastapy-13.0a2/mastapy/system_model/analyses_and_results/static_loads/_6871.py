"""_6871.py

HypoidGearSetLoadCase
"""
from typing import List

from mastapy.system_model.part_model.gears import _2514
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6869, _6870, _6780
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HypoidGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetLoadCase',)


class HypoidGearSetLoadCase(_6780.AGMAGleasonConicalGearSetLoadCase):
    """HypoidGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_LOAD_CASE

    class _Cast_HypoidGearSetLoadCase:
        """Special nested class for casting HypoidGearSetLoadCase to subclasses."""

        def __init__(self, parent: 'HypoidGearSetLoadCase'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_load_case(self):
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
        def hypoid_gear_set_load_case(self) -> 'HypoidGearSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2514.HypoidGearSet':
        """HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_6869.HypoidGearLoadCase]':
        """List[HypoidGearLoadCase]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gears_load_case(self) -> 'List[_6869.HypoidGearLoadCase]':
        """List[HypoidGearLoadCase]: 'HypoidGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes_load_case(self) -> 'List[_6870.HypoidGearMeshLoadCase]':
        """List[HypoidGearMeshLoadCase]: 'HypoidMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase':
        return self._Cast_HypoidGearSetLoadCase(self)
