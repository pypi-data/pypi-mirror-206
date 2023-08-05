"""_3572.py

RingPinsSteadyStateSynchronousResponseAtASpeed
"""
from mastapy.system_model.part_model.cycloidal import _2549
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6907
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3560
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'RingPinsSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsSteadyStateSynchronousResponseAtASpeed',)


class RingPinsSteadyStateSynchronousResponseAtASpeed(_3560.MountableComponentSteadyStateSynchronousResponseAtASpeed):
    """RingPinsSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _RING_PINS_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_RingPinsSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting RingPinsSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'RingPinsSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3560.MountableComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3508
            
            return self._parent._cast(_3508.ComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3562
            
            return self._parent._cast(_3562.PartSteadyStateSynchronousResponseAtASpeed)

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
        def ring_pins_steady_state_synchronous_response_at_a_speed(self) -> 'RingPinsSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingPinsSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2549.RingPins':
        """RingPins: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6907.RingPinsLoadCase':
        """RingPinsLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RingPinsSteadyStateSynchronousResponseAtASpeed._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_RingPinsSteadyStateSynchronousResponseAtASpeed(self)
