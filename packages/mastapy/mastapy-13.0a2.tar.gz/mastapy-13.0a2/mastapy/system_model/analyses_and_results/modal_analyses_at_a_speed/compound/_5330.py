"""_5330.py

StraightBevelSunGearCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5201
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5323
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'StraightBevelSunGearCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelSunGearCompoundModalAnalysisAtASpeed',)


class StraightBevelSunGearCompoundModalAnalysisAtASpeed(_5323.StraightBevelDiffGearCompoundModalAnalysisAtASpeed):
    """StraightBevelSunGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed:
        """Special nested class for casting StraightBevelSunGearCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'StraightBevelSunGearCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5323.StraightBevelDiffGearCompoundModalAnalysisAtASpeed)

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5234
            
            return self._parent._cast(_5234.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5222
            
            return self._parent._cast(_5222.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5250
            
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
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(self) -> 'StraightBevelSunGearCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelSunGearCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_5201.StraightBevelSunGearModalAnalysisAtASpeed]':
        """List[StraightBevelSunGearModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5201.StraightBevelSunGearModalAnalysisAtASpeed]':
        """List[StraightBevelSunGearModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelSunGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed':
        return self._Cast_StraightBevelSunGearCompoundModalAnalysisAtASpeed(self)
