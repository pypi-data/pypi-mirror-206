"""_3562.py

PartSteadyStateSynchronousResponseAtASpeed
"""
from mastapy.system_model.part_model import _2448
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3588
from mastapy.system_model.analyses_and_results.analysis_cases import _7510
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'PartSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('PartSteadyStateSynchronousResponseAtASpeed',)


class PartSteadyStateSynchronousResponseAtASpeed(_7510.PartStaticLoadAnalysisCase):
    """PartSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_PartSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PartSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'PartSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def part_static_load_analysis_case(self):
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
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3483
            
            return self._parent._cast(_3483.AbstractAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3484
            
            return self._parent._cast(_3484.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3485
            
            return self._parent._cast(_3485.AbstractShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3488
            
            return self._parent._cast(_3488.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3489
            
            return self._parent._cast(_3489.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3490
            
            return self._parent._cast(_3490.AssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3491
            
            return self._parent._cast(_3491.BearingSteadyStateSynchronousResponseAtASpeed)

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3493
            
            return self._parent._cast(_3493.BeltDriveSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3495
            
            return self._parent._cast(_3495.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed)

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
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3500
            
            return self._parent._cast(_3500.BevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3501
            
            return self._parent._cast(_3501.BevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def bolted_joint_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3502
            
            return self._parent._cast(_3502.BoltedJointSteadyStateSynchronousResponseAtASpeed)

        @property
        def bolt_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3503
            
            return self._parent._cast(_3503.BoltSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3505
            
            return self._parent._cast(_3505.ClutchHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3506
            
            return self._parent._cast(_3506.ClutchSteadyStateSynchronousResponseAtASpeed)

        @property
        def component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3508
            
            return self._parent._cast(_3508.ComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3510
            
            return self._parent._cast(_3510.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3511
            
            return self._parent._cast(_3511.ConceptCouplingSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3513
            
            return self._parent._cast(_3513.ConceptGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3514
            
            return self._parent._cast(_3514.ConceptGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3516
            
            return self._parent._cast(_3516.ConicalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3517
            
            return self._parent._cast(_3517.ConicalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def connector_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3519
            
            return self._parent._cast(_3519.ConnectorSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3521
            
            return self._parent._cast(_3521.CouplingHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3522
            
            return self._parent._cast(_3522.CouplingSteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3524
            
            return self._parent._cast(_3524.CVTPulleySteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3525
            
            return self._parent._cast(_3525.CVTSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3526
            
            return self._parent._cast(_3526.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3529
            
            return self._parent._cast(_3529.CycloidalDiscSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3531
            
            return self._parent._cast(_3531.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3532
            
            return self._parent._cast(_3532.CylindricalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3533
            
            return self._parent._cast(_3533.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def datum_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3534
            
            return self._parent._cast(_3534.DatumSteadyStateSynchronousResponseAtASpeed)

        @property
        def external_cad_model_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3535
            
            return self._parent._cast(_3535.ExternalCADModelSteadyStateSynchronousResponseAtASpeed)

        @property
        def face_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3537
            
            return self._parent._cast(_3537.FaceGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3538
            
            return self._parent._cast(_3538.FaceGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def fe_part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3539
            
            return self._parent._cast(_3539.FEPartSteadyStateSynchronousResponseAtASpeed)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3540
            
            return self._parent._cast(_3540.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3542
            
            return self._parent._cast(_3542.GearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3543
            
            return self._parent._cast(_3543.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def guide_dxf_model_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3544
            
            return self._parent._cast(_3544.GuideDxfModelSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3546
            
            return self._parent._cast(_3546.HypoidGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3547
            
            return self._parent._cast(_3547.HypoidGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3550
            
            return self._parent._cast(_3550.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3551
            
            return self._parent._cast(_3551.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3553
            
            return self._parent._cast(_3553.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3554
            
            return self._parent._cast(_3554.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3556
            
            return self._parent._cast(_3556.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3557
            
            return self._parent._cast(_3557.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3558
            
            return self._parent._cast(_3558.MassDiscSteadyStateSynchronousResponseAtASpeed)

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3559
            
            return self._parent._cast(_3559.MeasurementComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3560
            
            return self._parent._cast(_3560.MountableComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3561
            
            return self._parent._cast(_3561.OilSealSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3564
            
            return self._parent._cast(_3564.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3565
            
            return self._parent._cast(_3565.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed)

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3567
            
            return self._parent._cast(_3567.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3568
            
            return self._parent._cast(_3568.PlanetCarrierSteadyStateSynchronousResponseAtASpeed)

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3569
            
            return self._parent._cast(_3569.PointLoadSteadyStateSynchronousResponseAtASpeed)

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3570
            
            return self._parent._cast(_3570.PowerLoadSteadyStateSynchronousResponseAtASpeed)

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3571
            
            return self._parent._cast(_3571.PulleySteadyStateSynchronousResponseAtASpeed)

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3572
            
            return self._parent._cast(_3572.RingPinsSteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3574
            
            return self._parent._cast(_3574.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3576
            
            return self._parent._cast(_3576.RollingRingSteadyStateSynchronousResponseAtASpeed)

        @property
        def root_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3577
            
            return self._parent._cast(_3577.RootAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3578
            
            return self._parent._cast(_3578.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3579
            
            return self._parent._cast(_3579.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3581
            
            return self._parent._cast(_3581.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3583
            
            return self._parent._cast(_3583.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3584
            
            return self._parent._cast(_3584.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3586
            
            return self._parent._cast(_3586.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3587
            
            return self._parent._cast(_3587.SpringDamperSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3590
            
            return self._parent._cast(_3590.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3591
            
            return self._parent._cast(_3591.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3593
            
            return self._parent._cast(_3593.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed)

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
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3597
            
            return self._parent._cast(_3597.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3598
            
            return self._parent._cast(_3598.SynchroniserPartSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3599
            
            return self._parent._cast(_3599.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3600
            
            return self._parent._cast(_3600.SynchroniserSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3602
            
            return self._parent._cast(_3602.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3603
            
            return self._parent._cast(_3603.TorqueConverterSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3604
            
            return self._parent._cast(_3604.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed)

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3605
            
            return self._parent._cast(_3605.UnbalancedMassSteadyStateSynchronousResponseAtASpeed)

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3606
            
            return self._parent._cast(_3606.VirtualComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def worm_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3608
            
            return self._parent._cast(_3608.WormGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def worm_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3609
            
            return self._parent._cast(_3609.WormGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3611
            
            return self._parent._cast(_3611.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3612
            
            return self._parent._cast(_3612.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_steady_state_synchronous_response_at_a_speed(self) -> 'PartSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2448.Part':
        """Part: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def steady_state_synchronous_response_at_a_speed(self) -> '_3588.SteadyStateSynchronousResponseAtASpeed':
        """SteadyStateSynchronousResponseAtASpeed: 'SteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_PartSteadyStateSynchronousResponseAtASpeed(self)
