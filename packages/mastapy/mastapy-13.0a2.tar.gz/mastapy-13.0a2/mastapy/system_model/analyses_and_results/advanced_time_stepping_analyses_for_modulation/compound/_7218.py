"""_7218.py

SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from typing import List

from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7089
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation',)


class SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation(_7142.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation):
    """SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7142.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7180
            
            return self._parent._cast(_7180.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7128
            
            return self._parent._cast(_7128.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation)

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
        def synchroniser_half_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7217
            
            return self._parent._cast(_7217.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_sleeve_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7219
            
            return self._parent._cast(_7219.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_part_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_7089.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation]':
        """List[SynchroniserPartAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_7089.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation]':
        """List[SynchroniserPartAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation(self)
