"""_3647.py

ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3516
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3673
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed',)


class ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed(_3673.GearSetCompoundSteadyStateSynchronousResponseAtASpeed):
    """ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3673.GearSetCompoundSteadyStateSynchronousResponseAtASpeed)

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
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3619
            
            return self._parent._cast(_3619.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3626
            
            return self._parent._cast(_3626.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3631
            
            return self._parent._cast(_3631.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3677
            
            return self._parent._cast(_3677.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3681
            
            return self._parent._cast(_3681.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3684
            
            return self._parent._cast(_3684.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3687
            
            return self._parent._cast(_3687.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3714
            
            return self._parent._cast(_3714.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3720
            
            return self._parent._cast(_3720.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3723
            
            return self._parent._cast(_3723.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3741
            
            return self._parent._cast(_3741.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(self) -> 'ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_3516.ConicalGearSetSteadyStateSynchronousResponseAtASpeed]':
        """List[ConicalGearSetSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3516.ConicalGearSetSteadyStateSynchronousResponseAtASpeed]':
        """List[ConicalGearSetSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed(self)
