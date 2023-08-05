"""_2999.py

CouplingConnectionSteadyStateSynchronousResponse
"""
from mastapy.system_model.connections_and_sockets.couplings import _2327
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3028
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'CouplingConnectionSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionSteadyStateSynchronousResponse',)


class CouplingConnectionSteadyStateSynchronousResponse(_3028.InterMountableComponentConnectionSteadyStateSynchronousResponse):
    """CouplingConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_CouplingConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting CouplingConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'CouplingConnectionSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(self):
            return self._parent._cast(_3028.InterMountableComponentConnectionSteadyStateSynchronousResponse)

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
        def clutch_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2983
            
            return self._parent._cast(_2983.ClutchConnectionSteadyStateSynchronousResponse)

        @property
        def concept_coupling_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2988
            
            return self._parent._cast(_2988.ConceptCouplingConnectionSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3043
            
            return self._parent._cast(_3043.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse)

        @property
        def spring_damper_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3065
            
            return self._parent._cast(_3065.SpringDamperConnectionSteadyStateSynchronousResponse)

        @property
        def torque_converter_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3083
            
            return self._parent._cast(_3083.TorqueConverterConnectionSteadyStateSynchronousResponse)

        @property
        def coupling_connection_steady_state_synchronous_response(self) -> 'CouplingConnectionSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2327.CouplingConnection':
        """CouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingConnectionSteadyStateSynchronousResponse._Cast_CouplingConnectionSteadyStateSynchronousResponse':
        return self._Cast_CouplingConnectionSteadyStateSynchronousResponse(self)
