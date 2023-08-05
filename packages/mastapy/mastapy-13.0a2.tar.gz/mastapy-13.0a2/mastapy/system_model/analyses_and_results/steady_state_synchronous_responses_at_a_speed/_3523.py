"""_3523.py

CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
"""
from mastapy.system_model.connections_and_sockets import _2254
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3492
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed',)


class CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed(_3492.BeltConnectionSteadyStateSynchronousResponseAtASpeed):
    """CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def belt_connection_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3492.BeltConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3548
            
            return self._parent._cast(_3548.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3518
            
            return self._parent._cast(_3518.ConnectionSteadyStateSynchronousResponseAtASpeed)

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
        def cvt_belt_connection_steady_state_synchronous_response_at_a_speed(self) -> 'CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2254.CVTBeltConnection':
        """CVTBeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed(self)
