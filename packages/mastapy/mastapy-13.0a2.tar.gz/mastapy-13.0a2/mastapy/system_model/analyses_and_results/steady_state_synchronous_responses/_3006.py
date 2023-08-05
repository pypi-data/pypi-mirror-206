"""_3006.py

CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse
"""
from mastapy.system_model.connections_and_sockets.cycloidal import _2316
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2986
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse',)


class CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse(_2986.CoaxialConnectionSteadyStateSynchronousResponse):
    """CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def coaxial_connection_steady_state_synchronous_response(self):
            return self._parent._cast(_2986.CoaxialConnectionSteadyStateSynchronousResponse)

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3060
            
            return self._parent._cast(_3060.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2965
            
            return self._parent._cast(_2965.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse)

        @property
        def connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2997
            
            return self._parent._cast(_2997.ConnectionSteadyStateSynchronousResponse)

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
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(self) -> 'CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2316.CycloidalDiscCentralBearingConnection':
        """CycloidalDiscCentralBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse':
        return self._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse(self)
