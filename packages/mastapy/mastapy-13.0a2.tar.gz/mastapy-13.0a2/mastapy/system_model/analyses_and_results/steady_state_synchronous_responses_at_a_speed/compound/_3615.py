"""_3615.py

AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3484
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3638
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed',)


class AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed(_3638.ComponentCompoundSteadyStateSynchronousResponseAtASpeed):
    """AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(self):
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
        def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3614
            
            return self._parent._cast(_3614.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3658
            
            return self._parent._cast(_3658.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def fe_part_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3669
            
            return self._parent._cast(_3669.FEPartCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3708
            
            return self._parent._cast(_3708.ShaftCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(self) -> 'AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3484.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed]':
        """List[AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3484.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed]':
        """List[AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed(self)
