"""_3652.py

CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3521
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3690
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed',)


class CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(_3690.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed):
    """CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3690.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3638
            
            return self._parent._cast(_3638.ComponentCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3692
            
            return self._parent._cast(_3692.PartCompoundSteadyStateSynchronousResponseAtASpeed)

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
        def clutch_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3636
            
            return self._parent._cast(_3636.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3641
            
            return self._parent._cast(_3641.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3655
            
            return self._parent._cast(_3655.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3695
            
            return self._parent._cast(_3695.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3701
            
            return self._parent._cast(_3701.PulleyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3705
            
            return self._parent._cast(_3705.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3717
            
            return self._parent._cast(_3717.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3727
            
            return self._parent._cast(_3727.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3728
            
            return self._parent._cast(_3728.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3729
            
            return self._parent._cast(_3729.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3732
            
            return self._parent._cast(_3732.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3733
            
            return self._parent._cast(_3733.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(self) -> 'CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3521.CouplingHalfSteadyStateSynchronousResponseAtASpeed]':
        """List[CouplingHalfSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3521.CouplingHalfSteadyStateSynchronousResponseAtASpeed]':
        """List[CouplingHalfSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(self)
