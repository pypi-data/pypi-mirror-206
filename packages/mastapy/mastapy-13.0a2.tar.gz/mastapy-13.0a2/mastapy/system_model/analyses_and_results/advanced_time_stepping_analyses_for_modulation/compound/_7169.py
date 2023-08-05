"""_7169.py

KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from typing import List

from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7040
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7135
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation',)


class KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation(_7135.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation):
    """KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7135.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7161
            
            return self._parent._cast(_7161.GearCompoundAdvancedTimeSteppingAnalysisForModulation)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7172
            
            return self._parent._cast(_7172.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7175
            
            return self._parent._cast(_7175.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_7040.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation]':
        """List[KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_7040.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation]':
        """List[KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation(self)
