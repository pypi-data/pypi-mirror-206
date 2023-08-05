"""_3650.py

CouplingCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3522
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3711
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'CouplingCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingCompoundSteadyStateSynchronousResponseAtASpeed',)


class CouplingCompoundSteadyStateSynchronousResponseAtASpeed(_3711.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed):
    """CouplingCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_CouplingCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CouplingCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'CouplingCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3711.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3613
            
            return self._parent._cast(_3613.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

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
        def clutch_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3634
            
            return self._parent._cast(_3634.ClutchCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3639
            
            return self._parent._cast(_3639.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3693
            
            return self._parent._cast(_3693.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3715
            
            return self._parent._cast(_3715.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3730
            
            return self._parent._cast(_3730.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_compound_steady_state_synchronous_response_at_a_speed(self) -> 'CouplingCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_3522.CouplingSteadyStateSynchronousResponseAtASpeed]':
        """List[CouplingSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3522.CouplingSteadyStateSynchronousResponseAtASpeed]':
        """List[CouplingSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_CouplingCompoundSteadyStateSynchronousResponseAtASpeed(self)
