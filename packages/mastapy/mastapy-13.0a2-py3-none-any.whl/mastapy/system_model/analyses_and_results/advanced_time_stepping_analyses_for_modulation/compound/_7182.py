"""_7182.py

PartCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from typing import List

from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7053
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'PartCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundAdvancedTimeSteppingAnalysisForModulation',)


class PartCompoundAdvancedTimeSteppingAnalysisForModulation(_7508.PartCompoundAnalysis):
    """PartCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_PartCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting PartCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'PartCompoundAdvancedTimeSteppingAnalysisForModulation'):
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
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7103
            
            return self._parent._cast(_7103.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7104
            
            return self._parent._cast(_7104.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_or_housing_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7105
            
            return self._parent._cast(_7105.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7107
            
            return self._parent._cast(_7107.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7109
            
            return self._parent._cast(_7109.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7110
            
            return self._parent._cast(_7110.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bearing_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7111
            
            return self._parent._cast(_7111.BearingCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def belt_drive_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7113
            
            return self._parent._cast(_7113.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7114
            
            return self._parent._cast(_7114.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7116
            
            return self._parent._cast(_7116.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7117
            
            return self._parent._cast(_7117.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7118
            
            return self._parent._cast(_7118.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7119
            
            return self._parent._cast(_7119.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7121
            
            return self._parent._cast(_7121.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bolt_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7122
            
            return self._parent._cast(_7122.BoltCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bolted_joint_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7123
            
            return self._parent._cast(_7123.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def clutch_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7124
            
            return self._parent._cast(_7124.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def clutch_half_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7126
            
            return self._parent._cast(_7126.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7128
            
            return self._parent._cast(_7128.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_coupling_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7129
            
            return self._parent._cast(_7129.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7131
            
            return self._parent._cast(_7131.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7132
            
            return self._parent._cast(_7132.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7134
            
            return self._parent._cast(_7134.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7135
            
            return self._parent._cast(_7135.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7137
            
            return self._parent._cast(_7137.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connector_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7139
            
            return self._parent._cast(_7139.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7140
            
            return self._parent._cast(_7140.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7142
            
            return self._parent._cast(_7142.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cvt_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7144
            
            return self._parent._cast(_7144.CVTCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cvt_pulley_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7145
            
            return self._parent._cast(_7145.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7146
            
            return self._parent._cast(_7146.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_disc_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7148
            
            return self._parent._cast(_7148.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7150
            
            return self._parent._cast(_7150.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7152
            
            return self._parent._cast(_7152.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7153
            
            return self._parent._cast(_7153.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def datum_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7154
            
            return self._parent._cast(_7154.DatumCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def external_cad_model_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7155
            
            return self._parent._cast(_7155.ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7156
            
            return self._parent._cast(_7156.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7158
            
            return self._parent._cast(_7158.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def fe_part_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7159
            
            return self._parent._cast(_7159.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def flexible_pin_assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7160
            
            return self._parent._cast(_7160.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7161
            
            return self._parent._cast(_7161.GearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7163
            
            return self._parent._cast(_7163.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def guide_dxf_model_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7164
            
            return self._parent._cast(_7164.GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7165
            
            return self._parent._cast(_7165.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7167
            
            return self._parent._cast(_7167.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7169
            
            return self._parent._cast(_7169.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7171
            
            return self._parent._cast(_7171.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7172
            
            return self._parent._cast(_7172.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7174
            
            return self._parent._cast(_7174.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7175
            
            return self._parent._cast(_7175.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7177
            
            return self._parent._cast(_7177.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def mass_disc_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7178
            
            return self._parent._cast(_7178.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def measurement_component_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7179
            
            return self._parent._cast(_7179.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7180
            
            return self._parent._cast(_7180.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def oil_seal_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7181
            
            return self._parent._cast(_7181.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_to_part_shear_coupling_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7183
            
            return self._parent._cast(_7183.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_to_part_shear_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7185
            
            return self._parent._cast(_7185.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planetary_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7187
            
            return self._parent._cast(_7187.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planet_carrier_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7188
            
            return self._parent._cast(_7188.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def point_load_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7189
            
            return self._parent._cast(_7189.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def power_load_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7190
            
            return self._parent._cast(_7190.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def pulley_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7191
            
            return self._parent._cast(_7191.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def ring_pins_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7192
            
            return self._parent._cast(_7192.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def rolling_ring_assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7194
            
            return self._parent._cast(_7194.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def rolling_ring_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7195
            
            return self._parent._cast(_7195.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def root_assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7197
            
            return self._parent._cast(_7197.RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def shaft_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7198
            
            return self._parent._cast(_7198.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def shaft_hub_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7199
            
            return self._parent._cast(_7199.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7201
            
            return self._parent._cast(_7201.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7202
            
            return self._parent._cast(_7202.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7204
            
            return self._parent._cast(_7204.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spring_damper_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7205
            
            return self._parent._cast(_7205.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spring_damper_half_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7207
            
            return self._parent._cast(_7207.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7208
            
            return self._parent._cast(_7208.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7210
            
            return self._parent._cast(_7210.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7211
            
            return self._parent._cast(_7211.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7213
            
            return self._parent._cast(_7213.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7214
            
            return self._parent._cast(_7214.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7215
            
            return self._parent._cast(_7215.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7216
            
            return self._parent._cast(_7216.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_half_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7217
            
            return self._parent._cast(_7217.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_part_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7218
            
            return self._parent._cast(_7218.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_sleeve_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7219
            
            return self._parent._cast(_7219.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7220
            
            return self._parent._cast(_7220.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_pump_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7222
            
            return self._parent._cast(_7222.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_turbine_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7223
            
            return self._parent._cast(_7223.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def unbalanced_mass_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7224
            
            return self._parent._cast(_7224.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def virtual_component_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7225
            
            return self._parent._cast(_7225.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7226
            
            return self._parent._cast(_7226.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7228
            
            return self._parent._cast(_7228.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7229
            
            return self._parent._cast(_7229.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7231
            
            return self._parent._cast(_7231.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'PartCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_7053.PartAdvancedTimeSteppingAnalysisForModulation]':
        """List[PartAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_7053.PartAdvancedTimeSteppingAnalysisForModulation]':
        """List[PartAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PartCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_PartCompoundAdvancedTimeSteppingAnalysisForModulation(self)
