"""_3301.py

MountableComponentSteadyStateSynchronousResponseOnAShaft
"""
from mastapy.system_model.part_model import _2444
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3249
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'MountableComponentSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentSteadyStateSynchronousResponseOnAShaft',)


class MountableComponentSteadyStateSynchronousResponseOnAShaft(_3249.ComponentSteadyStateSynchronousResponseOnAShaft):
    """MountableComponentSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting MountableComponentSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'MountableComponentSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3249.ComponentSteadyStateSynchronousResponseOnAShaft)

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
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3230
            
            return self._parent._cast(_3230.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def bearing_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3232
            
            return self._parent._cast(_3232.BearingSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3237
            
            return self._parent._cast(_3237.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3238
            
            return self._parent._cast(_3238.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3239
            
            return self._parent._cast(_3239.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3242
            
            return self._parent._cast(_3242.BevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3246
            
            return self._parent._cast(_3246.ClutchHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3251
            
            return self._parent._cast(_3251.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3255
            
            return self._parent._cast(_3255.ConceptGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3258
            
            return self._parent._cast(_3258.ConicalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def connector_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3260
            
            return self._parent._cast(_3260.ConnectorSteadyStateSynchronousResponseOnAShaft)

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3262
            
            return self._parent._cast(_3262.CouplingHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3265
            
            return self._parent._cast(_3265.CVTPulleySteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3273
            
            return self._parent._cast(_3273.CylindricalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3274
            
            return self._parent._cast(_3274.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3279
            
            return self._parent._cast(_3279.FaceGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3284
            
            return self._parent._cast(_3284.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3288
            
            return self._parent._cast(_3288.HypoidGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3292
            
            return self._parent._cast(_3292.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3295
            
            return self._parent._cast(_3295.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3298
            
            return self._parent._cast(_3298.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mass_disc_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3299
            
            return self._parent._cast(_3299.MassDiscSteadyStateSynchronousResponseOnAShaft)

        @property
        def measurement_component_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3300
            
            return self._parent._cast(_3300.MeasurementComponentSteadyStateSynchronousResponseOnAShaft)

        @property
        def oil_seal_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3302
            
            return self._parent._cast(_3302.OilSealSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3305
            
            return self._parent._cast(_3305.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def planet_carrier_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3309
            
            return self._parent._cast(_3309.PlanetCarrierSteadyStateSynchronousResponseOnAShaft)

        @property
        def point_load_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3310
            
            return self._parent._cast(_3310.PointLoadSteadyStateSynchronousResponseOnAShaft)

        @property
        def power_load_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3311
            
            return self._parent._cast(_3311.PowerLoadSteadyStateSynchronousResponseOnAShaft)

        @property
        def pulley_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3312
            
            return self._parent._cast(_3312.PulleySteadyStateSynchronousResponseOnAShaft)

        @property
        def ring_pins_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3313
            
            return self._parent._cast(_3313.RingPinsSteadyStateSynchronousResponseOnAShaft)

        @property
        def rolling_ring_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3317
            
            return self._parent._cast(_3317.RollingRingSteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_hub_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3319
            
            return self._parent._cast(_3319.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3325
            
            return self._parent._cast(_3325.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3327
            
            return self._parent._cast(_3327.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3332
            
            return self._parent._cast(_3332.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3335
            
            return self._parent._cast(_3335.StraightBevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3336
            
            return self._parent._cast(_3336.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3337
            
            return self._parent._cast(_3337.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3338
            
            return self._parent._cast(_3338.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_part_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3339
            
            return self._parent._cast(_3339.SynchroniserPartSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3340
            
            return self._parent._cast(_3340.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_pump_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3343
            
            return self._parent._cast(_3343.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_turbine_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3345
            
            return self._parent._cast(_3345.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft)

        @property
        def unbalanced_mass_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3346
            
            return self._parent._cast(_3346.UnbalancedMassSteadyStateSynchronousResponseOnAShaft)

        @property
        def virtual_component_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3347
            
            return self._parent._cast(_3347.VirtualComponentSteadyStateSynchronousResponseOnAShaft)

        @property
        def worm_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3350
            
            return self._parent._cast(_3350.WormGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3353
            
            return self._parent._cast(_3353.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(self) -> 'MountableComponentSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2444.MountableComponent':
        """MountableComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft(self)
