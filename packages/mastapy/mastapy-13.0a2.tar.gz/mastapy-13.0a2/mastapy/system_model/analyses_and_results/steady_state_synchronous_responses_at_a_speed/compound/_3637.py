"""_3637.py

CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.connections_and_sockets import _2250
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3507
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3710
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed',)


class CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed(_3710.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed):
    """CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3710.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3616
            
            return self._parent._cast(_3616.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3648
            
            return self._parent._cast(_3648.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3657
            
            return self._parent._cast(_3657.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_at_a_speed(self) -> 'CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2250.CoaxialConnection':
        """CoaxialConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2250.CoaxialConnection':
        """CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3507.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed]':
        """List[CoaxialConnectionSteadyStateSynchronousResponseAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3507.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed]':
        """List[CoaxialConnectionSteadyStateSynchronousResponseAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed(self)
