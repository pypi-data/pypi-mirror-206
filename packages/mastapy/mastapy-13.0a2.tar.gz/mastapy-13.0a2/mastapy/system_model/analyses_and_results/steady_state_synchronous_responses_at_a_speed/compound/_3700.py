"""_3700.py

PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.part_model import _2452
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3570
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3735
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed',)


class PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed(_3735.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed):
    """PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def virtual_component_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3735.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3690
            
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
        def power_load_compound_steady_state_synchronous_response_at_a_speed(self) -> 'PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2452.PowerLoad':
        """PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3570.PowerLoadSteadyStateSynchronousResponseAtASpeed]':
        """List[PowerLoadSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3570.PowerLoadSteadyStateSynchronousResponseAtASpeed]':
        """List[PowerLoadSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed(self)
