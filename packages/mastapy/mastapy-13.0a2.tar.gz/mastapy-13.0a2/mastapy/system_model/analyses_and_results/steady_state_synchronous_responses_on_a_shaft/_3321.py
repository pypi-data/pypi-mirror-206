"""_3321.py

ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
"""
from mastapy.system_model.connections_and_sockets import _2276
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft',)


class ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft(_3227.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft):
    """ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(self):
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
        def coaxial_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3248
            
            return self._parent._cast(_3248.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3268
            
            return self._parent._cast(_3268.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def planetary_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3307
            
            return self._parent._cast(_3307.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(self) -> 'ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2276.ShaftToMountableComponentConnection':
        """ShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft(self)
