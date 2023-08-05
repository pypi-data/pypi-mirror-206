"""_5297.py

PartCompoundModalAnalysisAtASpeed
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5168
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'PartCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundModalAnalysisAtASpeed',)


class PartCompoundModalAnalysisAtASpeed(_7508.PartCompoundAnalysis):
    """PartCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_PartCompoundModalAnalysisAtASpeed:
        """Special nested class for casting PartCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'PartCompoundModalAnalysisAtASpeed'):
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
        def abstract_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5218
            
            return self._parent._cast(_5218.AbstractAssemblyCompoundModalAnalysisAtASpeed)

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
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5224
            
            return self._parent._cast(_5224.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5225
            
            return self._parent._cast(_5225.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def bearing_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5226
            
            return self._parent._cast(_5226.BearingCompoundModalAnalysisAtASpeed)

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5228
            
            return self._parent._cast(_5228.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5229
            
            return self._parent._cast(_5229.BevelDifferentialGearCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5231
            
            return self._parent._cast(_5231.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed)

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
        def bevel_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5236
            
            return self._parent._cast(_5236.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolt_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5237
            
            return self._parent._cast(_5237.BoltCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5238
            
            return self._parent._cast(_5238.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5239
            
            return self._parent._cast(_5239.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def clutch_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5241
            
            return self._parent._cast(_5241.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def component_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5243
            
            return self._parent._cast(_5243.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5244
            
            return self._parent._cast(_5244.ConceptCouplingCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5246
            
            return self._parent._cast(_5246.ConceptCouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5247
            
            return self._parent._cast(_5247.ConceptGearCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5249
            
            return self._parent._cast(_5249.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5250
            
            return self._parent._cast(_5250.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5252
            
            return self._parent._cast(_5252.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def connector_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5254
            
            return self._parent._cast(_5254.ConnectorCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5255
            
            return self._parent._cast(_5255.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5257
            
            return self._parent._cast(_5257.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def cvt_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5259
            
            return self._parent._cast(_5259.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5260
            
            return self._parent._cast(_5260.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5261
            
            return self._parent._cast(_5261.CycloidalAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5263
            
            return self._parent._cast(_5263.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5265
            
            return self._parent._cast(_5265.CylindricalGearCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5267
            
            return self._parent._cast(_5267.CylindricalGearSetCompoundModalAnalysisAtASpeed)

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
        def face_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5273
            
            return self._parent._cast(_5273.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5274
            
            return self._parent._cast(_5274.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5275
            
            return self._parent._cast(_5275.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5276
            
            return self._parent._cast(_5276.GearCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5278
            
            return self._parent._cast(_5278.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5279
            
            return self._parent._cast(_5279.GuideDxfModelCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5280
            
            return self._parent._cast(_5280.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5282
            
            return self._parent._cast(_5282.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5284
            
            return self._parent._cast(_5284.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5286
            
            return self._parent._cast(_5286.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5287
            
            return self._parent._cast(_5287.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5289
            
            return self._parent._cast(_5289.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5290
            
            return self._parent._cast(_5290.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5292
            
            return self._parent._cast(_5292.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed)

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
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5298
            
            return self._parent._cast(_5298.PartToPartShearCouplingCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5300
            
            return self._parent._cast(_5300.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5302
            
            return self._parent._cast(_5302.PlanetaryGearSetCompoundModalAnalysisAtASpeed)

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
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5309
            
            return self._parent._cast(_5309.RollingRingAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5310
            
            return self._parent._cast(_5310.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def root_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5312
            
            return self._parent._cast(_5312.RootAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5313
            
            return self._parent._cast(_5313.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5314
            
            return self._parent._cast(_5314.ShaftHubConnectionCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5316
            
            return self._parent._cast(_5316.SpecialisedAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5317
            
            return self._parent._cast(_5317.SpiralBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5319
            
            return self._parent._cast(_5319.SpiralBevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5320
            
            return self._parent._cast(_5320.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5322
            
            return self._parent._cast(_5322.SpringDamperHalfCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5323
            
            return self._parent._cast(_5323.StraightBevelDiffGearCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5325
            
            return self._parent._cast(_5325.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5326
            
            return self._parent._cast(_5326.StraightBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5328
            
            return self._parent._cast(_5328.StraightBevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5329
            
            return self._parent._cast(_5329.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5330
            
            return self._parent._cast(_5330.StraightBevelSunGearCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5331
            
            return self._parent._cast(_5331.SynchroniserCompoundModalAnalysisAtASpeed)

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
        def torque_converter_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5335
            
            return self._parent._cast(_5335.TorqueConverterCompoundModalAnalysisAtASpeed)

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
        def worm_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5343
            
            return self._parent._cast(_5343.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5344
            
            return self._parent._cast(_5344.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5346
            
            return self._parent._cast(_5346.ZerolBevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(self) -> 'PartCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5168.PartModalAnalysisAtASpeed]':
        """List[PartModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5168.PartModalAnalysisAtASpeed]':
        """List[PartModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed':
        return self._Cast_PartCompoundModalAnalysisAtASpeed(self)
