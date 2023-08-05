"""_3376.py

ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2323
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3245
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3392
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft',)


class ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft(_3392.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft):
    """ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3392.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3419
            
            return self._parent._cast(_3419.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3389
            
            return self._parent._cast(_3389.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def clutch_connection_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
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
    def connection_analysis_cases_ready(self) -> 'List[_3245.ClutchConnectionSteadyStateSynchronousResponseOnAShaft]':
        """List[ClutchConnectionSteadyStateSynchronousResponseOnAShaft]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3245.ClutchConnectionSteadyStateSynchronousResponseOnAShaft]':
        """List[ClutchConnectionSteadyStateSynchronousResponseOnAShaft]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft(self)
