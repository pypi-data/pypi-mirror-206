"""_3664.py

DatumCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.part_model import _2428
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3534
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3638
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'DatumCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumCompoundSteadyStateSynchronousResponseAtASpeed',)


class DatumCompoundSteadyStateSynchronousResponseAtASpeed(_3638.ComponentCompoundSteadyStateSynchronousResponseAtASpeed):
    """DatumCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_DatumCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting DatumCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'DatumCompoundSteadyStateSynchronousResponseAtASpeed'):
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
        def datum_compound_steady_state_synchronous_response_at_a_speed(self) -> 'DatumCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DatumCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2428.Datum':
        """Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3534.DatumSteadyStateSynchronousResponseAtASpeed]':
        """List[DatumSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3534.DatumSteadyStateSynchronousResponseAtASpeed]':
        """List[DatumSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'DatumCompoundSteadyStateSynchronousResponseAtASpeed._Cast_DatumCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_DatumCompoundSteadyStateSynchronousResponseAtASpeed(self)
