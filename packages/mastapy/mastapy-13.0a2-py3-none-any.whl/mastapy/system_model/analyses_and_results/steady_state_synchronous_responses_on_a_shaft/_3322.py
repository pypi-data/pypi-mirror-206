"""_3322.py

SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
"""
from mastapy.system_model.part_model import _2456
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft',)


class SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft(_3224.AbstractAssemblySteadyStateSynchronousResponseOnAShaft):
    """SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(self):
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
        def belt_drive_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3234
            
            return self._parent._cast(_3234.BeltDriveSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3236
            
            return self._parent._cast(_3236.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3241
            
            return self._parent._cast(_3241.BevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def bolted_joint_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3243
            
            return self._parent._cast(_3243.BoltedJointSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3247
            
            return self._parent._cast(_3247.ClutchSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3252
            
            return self._parent._cast(_3252.ConceptCouplingSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3254
            
            return self._parent._cast(_3254.ConceptGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3257
            
            return self._parent._cast(_3257.ConicalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3263
            
            return self._parent._cast(_3263.CouplingSteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3266
            
            return self._parent._cast(_3266.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3267
            
            return self._parent._cast(_3267.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3272
            
            return self._parent._cast(_3272.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3278
            
            return self._parent._cast(_3278.FaceGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3281
            
            return self._parent._cast(_3281.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3283
            
            return self._parent._cast(_3283.GearSetSteadyStateSynchronousResponseOnAShaft)

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
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3306
            
            return self._parent._cast(_3306.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft)

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3308
            
            return self._parent._cast(_3308.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3315
            
            return self._parent._cast(_3315.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3324
            
            return self._parent._cast(_3324.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3328
            
            return self._parent._cast(_3328.SpringDamperSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3331
            
            return self._parent._cast(_3331.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3334
            
            return self._parent._cast(_3334.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3341
            
            return self._parent._cast(_3341.SynchroniserSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3344
            
            return self._parent._cast(_3344.TorqueConverterSteadyStateSynchronousResponseOnAShaft)

        @property
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3349
            
            return self._parent._cast(_3349.WormGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3352
            
            return self._parent._cast(_3352.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(self) -> 'SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2456.SpecialisedAssembly':
        """SpecialisedAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft':
        return self._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft(self)
