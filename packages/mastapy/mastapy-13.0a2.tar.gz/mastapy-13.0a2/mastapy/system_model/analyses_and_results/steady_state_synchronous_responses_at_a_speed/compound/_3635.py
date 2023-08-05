"""_3635.py

ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2323
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3504
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3651
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed',)


class ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed(_3651.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed):
    """ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def coupling_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3651.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3678
            
            return self._parent._cast(_3678.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

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
        def clutch_connection_compound_steady_state_synchronous_response_at_a_speed(self) -> 'ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2323.ClutchConnection':
        """ClutchConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2323.ClutchConnection':
        """ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3504.ClutchConnectionSteadyStateSynchronousResponseAtASpeed]':
        """List[ClutchConnectionSteadyStateSynchronousResponseAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3504.ClutchConnectionSteadyStateSynchronousResponseAtASpeed]':
        """List[ClutchConnectionSteadyStateSynchronousResponseAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed(self)
