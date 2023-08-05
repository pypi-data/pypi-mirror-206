"""_3056.py

RollingRingSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2575
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6911
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3000
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'RollingRingSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingSteadyStateSynchronousResponse',)


class RollingRingSteadyStateSynchronousResponse(_3000.CouplingHalfSteadyStateSynchronousResponse):
    """RollingRingSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_RollingRingSteadyStateSynchronousResponse:
        """Special nested class for casting RollingRingSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'RollingRingSteadyStateSynchronousResponse'):
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
        def rolling_ring_steady_state_synchronous_response(self) -> 'RollingRingSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingRingSteadyStateSynchronousResponse.TYPE'):
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
    def planetaries(self) -> 'List[RollingRingSteadyStateSynchronousResponse]':
        """List[RollingRingSteadyStateSynchronousResponse]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse':
        return self._Cast_RollingRingSteadyStateSynchronousResponse(self)
