"""_3412.py

GearCompoundSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3284
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3431
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'GearCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundSteadyStateSynchronousResponseOnAShaft',)


class GearCompoundSteadyStateSynchronousResponseOnAShaft(_3431.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft):
    """GearCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_GearCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting GearCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'GearCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(self):
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
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3358
            
            return self._parent._cast(_3358.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3370
            
            return self._parent._cast(_3370.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3383
            
            return self._parent._cast(_3383.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3386
            
            return self._parent._cast(_3386.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3401
            
            return self._parent._cast(_3401.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3404
            
            return self._parent._cast(_3404.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3407
            
            return self._parent._cast(_3407.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3416
            
            return self._parent._cast(_3416.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3420
            
            return self._parent._cast(_3420.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3423
            
            return self._parent._cast(_3423.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3426
            
            return self._parent._cast(_3426.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def worm_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3477
            
            return self._parent._cast(_3477.WormGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3480
            
            return self._parent._cast(_3480.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'GearCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3284.GearSteadyStateSynchronousResponseOnAShaft]':
        """List[GearSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3284.GearSteadyStateSynchronousResponseOnAShaft]':
        """List[GearSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_GearCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_GearCompoundSteadyStateSynchronousResponseOnAShaft(self)
