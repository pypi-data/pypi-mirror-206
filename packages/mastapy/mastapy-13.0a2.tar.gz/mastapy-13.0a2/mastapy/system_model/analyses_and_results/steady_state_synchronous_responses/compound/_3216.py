"""_3216.py

UnbalancedMassCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.part_model import _2457
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3087
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3217
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'UnbalancedMassCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassCompoundSteadyStateSynchronousResponse',)


class UnbalancedMassCompoundSteadyStateSynchronousResponse(_3217.VirtualComponentCompoundSteadyStateSynchronousResponse):
    """UnbalancedMassCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting UnbalancedMassCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'UnbalancedMassCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def virtual_component_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3217.VirtualComponentCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3172
            
            return self._parent._cast(_3172.MountableComponentCompoundSteadyStateSynchronousResponse)

        @property
        def component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3120
            
            return self._parent._cast(_3120.ComponentCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3174
            
            return self._parent._cast(_3174.PartCompoundSteadyStateSynchronousResponse)

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
        def unbalanced_mass_compound_steady_state_synchronous_response(self) -> 'UnbalancedMassCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'UnbalancedMassCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2457.UnbalancedMass':
        """UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3087.UnbalancedMassSteadyStateSynchronousResponse]':
        """List[UnbalancedMassSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3087.UnbalancedMassSteadyStateSynchronousResponse]':
        """List[UnbalancedMassSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'UnbalancedMassCompoundSteadyStateSynchronousResponse._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse':
        return self._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse(self)
