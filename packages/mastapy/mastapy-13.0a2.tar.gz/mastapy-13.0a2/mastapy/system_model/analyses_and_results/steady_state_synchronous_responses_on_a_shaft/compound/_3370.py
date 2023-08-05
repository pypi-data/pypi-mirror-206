"""_3370.py

BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3242
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'BevelGearCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearCompoundSteadyStateSynchronousResponseOnAShaft',)


class BevelGearCompoundSteadyStateSynchronousResponseOnAShaft(_3358.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft):
    """BevelGearCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_BevelGearCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BevelGearCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'BevelGearCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3358.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3386
            
            return self._parent._cast(_3386.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3412
            
            return self._parent._cast(_3412.GearCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3365
            
            return self._parent._cast(_3365.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3368
            
            return self._parent._cast(_3368.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3369
            
            return self._parent._cast(_3369.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3453
            
            return self._parent._cast(_3453.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3459
            
            return self._parent._cast(_3459.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3462
            
            return self._parent._cast(_3462.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3465
            
            return self._parent._cast(_3465.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3466
            
            return self._parent._cast(_3466.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3480
            
            return self._parent._cast(_3480.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'BevelGearCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3242.BevelGearSteadyStateSynchronousResponseOnAShaft]':
        """List[BevelGearSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3242.BevelGearSteadyStateSynchronousResponseOnAShaft]':
        """List[BevelGearSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_BevelGearCompoundSteadyStateSynchronousResponseOnAShaft(self)
