"""_3436.py

PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2568
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3305
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3393
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft',)


class PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft(_3393.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft):
    """PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3393.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3431
            
            return self._parent._cast(_3431.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3379
            
            return self._parent._cast(_3379.ComponentCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3433
            
            return self._parent._cast(_3433.PartCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2568.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3305.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft]':
        """List[PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3305.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft]':
        """List[PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft(self)
