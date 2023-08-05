"""_7148.py

CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from typing import List

from mastapy.system_model.part_model.cycloidal import _2548
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7017
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7104
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation',)


class CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation(_7104.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation):
    """CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def abstract_shaft_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7104.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_or_housing_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7105
            
            return self._parent._cast(_7105.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation)

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
        def cycloidal_disc_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2548.CycloidalDisc':
        """CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_7017.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation]':
        """List[CycloidalDiscAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_7017.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation]':
        """List[CycloidalDiscAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation(self)
