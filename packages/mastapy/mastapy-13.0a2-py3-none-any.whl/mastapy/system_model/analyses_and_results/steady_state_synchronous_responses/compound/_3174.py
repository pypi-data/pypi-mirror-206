"""_3174.py

PartCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3042
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'PartCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundSteadyStateSynchronousResponse',)


class PartCompoundSteadyStateSynchronousResponse(_7508.PartCompoundAnalysis):
    """PartCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_PartCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting PartCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'PartCompoundSteadyStateSynchronousResponse'):
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
        def abstract_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3095
            
            return self._parent._cast(_3095.AbstractAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3096
            
            return self._parent._cast(_3096.AbstractShaftCompoundSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3097
            
            return self._parent._cast(_3097.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3099
            
            return self._parent._cast(_3099.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3101
            
            return self._parent._cast(_3101.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3102
            
            return self._parent._cast(_3102.AssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def bearing_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3103
            
            return self._parent._cast(_3103.BearingCompoundSteadyStateSynchronousResponse)

        @property
        def belt_drive_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3105
            
            return self._parent._cast(_3105.BeltDriveCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3106
            
            return self._parent._cast(_3106.BevelDifferentialGearCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3108
            
            return self._parent._cast(_3108.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3109
            
            return self._parent._cast(_3109.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3110
            
            return self._parent._cast(_3110.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3111
            
            return self._parent._cast(_3111.BevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3113
            
            return self._parent._cast(_3113.BevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def bolt_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3114
            
            return self._parent._cast(_3114.BoltCompoundSteadyStateSynchronousResponse)

        @property
        def bolted_joint_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3115
            
            return self._parent._cast(_3115.BoltedJointCompoundSteadyStateSynchronousResponse)

        @property
        def clutch_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3116
            
            return self._parent._cast(_3116.ClutchCompoundSteadyStateSynchronousResponse)

        @property
        def clutch_half_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3118
            
            return self._parent._cast(_3118.ClutchHalfCompoundSteadyStateSynchronousResponse)

        @property
        def component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3120
            
            return self._parent._cast(_3120.ComponentCompoundSteadyStateSynchronousResponse)

        @property
        def concept_coupling_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3121
            
            return self._parent._cast(_3121.ConceptCouplingCompoundSteadyStateSynchronousResponse)

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3123
            
            return self._parent._cast(_3123.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse)

        @property
        def concept_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3124
            
            return self._parent._cast(_3124.ConceptGearCompoundSteadyStateSynchronousResponse)

        @property
        def concept_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3126
            
            return self._parent._cast(_3126.ConceptGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def conical_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3127
            
            return self._parent._cast(_3127.ConicalGearCompoundSteadyStateSynchronousResponse)

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3129
            
            return self._parent._cast(_3129.ConicalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def connector_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3131
            
            return self._parent._cast(_3131.ConnectorCompoundSteadyStateSynchronousResponse)

        @property
        def coupling_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3132
            
            return self._parent._cast(_3132.CouplingCompoundSteadyStateSynchronousResponse)

        @property
        def coupling_half_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3134
            
            return self._parent._cast(_3134.CouplingHalfCompoundSteadyStateSynchronousResponse)

        @property
        def cvt_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3136
            
            return self._parent._cast(_3136.CVTCompoundSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3137
            
            return self._parent._cast(_3137.CVTPulleyCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3138
            
            return self._parent._cast(_3138.CycloidalAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3140
            
            return self._parent._cast(_3140.CycloidalDiscCompoundSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3142
            
            return self._parent._cast(_3142.CylindricalGearCompoundSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3144
            
            return self._parent._cast(_3144.CylindricalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3145
            
            return self._parent._cast(_3145.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse)

        @property
        def datum_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3146
            
            return self._parent._cast(_3146.DatumCompoundSteadyStateSynchronousResponse)

        @property
        def external_cad_model_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3147
            
            return self._parent._cast(_3147.ExternalCADModelCompoundSteadyStateSynchronousResponse)

        @property
        def face_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3148
            
            return self._parent._cast(_3148.FaceGearCompoundSteadyStateSynchronousResponse)

        @property
        def face_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3150
            
            return self._parent._cast(_3150.FaceGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def fe_part_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3151
            
            return self._parent._cast(_3151.FEPartCompoundSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3152
            
            return self._parent._cast(_3152.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3153
            
            return self._parent._cast(_3153.GearCompoundSteadyStateSynchronousResponse)

        @property
        def gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3155
            
            return self._parent._cast(_3155.GearSetCompoundSteadyStateSynchronousResponse)

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3156
            
            return self._parent._cast(_3156.GuideDxfModelCompoundSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3157
            
            return self._parent._cast(_3157.HypoidGearCompoundSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3159
            
            return self._parent._cast(_3159.HypoidGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3161
            
            return self._parent._cast(_3161.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3163
            
            return self._parent._cast(_3163.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3164
            
            return self._parent._cast(_3164.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3166
            
            return self._parent._cast(_3166.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3167
            
            return self._parent._cast(_3167.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3169
            
            return self._parent._cast(_3169.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def mass_disc_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3170
            
            return self._parent._cast(_3170.MassDiscCompoundSteadyStateSynchronousResponse)

        @property
        def measurement_component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3171
            
            return self._parent._cast(_3171.MeasurementComponentCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3172
            
            return self._parent._cast(_3172.MountableComponentCompoundSteadyStateSynchronousResponse)

        @property
        def oil_seal_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3173
            
            return self._parent._cast(_3173.OilSealCompoundSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3175
            
            return self._parent._cast(_3175.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3177
            
            return self._parent._cast(_3177.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse)

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3179
            
            return self._parent._cast(_3179.PlanetaryGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def planet_carrier_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3180
            
            return self._parent._cast(_3180.PlanetCarrierCompoundSteadyStateSynchronousResponse)

        @property
        def point_load_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3181
            
            return self._parent._cast(_3181.PointLoadCompoundSteadyStateSynchronousResponse)

        @property
        def power_load_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3182
            
            return self._parent._cast(_3182.PowerLoadCompoundSteadyStateSynchronousResponse)

        @property
        def pulley_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3183
            
            return self._parent._cast(_3183.PulleyCompoundSteadyStateSynchronousResponse)

        @property
        def ring_pins_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3184
            
            return self._parent._cast(_3184.RingPinsCompoundSteadyStateSynchronousResponse)

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3186
            
            return self._parent._cast(_3186.RollingRingAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def rolling_ring_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3187
            
            return self._parent._cast(_3187.RollingRingCompoundSteadyStateSynchronousResponse)

        @property
        def root_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3189
            
            return self._parent._cast(_3189.RootAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3190
            
            return self._parent._cast(_3190.ShaftCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3191
            
            return self._parent._cast(_3191.ShaftHubConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3193
            
            return self._parent._cast(_3193.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3194
            
            return self._parent._cast(_3194.SpiralBevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3196
            
            return self._parent._cast(_3196.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def spring_damper_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3197
            
            return self._parent._cast(_3197.SpringDamperCompoundSteadyStateSynchronousResponse)

        @property
        def spring_damper_half_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3199
            
            return self._parent._cast(_3199.SpringDamperHalfCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3200
            
            return self._parent._cast(_3200.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3202
            
            return self._parent._cast(_3202.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3203
            
            return self._parent._cast(_3203.StraightBevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3205
            
            return self._parent._cast(_3205.StraightBevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3206
            
            return self._parent._cast(_3206.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3207
            
            return self._parent._cast(_3207.StraightBevelSunGearCompoundSteadyStateSynchronousResponse)

        @property
        def synchroniser_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3208
            
            return self._parent._cast(_3208.SynchroniserCompoundSteadyStateSynchronousResponse)

        @property
        def synchroniser_half_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3209
            
            return self._parent._cast(_3209.SynchroniserHalfCompoundSteadyStateSynchronousResponse)

        @property
        def synchroniser_part_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3210
            
            return self._parent._cast(_3210.SynchroniserPartCompoundSteadyStateSynchronousResponse)

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3211
            
            return self._parent._cast(_3211.SynchroniserSleeveCompoundSteadyStateSynchronousResponse)

        @property
        def torque_converter_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3212
            
            return self._parent._cast(_3212.TorqueConverterCompoundSteadyStateSynchronousResponse)

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3214
            
            return self._parent._cast(_3214.TorqueConverterPumpCompoundSteadyStateSynchronousResponse)

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3215
            
            return self._parent._cast(_3215.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse)

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3216
            
            return self._parent._cast(_3216.UnbalancedMassCompoundSteadyStateSynchronousResponse)

        @property
        def virtual_component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3217
            
            return self._parent._cast(_3217.VirtualComponentCompoundSteadyStateSynchronousResponse)

        @property
        def worm_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3218
            
            return self._parent._cast(_3218.WormGearCompoundSteadyStateSynchronousResponse)

        @property
        def worm_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3220
            
            return self._parent._cast(_3220.WormGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3221
            
            return self._parent._cast(_3221.ZerolBevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3223
            
            return self._parent._cast(_3223.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_steady_state_synchronous_response(self) -> 'PartCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3042.PartSteadyStateSynchronousResponse]':
        """List[PartSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3042.PartSteadyStateSynchronousResponse]':
        """List[PartSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartCompoundSteadyStateSynchronousResponse._Cast_PartCompoundSteadyStateSynchronousResponse':
        return self._Cast_PartCompoundSteadyStateSynchronousResponse(self)
