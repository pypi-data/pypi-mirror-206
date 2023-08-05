"""_5083.py

WormGearCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.part_model.gears import _2530
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4955
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5018
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'WormGearCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearCompoundModalAnalysisAtAStiffness',)


class WormGearCompoundModalAnalysisAtAStiffness(_5018.GearCompoundModalAnalysisAtAStiffness):
    """WormGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_WormGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting WormGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'WormGearCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def gear_compound_modal_analysis_at_a_stiffness(self):
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
        def worm_gear_compound_modal_analysis_at_a_stiffness(self) -> 'WormGearCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2530.WormGear':
        """WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4955.WormGearModalAnalysisAtAStiffness]':
        """List[WormGearModalAnalysisAtAStiffness]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4955.WormGearModalAnalysisAtAStiffness]':
        """List[WormGearModalAnalysisAtAStiffness]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'WormGearCompoundModalAnalysisAtAStiffness._Cast_WormGearCompoundModalAnalysisAtAStiffness':
        return self._Cast_WormGearCompoundModalAnalysisAtAStiffness(self)
