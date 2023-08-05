"""_7081.py

StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
"""
from typing import List

from mastapy.system_model.part_model.gears import _2525
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6925
from mastapy.system_model.analyses_and_results.system_deflections import _2793
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7079, _7080, _6991
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation',)


class StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation(_6991.BevelGearSetAdvancedTimeSteppingAnalysisForModulation):
    """StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_6991.BevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6978
            
            return self._parent._cast(_6978.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7007
            
            return self._parent._cast(_7007.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7033
            
            return self._parent._cast(_7033.GearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7072
            
            return self._parent._cast(_7072.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6969
            
            return self._parent._cast(_6969.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7053
            
            return self._parent._cast(_7053.PartAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

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
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(self) -> 'StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2525.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6925.StraightBevelDiffGearSetLoadCase':
        """StraightBevelDiffGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2793.StraightBevelDiffGearSetSystemDeflection':
        """StraightBevelDiffGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_diff_gears_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7079.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation]':
        """List[StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation]: 'StraightBevelDiffGearsAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearsAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_meshes_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7080.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation]':
        """List[StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation]: 'StraightBevelDiffMeshesAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshesAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation(self)
