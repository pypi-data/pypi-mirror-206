"""_3563.py

PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed
"""
from mastapy.system_model.connections_and_sockets.couplings import _2329
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6893
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3520
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed',)


class PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed(_3520.CouplingConnectionSteadyStateSynchronousResponseAtASpeed):
    """PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3520.CouplingConnectionSteadyStateSynchronousResponseAtASpeed)

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
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_at_a_speed(self) -> 'PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2329.PartToPartShearCouplingConnection':
        """PartToPartShearCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6893.PartToPartShearCouplingConnectionLoadCase':
        """PartToPartShearCouplingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed(self)
