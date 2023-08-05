"""_3433.py

PartCompoundSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3303
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'PartCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundSteadyStateSynchronousResponseOnAShaft',)


class PartCompoundSteadyStateSynchronousResponseOnAShaft(_7508.PartCompoundAnalysis):
    """PartCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PartCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'PartCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def part_compound_analysis(self):
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
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3354
            
            return self._parent._cast(_3354.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3355
            
            return self._parent._cast(_3355.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3356
            
            return self._parent._cast(_3356.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3358
            
            return self._parent._cast(_3358.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3360
            
            return self._parent._cast(_3360.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3361
            
            return self._parent._cast(_3361.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def bearing_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3362
            
            return self._parent._cast(_3362.BearingCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def belt_drive_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3364
            
            return self._parent._cast(_3364.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3365
            
            return self._parent._cast(_3365.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3367
            
            return self._parent._cast(_3367.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3372
            
            return self._parent._cast(_3372.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def bolt_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3373
            
            return self._parent._cast(_3373.BoltCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def bolted_joint_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3374
            
            return self._parent._cast(_3374.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3375
            
            return self._parent._cast(_3375.ClutchCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3377
            
            return self._parent._cast(_3377.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3379
            
            return self._parent._cast(_3379.ComponentCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3380
            
            return self._parent._cast(_3380.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3382
            
            return self._parent._cast(_3382.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3383
            
            return self._parent._cast(_3383.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3385
            
            return self._parent._cast(_3385.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3386
            
            return self._parent._cast(_3386.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3388
            
            return self._parent._cast(_3388.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def connector_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3390
            
            return self._parent._cast(_3390.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def coupling_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3391
            
            return self._parent._cast(_3391.CouplingCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3393
            
            return self._parent._cast(_3393.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3395
            
            return self._parent._cast(_3395.CVTCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3396
            
            return self._parent._cast(_3396.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3397
            
            return self._parent._cast(_3397.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3399
            
            return self._parent._cast(_3399.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3401
            
            return self._parent._cast(_3401.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3403
            
            return self._parent._cast(_3403.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3404
            
            return self._parent._cast(_3404.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def datum_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3405
            
            return self._parent._cast(_3405.DatumCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def external_cad_model_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3406
            
            return self._parent._cast(_3406.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3407
            
            return self._parent._cast(_3407.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3409
            
            return self._parent._cast(_3409.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def fe_part_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3410
            
            return self._parent._cast(_3410.FEPartCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3411
            
            return self._parent._cast(_3411.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3412
            
            return self._parent._cast(_3412.GearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3414
            
            return self._parent._cast(_3414.GearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3415
            
            return self._parent._cast(_3415.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3416
            
            return self._parent._cast(_3416.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3418
            
            return self._parent._cast(_3418.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3420
            
            return self._parent._cast(_3420.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3422
            
            return self._parent._cast(_3422.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3423
            
            return self._parent._cast(_3423.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3425
            
            return self._parent._cast(_3425.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3426
            
            return self._parent._cast(_3426.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3428
            
            return self._parent._cast(_3428.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def mass_disc_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3429
            
            return self._parent._cast(_3429.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def measurement_component_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3430
            
            return self._parent._cast(_3430.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3431
            
            return self._parent._cast(_3431.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def oil_seal_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3432
            
            return self._parent._cast(_3432.OilSealCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3434
            
            return self._parent._cast(_3434.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3436
            
            return self._parent._cast(_3436.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3438
            
            return self._parent._cast(_3438.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def planet_carrier_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3439
            
            return self._parent._cast(_3439.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def point_load_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3440
            
            return self._parent._cast(_3440.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def power_load_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3441
            
            return self._parent._cast(_3441.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def pulley_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3442
            
            return self._parent._cast(_3442.PulleyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def ring_pins_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3443
            
            return self._parent._cast(_3443.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3445
            
            return self._parent._cast(_3445.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3446
            
            return self._parent._cast(_3446.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def root_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3448
            
            return self._parent._cast(_3448.RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3449
            
            return self._parent._cast(_3449.ShaftCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3450
            
            return self._parent._cast(_3450.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3452
            
            return self._parent._cast(_3452.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3453
            
            return self._parent._cast(_3453.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3455
            
            return self._parent._cast(_3455.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3456
            
            return self._parent._cast(_3456.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3458
            
            return self._parent._cast(_3458.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3459
            
            return self._parent._cast(_3459.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3461
            
            return self._parent._cast(_3461.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3462
            
            return self._parent._cast(_3462.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3464
            
            return self._parent._cast(_3464.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3465
            
            return self._parent._cast(_3465.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3466
            
            return self._parent._cast(_3466.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3467
            
            return self._parent._cast(_3467.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3468
            
            return self._parent._cast(_3468.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3469
            
            return self._parent._cast(_3469.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3470
            
            return self._parent._cast(_3470.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3471
            
            return self._parent._cast(_3471.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3473
            
            return self._parent._cast(_3473.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3474
            
            return self._parent._cast(_3474.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3475
            
            return self._parent._cast(_3475.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def virtual_component_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3476
            
            return self._parent._cast(_3476.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def worm_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3477
            
            return self._parent._cast(_3477.WormGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3479
            
            return self._parent._cast(_3479.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3480
            
            return self._parent._cast(_3480.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3482
            
            return self._parent._cast(_3482.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'PartCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3303.PartSteadyStateSynchronousResponseOnAShaft]':
        """List[PartSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3303.PartSteadyStateSynchronousResponseOnAShaft]':
        """List[PartSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft(self)
