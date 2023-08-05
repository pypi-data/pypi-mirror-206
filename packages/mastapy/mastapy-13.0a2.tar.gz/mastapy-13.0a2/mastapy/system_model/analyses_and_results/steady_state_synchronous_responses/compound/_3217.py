"""_3217.py

VirtualComponentCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3088
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3172
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'VirtualComponentCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentCompoundSteadyStateSynchronousResponse',)


class VirtualComponentCompoundSteadyStateSynchronousResponse(_3172.MountableComponentCompoundSteadyStateSynchronousResponse):
    """VirtualComponentCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_VirtualComponentCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting VirtualComponentCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'VirtualComponentCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response(self):
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
        def mass_disc_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3170
            
            return self._parent._cast(_3170.MassDiscCompoundSteadyStateSynchronousResponse)

        @property
        def measurement_component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3171
            
            return self._parent._cast(_3171.MeasurementComponentCompoundSteadyStateSynchronousResponse)

        @property
        def point_load_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3181
            
            return self._parent._cast(_3181.PointLoadCompoundSteadyStateSynchronousResponse)

        @property
        def power_load_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3182
            
            return self._parent._cast(_3182.PowerLoadCompoundSteadyStateSynchronousResponse)

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3216
            
            return self._parent._cast(_3216.UnbalancedMassCompoundSteadyStateSynchronousResponse)

        @property
        def virtual_component_compound_steady_state_synchronous_response(self) -> 'VirtualComponentCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3088.VirtualComponentSteadyStateSynchronousResponse]':
        """List[VirtualComponentSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3088.VirtualComponentSteadyStateSynchronousResponse]':
        """List[VirtualComponentSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse':
        return self._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse(self)
