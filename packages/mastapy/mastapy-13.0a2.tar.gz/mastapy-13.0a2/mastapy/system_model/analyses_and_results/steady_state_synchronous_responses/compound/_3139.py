"""_3139.py

CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3006
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3119
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse',)


class CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse(_3119.CoaxialConnectionCompoundSteadyStateSynchronousResponse):
    """CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def coaxial_connection_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3119.CoaxialConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3192
            
            return self._parent._cast(_3192.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3098
            
            return self._parent._cast(_3098.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3130
            
            return self._parent._cast(_3130.ConnectionCompoundSteadyStateSynchronousResponse)

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
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(self) -> 'CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3006.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse]':
        """List[CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3006.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse]':
        """List[CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse':
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse(self)
