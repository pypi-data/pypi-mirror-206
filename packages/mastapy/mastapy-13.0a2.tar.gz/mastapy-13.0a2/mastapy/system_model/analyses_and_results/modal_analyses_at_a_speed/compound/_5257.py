"""_5257.py

CouplingHalfCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5127
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5295
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'CouplingHalfCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfCompoundModalAnalysisAtASpeed',)


class CouplingHalfCompoundModalAnalysisAtASpeed(_5295.MountableComponentCompoundModalAnalysisAtASpeed):
    """CouplingHalfCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_CouplingHalfCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CouplingHalfCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'CouplingHalfCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(self):
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
        def clutch_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5241
            
            return self._parent._cast(_5241.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5246
            
            return self._parent._cast(_5246.ConceptCouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5260
            
            return self._parent._cast(_5260.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5300
            
            return self._parent._cast(_5300.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def pulley_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5306
            
            return self._parent._cast(_5306.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5310
            
            return self._parent._cast(_5310.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5322
            
            return self._parent._cast(_5322.SpringDamperHalfCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5332
            
            return self._parent._cast(_5332.SynchroniserHalfCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5333
            
            return self._parent._cast(_5333.SynchroniserPartCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5334
            
            return self._parent._cast(_5334.SynchroniserSleeveCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5337
            
            return self._parent._cast(_5337.TorqueConverterPumpCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5338
            
            return self._parent._cast(_5338.TorqueConverterTurbineCompoundModalAnalysisAtASpeed)

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(self) -> 'CouplingHalfCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5127.CouplingHalfModalAnalysisAtASpeed]':
        """List[CouplingHalfModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5127.CouplingHalfModalAnalysisAtASpeed]':
        """List[CouplingHalfModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed':
        return self._Cast_CouplingHalfCompoundModalAnalysisAtASpeed(self)
