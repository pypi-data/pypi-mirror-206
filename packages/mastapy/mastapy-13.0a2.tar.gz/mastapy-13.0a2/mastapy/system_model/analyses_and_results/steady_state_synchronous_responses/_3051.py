"""_3051.py

PulleySteadyStateSynchronousResponse
"""
from mastapy.system_model.part_model.couplings import _2569
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6904
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3000
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'PulleySteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleySteadyStateSynchronousResponse',)


class PulleySteadyStateSynchronousResponse(_3000.CouplingHalfSteadyStateSynchronousResponse):
    """PulleySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_PulleySteadyStateSynchronousResponse:
        """Special nested class for casting PulleySteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'PulleySteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response(self):
            return self._parent._cast(_3000.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3040
            
            return self._parent._cast(_3040.MountableComponentSteadyStateSynchronousResponse)

        @property
        def component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2987
            
            return self._parent._cast(_2987.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3042
            
            return self._parent._cast(_3042.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def cvt_pulley_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3003
            
            return self._parent._cast(_3003.CVTPulleySteadyStateSynchronousResponse)

        @property
        def pulley_steady_state_synchronous_response(self) -> 'PulleySteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PulleySteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2569.Pulley':
        """Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6904.PulleyLoadCase':
        """PulleyLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PulleySteadyStateSynchronousResponse._Cast_PulleySteadyStateSynchronousResponse':
        return self._Cast_PulleySteadyStateSynchronousResponse(self)
