"""_6184.py

PartCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6055
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'PartCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundHarmonicAnalysisOfSingleExcitation',)


class PartCompoundHarmonicAnalysisOfSingleExcitation(_7508.PartCompoundAnalysis):
    """PartCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_PartCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PartCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'PartCompoundHarmonicAnalysisOfSingleExcitation'):
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
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6105
            
            return self._parent._cast(_6105.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6106
            
            return self._parent._cast(_6106.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6107
            
            return self._parent._cast(_6107.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6109
            
            return self._parent._cast(_6109.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6111
            
            return self._parent._cast(_6111.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def assembly_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6112
            
            return self._parent._cast(_6112.AssemblyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bearing_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6113
            
            return self._parent._cast(_6113.BearingCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6115
            
            return self._parent._cast(_6115.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6116
            
            return self._parent._cast(_6116.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6118
            
            return self._parent._cast(_6118.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6119
            
            return self._parent._cast(_6119.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6120
            
            return self._parent._cast(_6120.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6121
            
            return self._parent._cast(_6121.BevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6123
            
            return self._parent._cast(_6123.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bolt_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6124
            
            return self._parent._cast(_6124.BoltCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def bolted_joint_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6125
            
            return self._parent._cast(_6125.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6126
            
            return self._parent._cast(_6126.ClutchCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6128
            
            return self._parent._cast(_6128.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def component_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6130
            
            return self._parent._cast(_6130.ComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6131
            
            return self._parent._cast(_6131.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_half_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6133
            
            return self._parent._cast(_6133.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6134
            
            return self._parent._cast(_6134.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6136
            
            return self._parent._cast(_6136.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6137
            
            return self._parent._cast(_6137.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6139
            
            return self._parent._cast(_6139.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def connector_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6141
            
            return self._parent._cast(_6141.ConnectorCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6142
            
            return self._parent._cast(_6142.CouplingCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6144
            
            return self._parent._cast(_6144.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6146
            
            return self._parent._cast(_6146.CVTCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_pulley_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6147
            
            return self._parent._cast(_6147.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6148
            
            return self._parent._cast(_6148.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6150
            
            return self._parent._cast(_6150.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6152
            
            return self._parent._cast(_6152.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6154
            
            return self._parent._cast(_6154.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6155
            
            return self._parent._cast(_6155.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def datum_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6156
            
            return self._parent._cast(_6156.DatumCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6157
            
            return self._parent._cast(_6157.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6158
            
            return self._parent._cast(_6158.FaceGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6160
            
            return self._parent._cast(_6160.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def fe_part_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6161
            
            return self._parent._cast(_6161.FEPartCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def flexible_pin_assembly_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6162
            
            return self._parent._cast(_6162.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6163
            
            return self._parent._cast(_6163.GearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6165
            
            return self._parent._cast(_6165.GearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6166
            
            return self._parent._cast(_6166.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6167
            
            return self._parent._cast(_6167.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6169
            
            return self._parent._cast(_6169.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6171
            
            return self._parent._cast(_6171.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6173
            
            return self._parent._cast(_6173.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6174
            
            return self._parent._cast(_6174.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6176
            
            return self._parent._cast(_6176.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6177
            
            return self._parent._cast(_6177.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6179
            
            return self._parent._cast(_6179.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def mass_disc_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6180
            
            return self._parent._cast(_6180.MassDiscCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6181
            
            return self._parent._cast(_6181.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6182
            
            return self._parent._cast(_6182.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def oil_seal_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6183
            
            return self._parent._cast(_6183.OilSealCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6185
            
            return self._parent._cast(_6185.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6187
            
            return self._parent._cast(_6187.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6189
            
            return self._parent._cast(_6189.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def planet_carrier_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6190
            
            return self._parent._cast(_6190.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def point_load_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6191
            
            return self._parent._cast(_6191.PointLoadCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6192
            
            return self._parent._cast(_6192.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6193
            
            return self._parent._cast(_6193.PulleyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6194
            
            return self._parent._cast(_6194.RingPinsCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_assembly_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6196
            
            return self._parent._cast(_6196.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6197
            
            return self._parent._cast(_6197.RollingRingCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def root_assembly_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6199
            
            return self._parent._cast(_6199.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6200
            
            return self._parent._cast(_6200.ShaftCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6201
            
            return self._parent._cast(_6201.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6203
            
            return self._parent._cast(_6203.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6204
            
            return self._parent._cast(_6204.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6206
            
            return self._parent._cast(_6206.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6207
            
            return self._parent._cast(_6207.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_half_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6209
            
            return self._parent._cast(_6209.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6210
            
            return self._parent._cast(_6210.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6212
            
            return self._parent._cast(_6212.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6213
            
            return self._parent._cast(_6213.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6215
            
            return self._parent._cast(_6215.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6216
            
            return self._parent._cast(_6216.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6217
            
            return self._parent._cast(_6217.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6218
            
            return self._parent._cast(_6218.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_half_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6219
            
            return self._parent._cast(_6219.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_part_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6220
            
            return self._parent._cast(_6220.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6221
            
            return self._parent._cast(_6221.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6222
            
            return self._parent._cast(_6222.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_pump_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6224
            
            return self._parent._cast(_6224.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_turbine_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6225
            
            return self._parent._cast(_6225.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6226
            
            return self._parent._cast(_6226.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6227
            
            return self._parent._cast(_6227.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6228
            
            return self._parent._cast(_6228.WormGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6230
            
            return self._parent._cast(_6230.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6231
            
            return self._parent._cast(_6231.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6233
            
            return self._parent._cast(_6233.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def part_compound_harmonic_analysis_of_single_excitation(self) -> 'PartCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6055.PartHarmonicAnalysisOfSingleExcitation]':
        """List[PartHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6055.PartHarmonicAnalysisOfSingleExcitation]':
        """List[PartHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_PartCompoundHarmonicAnalysisOfSingleExcitation(self)
