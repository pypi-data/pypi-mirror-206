"""_3693.py

PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2567
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3565
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3650
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed',)


class PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed(_3650.CouplingCompoundSteadyStateSynchronousResponseAtASpeed):
    """PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def coupling_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3650.CouplingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3711
            
            return self._parent._cast(_3711.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3613
            
            return self._parent._cast(_3613.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3692
            
            return self._parent._cast(_3692.PartCompoundSteadyStateSynchronousResponseAtASpeed)

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
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_at_a_speed(self) -> 'PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
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
    def assembly_analysis_cases_ready(self) -> 'List[_3565.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed]':
        """List[PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3565.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed]':
        """List[PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed(self)
