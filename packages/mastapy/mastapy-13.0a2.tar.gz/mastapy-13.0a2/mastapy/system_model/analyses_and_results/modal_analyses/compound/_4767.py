"""_4767.py

KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses import _4618
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4733
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis',)


class KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis(_4733.ConicalGearCompoundModalAnalysis):
    """KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis'):
            self._parent = parent

        @property
        def conical_gear_compound_modal_analysis(self):
            return self._parent._cast(_4733.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4759
            
            return self._parent._cast(_4759.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4778
            
            return self._parent._cast(_4778.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4726
            
            return self._parent._cast(_4726.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4780
            
            return self._parent._cast(_4780.PartCompoundModalAnalysis)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4770
            
            return self._parent._cast(_4770.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4773
            
            return self._parent._cast(_4773.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(self) -> 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4618.KlingelnbergCycloPalloidConicalGearModalAnalysis]':
        """List[KlingelnbergCycloPalloidConicalGearModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4618.KlingelnbergCycloPalloidConicalGearModalAnalysis]':
        """List[KlingelnbergCycloPalloidConicalGearModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis':
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis(self)
