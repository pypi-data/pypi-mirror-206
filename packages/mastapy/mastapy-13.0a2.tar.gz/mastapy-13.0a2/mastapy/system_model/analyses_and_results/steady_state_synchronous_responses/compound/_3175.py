"""_3175.py

PartToPartShearCouplingCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2567
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3045
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3132
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'PartToPartShearCouplingCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingCompoundSteadyStateSynchronousResponse',)


class PartToPartShearCouplingCompoundSteadyStateSynchronousResponse(_3132.CouplingCompoundSteadyStateSynchronousResponse):
    """PartToPartShearCouplingCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting PartToPartShearCouplingCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'PartToPartShearCouplingCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def coupling_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3132.CouplingCompoundSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3193
            
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
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(self) -> 'PartToPartShearCouplingCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2567.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2567.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3045.PartToPartShearCouplingSteadyStateSynchronousResponse]':
        """List[PartToPartShearCouplingSteadyStateSynchronousResponse]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3045.PartToPartShearCouplingSteadyStateSynchronousResponse]':
        """List[PartToPartShearCouplingSteadyStateSynchronousResponse]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartToPartShearCouplingCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponse':
        return self._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponse(self)
