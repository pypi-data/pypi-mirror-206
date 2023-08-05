"""_5072.py

StraightBevelSunGearCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4943
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5065
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'StraightBevelSunGearCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelSunGearCompoundModalAnalysisAtAStiffness',)


class StraightBevelSunGearCompoundModalAnalysisAtAStiffness(_5065.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness):
    """StraightBevelSunGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting StraightBevelSunGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'StraightBevelSunGearCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_5065.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4976
            
            return self._parent._cast(_4976.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4964
            
            return self._parent._cast(_4964.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness)

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4992
            
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
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(self) -> 'StraightBevelSunGearCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelSunGearCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_4943.StraightBevelSunGearModalAnalysisAtAStiffness]':
        """List[StraightBevelSunGearModalAnalysisAtAStiffness]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4943.StraightBevelSunGearModalAnalysisAtAStiffness]':
        """List[StraightBevelSunGearModalAnalysisAtAStiffness]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness':
        return self._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness(self)
