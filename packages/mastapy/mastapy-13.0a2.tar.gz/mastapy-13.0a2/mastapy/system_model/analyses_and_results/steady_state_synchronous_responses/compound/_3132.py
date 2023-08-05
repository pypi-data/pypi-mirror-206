"""_3132.py

CouplingCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3001
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3193
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'CouplingCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingCompoundSteadyStateSynchronousResponse',)


class CouplingCompoundSteadyStateSynchronousResponse(_3193.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse):
    """CouplingCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_CouplingCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CouplingCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'CouplingCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3193.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3095
            
            return self._parent._cast(_3095.AbstractAssemblyCompoundSteadyStateSynchronousResponse)

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
        def clutch_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3116
            
            return self._parent._cast(_3116.ClutchCompoundSteadyStateSynchronousResponse)

        @property
        def concept_coupling_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3121
            
            return self._parent._cast(_3121.ConceptCouplingCompoundSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3175
            
            return self._parent._cast(_3175.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse)

        @property
        def spring_damper_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3197
            
            return self._parent._cast(_3197.SpringDamperCompoundSteadyStateSynchronousResponse)

        @property
        def torque_converter_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3212
            
            return self._parent._cast(_3212.TorqueConverterCompoundSteadyStateSynchronousResponse)

        @property
        def coupling_compound_steady_state_synchronous_response(self) -> 'CouplingCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_3001.CouplingSteadyStateSynchronousResponse]':
        """List[CouplingSteadyStateSynchronousResponse]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3001.CouplingSteadyStateSynchronousResponse]':
        """List[CouplingSteadyStateSynchronousResponse]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse':
        return self._Cast_CouplingCompoundSteadyStateSynchronousResponse(self)
