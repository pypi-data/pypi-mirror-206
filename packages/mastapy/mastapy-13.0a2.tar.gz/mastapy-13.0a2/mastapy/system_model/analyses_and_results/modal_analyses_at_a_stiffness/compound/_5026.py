"""_5026.py

KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4898
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4992
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness',)


class KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness(_4992.ConicalGearCompoundModalAnalysisAtAStiffness):
    """KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4992.ConicalGearCompoundModalAnalysisAtAStiffness)

        @property
        def gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5018
            
            return self._parent._cast(_5018.GearCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5037
            
            return self._parent._cast(_5037.MountableComponentCompoundModalAnalysisAtAStiffness)

        @property
        def component_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4985
            
            return self._parent._cast(_4985.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5039
            
            return self._parent._cast(_5039.PartCompoundModalAnalysisAtAStiffness)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5029
            
            return self._parent._cast(_5029.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5032
            
            return self._parent._cast(_5032.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(self) -> 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4898.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness]':
        """List[KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4898.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness]':
        """List[KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness':
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness(self)
