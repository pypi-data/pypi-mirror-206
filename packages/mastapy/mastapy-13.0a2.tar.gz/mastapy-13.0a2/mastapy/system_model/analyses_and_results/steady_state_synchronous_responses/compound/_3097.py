"""_3097.py

AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2963
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3120
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse',)


class AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse(_3120.ComponentCompoundSteadyStateSynchronousResponse):
    """AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3120.ComponentCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3174
            
            return self._parent._cast(_3174.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3096
            
            return self._parent._cast(_3096.AbstractShaftCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3140
            
            return self._parent._cast(_3140.CycloidalDiscCompoundSteadyStateSynchronousResponse)

        @property
        def fe_part_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3151
            
            return self._parent._cast(_3151.FEPartCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3190
            
            return self._parent._cast(_3190.ShaftCompoundSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response(self) -> 'AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_2963.AbstractShaftOrHousingSteadyStateSynchronousResponse]':
        """List[AbstractShaftOrHousingSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_2963.AbstractShaftOrHousingSteadyStateSynchronousResponse]':
        """List[AbstractShaftOrHousingSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse':
        return self._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse(self)
