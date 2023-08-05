"""_3398.py

CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3268
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3378
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft',)


class CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft(_3378.CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft):
    """CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3378.CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3451
            
            return self._parent._cast(_3451.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3357
            
            return self._parent._cast(_3357.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3268.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft]':
        """List[CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3268.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft]':
        """List[CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft(self)
