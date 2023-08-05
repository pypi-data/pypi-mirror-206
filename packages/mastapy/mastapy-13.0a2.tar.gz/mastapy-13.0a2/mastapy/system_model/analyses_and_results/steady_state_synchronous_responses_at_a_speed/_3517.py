"""_3517.py

ConicalGearSteadyStateSynchronousResponseAtASpeed
"""
from typing import List

from mastapy.system_model.part_model.gears import _2502
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'ConicalGearSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSteadyStateSynchronousResponseAtASpeed',)


class ConicalGearSteadyStateSynchronousResponseAtASpeed(_3543.GearSteadyStateSynchronousResponseAtASpeed):
    """ConicalGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConicalGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'ConicalGearSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def gear_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3543.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3560
            
            return self._parent._cast(_3560.MountableComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3508
            
            return self._parent._cast(_3508.ComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3562
            
            return self._parent._cast(_3562.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3489
            
            return self._parent._cast(_3489.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3496
            
            return self._parent._cast(_3496.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3497
            
            return self._parent._cast(_3497.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3498
            
            return self._parent._cast(_3498.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3501
            
            return self._parent._cast(_3501.BevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3547
            
            return self._parent._cast(_3547.HypoidGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3551
            
            return self._parent._cast(_3551.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3554
            
            return self._parent._cast(_3554.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3557
            
            return self._parent._cast(_3557.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3584
            
            return self._parent._cast(_3584.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3591
            
            return self._parent._cast(_3591.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3594
            
            return self._parent._cast(_3594.StraightBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3595
            
            return self._parent._cast(_3595.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3596
            
            return self._parent._cast(_3596.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3612
            
            return self._parent._cast(_3612.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(self) -> 'ConicalGearSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2502.ConicalGear':
        """ConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ConicalGearSteadyStateSynchronousResponseAtASpeed]':
        """List[ConicalGearSteadyStateSynchronousResponseAtASpeed]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_ConicalGearSteadyStateSynchronousResponseAtASpeed(self)
