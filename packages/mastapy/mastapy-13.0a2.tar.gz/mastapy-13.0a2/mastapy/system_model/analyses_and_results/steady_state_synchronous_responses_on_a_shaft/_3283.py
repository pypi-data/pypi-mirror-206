"""_3283.py

GearSetSteadyStateSynchronousResponseOnAShaft
"""
from mastapy.system_model.part_model.gears import _2511
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3322
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'GearSetSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetSteadyStateSynchronousResponseOnAShaft',)


class GearSetSteadyStateSynchronousResponseOnAShaft(_3322.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft):
    """GearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_GearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting GearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'GearSetSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3322.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3224
            
            return self._parent._cast(_3224.AbstractAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def part_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3303
            
            return self._parent._cast(_3303.PartSteadyStateSynchronousResponseOnAShaft)

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
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3229
            
            return self._parent._cast(_3229.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3236
            
            return self._parent._cast(_3236.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3241
            
            return self._parent._cast(_3241.BevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3254
            
            return self._parent._cast(_3254.ConceptGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3257
            
            return self._parent._cast(_3257.ConicalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3272
            
            return self._parent._cast(_3272.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3278
            
            return self._parent._cast(_3278.FaceGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3287
            
            return self._parent._cast(_3287.HypoidGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3291
            
            return self._parent._cast(_3291.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3294
            
            return self._parent._cast(_3294.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3297
            
            return self._parent._cast(_3297.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3308
            
            return self._parent._cast(_3308.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3324
            
            return self._parent._cast(_3324.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3331
            
            return self._parent._cast(_3331.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3334
            
            return self._parent._cast(_3334.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3349
            
            return self._parent._cast(_3349.WormGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3352
            
            return self._parent._cast(_3352.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(self) -> 'GearSetSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2511.GearSet':
        """GearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearSetSteadyStateSynchronousResponseOnAShaft._Cast_GearSetSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_GearSetSteadyStateSynchronousResponseOnAShaft(self)
