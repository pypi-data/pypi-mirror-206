"""_3649.py

ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3519
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3690
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'ConnectorCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorCompoundSteadyStateSynchronousResponseAtASpeed',)


class ConnectorCompoundSteadyStateSynchronousResponseAtASpeed(_3690.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed):
    """ConnectorCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConnectorCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'ConnectorCompoundSteadyStateSynchronousResponseAtASpeed'):
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
        def bearing_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3621
            
            return self._parent._cast(_3621.BearingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def oil_seal_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3691
            
            return self._parent._cast(_3691.OilSealCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3709
            
            return self._parent._cast(_3709.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def connector_compound_steady_state_synchronous_response_at_a_speed(self) -> 'ConnectorCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectorCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3519.ConnectorSteadyStateSynchronousResponseAtASpeed]':
        """List[ConnectorSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3519.ConnectorSteadyStateSynchronousResponseAtASpeed]':
        """List[ConnectorSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed(self)
