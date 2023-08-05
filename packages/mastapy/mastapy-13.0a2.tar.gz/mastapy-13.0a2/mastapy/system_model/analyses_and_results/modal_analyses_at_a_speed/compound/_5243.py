"""_5243.py

ComponentCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5114
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5297
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'ComponentCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentCompoundModalAnalysisAtASpeed',)


class ComponentCompoundModalAnalysisAtASpeed(_5297.PartCompoundModalAnalysisAtASpeed):
    """ComponentCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_ComponentCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ComponentCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'ComponentCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def part_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5297.PartCompoundModalAnalysisAtASpeed)

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
        def abstract_shaft_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5219
            
            return self._parent._cast(_5219.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5220
            
            return self._parent._cast(_5220.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5222
            
            return self._parent._cast(_5222.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def bearing_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5226
            
            return self._parent._cast(_5226.BearingCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5229
            
            return self._parent._cast(_5229.BevelDifferentialGearCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5232
            
            return self._parent._cast(_5232.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5233
            
            return self._parent._cast(_5233.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed)

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5234
            
            return self._parent._cast(_5234.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def bolt_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5237
            
            return self._parent._cast(_5237.BoltCompoundModalAnalysisAtASpeed)

        @property
        def clutch_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5241
            
            return self._parent._cast(_5241.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5246
            
            return self._parent._cast(_5246.ConceptCouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5247
            
            return self._parent._cast(_5247.ConceptGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5250
            
            return self._parent._cast(_5250.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def connector_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5254
            
            return self._parent._cast(_5254.ConnectorCompoundModalAnalysisAtASpeed)

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5257
            
            return self._parent._cast(_5257.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5260
            
            return self._parent._cast(_5260.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5263
            
            return self._parent._cast(_5263.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5265
            
            return self._parent._cast(_5265.CylindricalGearCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5268
            
            return self._parent._cast(_5268.CylindricalPlanetGearCompoundModalAnalysisAtASpeed)

        @property
        def datum_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5269
            
            return self._parent._cast(_5269.DatumCompoundModalAnalysisAtASpeed)

        @property
        def external_cad_model_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5270
            
            return self._parent._cast(_5270.ExternalCADModelCompoundModalAnalysisAtASpeed)

        @property
        def face_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5271
            
            return self._parent._cast(_5271.FaceGearCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5274
            
            return self._parent._cast(_5274.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5276
            
            return self._parent._cast(_5276.GearCompoundModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5279
            
            return self._parent._cast(_5279.GuideDxfModelCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5280
            
            return self._parent._cast(_5280.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5284
            
            return self._parent._cast(_5284.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5287
            
            return self._parent._cast(_5287.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5290
            
            return self._parent._cast(_5290.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def mass_disc_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5293
            
            return self._parent._cast(_5293.MassDiscCompoundModalAnalysisAtASpeed)

        @property
        def measurement_component_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5294
            
            return self._parent._cast(_5294.MeasurementComponentCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5295
            
            return self._parent._cast(_5295.MountableComponentCompoundModalAnalysisAtASpeed)

        @property
        def oil_seal_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5296
            
            return self._parent._cast(_5296.OilSealCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5300
            
            return self._parent._cast(_5300.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def planet_carrier_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5303
            
            return self._parent._cast(_5303.PlanetCarrierCompoundModalAnalysisAtASpeed)

        @property
        def point_load_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5304
            
            return self._parent._cast(_5304.PointLoadCompoundModalAnalysisAtASpeed)

        @property
        def power_load_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5305
            
            return self._parent._cast(_5305.PowerLoadCompoundModalAnalysisAtASpeed)

        @property
        def pulley_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5306
            
            return self._parent._cast(_5306.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def ring_pins_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5307
            
            return self._parent._cast(_5307.RingPinsCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5310
            
            return self._parent._cast(_5310.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5313
            
            return self._parent._cast(_5313.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5314
            
            return self._parent._cast(_5314.ShaftHubConnectionCompoundModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5317
            
            return self._parent._cast(_5317.SpiralBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5322
            
            return self._parent._cast(_5322.SpringDamperHalfCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5323
            
            return self._parent._cast(_5323.StraightBevelDiffGearCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5326
            
            return self._parent._cast(_5326.StraightBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5329
            
            return self._parent._cast(_5329.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5330
            
            return self._parent._cast(_5330.StraightBevelSunGearCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5332
            
            return self._parent._cast(_5332.SynchroniserHalfCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5333
            
            return self._parent._cast(_5333.SynchroniserPartCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5334
            
            return self._parent._cast(_5334.SynchroniserSleeveCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5337
            
            return self._parent._cast(_5337.TorqueConverterPumpCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5338
            
            return self._parent._cast(_5338.TorqueConverterTurbineCompoundModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5339
            
            return self._parent._cast(_5339.UnbalancedMassCompoundModalAnalysisAtASpeed)

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5340
            
            return self._parent._cast(_5340.VirtualComponentCompoundModalAnalysisAtASpeed)

        @property
        def worm_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5341
            
            return self._parent._cast(_5341.WormGearCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5344
            
            return self._parent._cast(_5344.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def component_compound_modal_analysis_at_a_speed(self) -> 'ComponentCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5114.ComponentModalAnalysisAtASpeed]':
        """List[ComponentModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5114.ComponentModalAnalysisAtASpeed]':
        """List[ComponentModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed':
        return self._Cast_ComponentCompoundModalAnalysisAtASpeed(self)
