"""_5284.py

KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5156
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5250
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed',)


class KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed(_5250.ConicalGearCompoundModalAnalysisAtASpeed):
    """KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5250.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5276
            
            return self._parent._cast(_5276.GearCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5295
            
            return self._parent._cast(_5295.MountableComponentCompoundModalAnalysisAtASpeed)

        @property
        def component_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5243
            
            return self._parent._cast(_5243.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5297
            
            return self._parent._cast(_5297.PartCompoundModalAnalysisAtASpeed)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5287
            
            return self._parent._cast(_5287.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5290
            
            return self._parent._cast(_5290.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(self) -> 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5156.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed]':
        """List[KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5156.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed]':
        """List[KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed':
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed(self)
