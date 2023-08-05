"""_3309.py

PlanetCarrierSteadyStateSynchronousResponseOnAShaft
"""
from mastapy.system_model.part_model import _2449
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6899
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'PlanetCarrierSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierSteadyStateSynchronousResponseOnAShaft',)


class PlanetCarrierSteadyStateSynchronousResponseOnAShaft(_3301.MountableComponentSteadyStateSynchronousResponseOnAShaft):
    """PlanetCarrierSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PlanetCarrierSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'PlanetCarrierSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(self):
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
        def planet_carrier_steady_state_synchronous_response_on_a_shaft(self) -> 'PlanetCarrierSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetCarrierSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2449.PlanetCarrier':
        """PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6899.PlanetCarrierLoadCase':
        """PlanetCarrierLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PlanetCarrierSteadyStateSynchronousResponseOnAShaft._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_PlanetCarrierSteadyStateSynchronousResponseOnAShaft(self)
