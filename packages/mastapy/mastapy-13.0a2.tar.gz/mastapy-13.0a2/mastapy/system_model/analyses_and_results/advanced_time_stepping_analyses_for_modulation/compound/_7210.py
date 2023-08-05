"""_7210.py

StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from typing import List

from mastapy.system_model.part_model.gears import _2525
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7081
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7208, _7209, _7121
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation',)


class StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(_7121.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation):
    """StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7121.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7109
            
            return self._parent._cast(_7109.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7137
            
            return self._parent._cast(_7137.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7163
            
            return self._parent._cast(_7163.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7201
            
            return self._parent._cast(_7201.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7103
            
            return self._parent._cast(_7103.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7182
            
            return self._parent._cast(_7182.PartCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2525.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def assembly_analysis_cases_ready(self) -> 'List[_7081.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation]':
        """List[StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gears_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7208.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation]: 'StraightBevelDiffGearsCompoundAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearsCompoundAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_meshes_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7209.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation]: 'StraightBevelDiffMeshesCompoundAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshesCompoundAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_7081.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation]':
        """List[StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(self)
