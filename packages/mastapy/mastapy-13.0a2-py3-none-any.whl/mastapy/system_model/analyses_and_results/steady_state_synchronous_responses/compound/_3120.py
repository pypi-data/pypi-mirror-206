"""_3120.py

ComponentCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2987
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3174
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'ComponentCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentCompoundSteadyStateSynchronousResponse',)


class ComponentCompoundSteadyStateSynchronousResponse(_3174.PartCompoundSteadyStateSynchronousResponse):
    """ComponentCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_ComponentCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ComponentCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'ComponentCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def part_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3174.PartCompoundSteadyStateSynchronousResponse)

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
        def bearing_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3103
            
            return self._parent._cast(_3103.BearingCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3106
            
            return self._parent._cast(_3106.BevelDifferentialGearCompoundSteadyStateSynchronousResponse)

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
        def bolt_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3114
            
            return self._parent._cast(_3114.BoltCompoundSteadyStateSynchronousResponse)

        @property
        def clutch_half_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3118
            
            return self._parent._cast(_3118.ClutchHalfCompoundSteadyStateSynchronousResponse)

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3123
            
            return self._parent._cast(_3123.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse)

        @property
        def concept_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3124
            
            return self._parent._cast(_3124.ConceptGearCompoundSteadyStateSynchronousResponse)

        @property
        def conical_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3127
            
            return self._parent._cast(_3127.ConicalGearCompoundSteadyStateSynchronousResponse)

        @property
        def connector_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3131
            
            return self._parent._cast(_3131.ConnectorCompoundSteadyStateSynchronousResponse)

        @property
        def coupling_half_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3134
            
            return self._parent._cast(_3134.CouplingHalfCompoundSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3137
            
            return self._parent._cast(_3137.CVTPulleyCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3140
            
            return self._parent._cast(_3140.CycloidalDiscCompoundSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3142
            
            return self._parent._cast(_3142.CylindricalGearCompoundSteadyStateSynchronousResponse)

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
        def fe_part_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3151
            
            return self._parent._cast(_3151.FEPartCompoundSteadyStateSynchronousResponse)

        @property
        def gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3153
            
            return self._parent._cast(_3153.GearCompoundSteadyStateSynchronousResponse)

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3156
            
            return self._parent._cast(_3156.GuideDxfModelCompoundSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3157
            
            return self._parent._cast(_3157.HypoidGearCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3161
            
            return self._parent._cast(_3161.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3164
            
            return self._parent._cast(_3164.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3167
            
            return self._parent._cast(_3167.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse)

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
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3177
            
            return self._parent._cast(_3177.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse)

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
        def rolling_ring_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3187
            
            return self._parent._cast(_3187.RollingRingCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3190
            
            return self._parent._cast(_3190.ShaftCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3191
            
            return self._parent._cast(_3191.ShaftHubConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3194
            
            return self._parent._cast(_3194.SpiralBevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def spring_damper_half_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3199
            
            return self._parent._cast(_3199.SpringDamperHalfCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3200
            
            return self._parent._cast(_3200.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3203
            
            return self._parent._cast(_3203.StraightBevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3206
            
            return self._parent._cast(_3206.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3207
            
            return self._parent._cast(_3207.StraightBevelSunGearCompoundSteadyStateSynchronousResponse)

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
        def zerol_bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3221
            
            return self._parent._cast(_3221.ZerolBevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def component_compound_steady_state_synchronous_response(self) -> 'ComponentCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_2987.ComponentSteadyStateSynchronousResponse]':
        """List[ComponentSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_2987.ComponentSteadyStateSynchronousResponse]':
        """List[ComponentSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse':
        return self._Cast_ComponentCompoundSteadyStateSynchronousResponse(self)
