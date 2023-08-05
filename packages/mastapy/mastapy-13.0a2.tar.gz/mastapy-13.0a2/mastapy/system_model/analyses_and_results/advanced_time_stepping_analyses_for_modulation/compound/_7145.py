"""_7145.py

CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from typing import List

from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7015
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7191
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation',)


class CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation(_7191.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation):
    """CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def pulley_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7191.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7142
            
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
        def cvt_pulley_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_7015.CVTPulleyAdvancedTimeSteppingAnalysisForModulation]':
        """List[CVTPulleyAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_7015.CVTPulleyAdvancedTimeSteppingAnalysisForModulation]':
        """List[CVTPulleyAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation(self)
