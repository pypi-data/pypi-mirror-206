"""_3214.py

TorqueConverterPumpCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2587
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3084
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3134
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'TorqueConverterPumpCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpCompoundSteadyStateSynchronousResponse',)


class TorqueConverterPumpCompoundSteadyStateSynchronousResponse(_3134.CouplingHalfCompoundSteadyStateSynchronousResponse):
    """TorqueConverterPumpCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting TorqueConverterPumpCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'TorqueConverterPumpCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3134.CouplingHalfCompoundSteadyStateSynchronousResponse)

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
        def torque_converter_pump_compound_steady_state_synchronous_response(self) -> 'TorqueConverterPumpCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2587.TorqueConverterPump':
        """TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3084.TorqueConverterPumpSteadyStateSynchronousResponse]':
        """List[TorqueConverterPumpSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3084.TorqueConverterPumpSteadyStateSynchronousResponse]':
        """List[TorqueConverterPumpSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'TorqueConverterPumpCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse':
        return self._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse(self)
