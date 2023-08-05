"""_3317.py

RollingRingSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2575
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6911
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3262
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'RollingRingSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingSteadyStateSynchronousResponseOnAShaft',)


class RollingRingSteadyStateSynchronousResponseOnAShaft(_3262.CouplingHalfSteadyStateSynchronousResponseOnAShaft):
    """RollingRingSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_RollingRingSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting RollingRingSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'RollingRingSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3262.CouplingHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3301
            
            return self._parent._cast(_3301.MountableComponentSteadyStateSynchronousResponseOnAShaft)

        @property
        def component_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3249
            
            return self._parent._cast(_3249.ComponentSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3303
            
            return self._parent._cast(_3303.PartSteadyStateSynchronousResponseOnAShaft)

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
        def rolling_ring_steady_state_synchronous_response_on_a_shaft(self) -> 'RollingRingSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingRingSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2575.RollingRing':
        """RollingRing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6911.RollingRingLoadCase':
        """RollingRingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[RollingRingSteadyStateSynchronousResponseOnAShaft]':
        """List[RollingRingSteadyStateSynchronousResponseOnAShaft]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RollingRingSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_RollingRingSteadyStateSynchronousResponseOnAShaft(self)
