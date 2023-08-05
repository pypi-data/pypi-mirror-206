"""_3372.py

BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3241
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3360
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft',)


class BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft(_3360.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft):
    """BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3360.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3388
            
            return self._parent._cast(_3388.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3414
            
            return self._parent._cast(_3414.GearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3452
            
            return self._parent._cast(_3452.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3354
            
            return self._parent._cast(_3354.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3367
            
            return self._parent._cast(_3367.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3455
            
            return self._parent._cast(_3455.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3461
            
            return self._parent._cast(_3461.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3464
            
            return self._parent._cast(_3464.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3482
            
            return self._parent._cast(_3482.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_3241.BevelGearSetSteadyStateSynchronousResponseOnAShaft]':
        """List[BevelGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3241.BevelGearSetSteadyStateSynchronousResponseOnAShaft]':
        """List[BevelGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft(self)
