"""_3307.py

PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft
"""
from mastapy.system_model.connections_and_sockets import _2268
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6896
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3321
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft',)


class PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft(_3321.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft):
    """PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3321.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3227
            
            return self._parent._cast(_3227.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3259
            
            return self._parent._cast(_3259.ConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7503
            
            return self._parent._cast(_7503.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7500
            
            return self._parent._cast(_7500.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2628
            
            return self._parent._cast(_2628.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def planetary_connection_steady_state_synchronous_response_on_a_shaft(self) -> 'PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2268.PlanetaryConnection':
        """PlanetaryConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6896.PlanetaryConnectionLoadCase':
        """PlanetaryConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft(self)
