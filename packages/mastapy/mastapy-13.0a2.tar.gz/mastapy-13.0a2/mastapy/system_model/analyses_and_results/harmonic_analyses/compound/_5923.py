"""_5923.py

MountableComponentCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5753
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5871
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'MountableComponentCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentCompoundHarmonicAnalysis',)


class MountableComponentCompoundHarmonicAnalysis(_5871.ComponentCompoundHarmonicAnalysis):
    """MountableComponentCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_MountableComponentCompoundHarmonicAnalysis:
        """Special nested class for casting MountableComponentCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'MountableComponentCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def component_compound_harmonic_analysis(self):
            return self._parent._cast(_5871.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5925
            
            return self._parent._cast(_5925.PartCompoundHarmonicAnalysis)

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
        def agma_gleason_conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5850
            
            return self._parent._cast(_5850.AGMAGleasonConicalGearCompoundHarmonicAnalysis)

        @property
        def bearing_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5854
            
            return self._parent._cast(_5854.BearingCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5857
            
            return self._parent._cast(_5857.BevelDifferentialGearCompoundHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5860
            
            return self._parent._cast(_5860.BevelDifferentialPlanetGearCompoundHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5861
            
            return self._parent._cast(_5861.BevelDifferentialSunGearCompoundHarmonicAnalysis)

        @property
        def bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5862
            
            return self._parent._cast(_5862.BevelGearCompoundHarmonicAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5869
            
            return self._parent._cast(_5869.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5874
            
            return self._parent._cast(_5874.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def concept_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5875
            
            return self._parent._cast(_5875.ConceptGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5878
            
            return self._parent._cast(_5878.ConicalGearCompoundHarmonicAnalysis)

        @property
        def connector_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5882
            
            return self._parent._cast(_5882.ConnectorCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5885
            
            return self._parent._cast(_5885.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5888
            
            return self._parent._cast(_5888.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5893
            
            return self._parent._cast(_5893.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5896
            
            return self._parent._cast(_5896.CylindricalPlanetGearCompoundHarmonicAnalysis)

        @property
        def face_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5899
            
            return self._parent._cast(_5899.FaceGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5904
            
            return self._parent._cast(_5904.GearCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5908
            
            return self._parent._cast(_5908.HypoidGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5912
            
            return self._parent._cast(_5912.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5915
            
            return self._parent._cast(_5915.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5918
            
            return self._parent._cast(_5918.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def mass_disc_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5921
            
            return self._parent._cast(_5921.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5922
            
            return self._parent._cast(_5922.MeasurementComponentCompoundHarmonicAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5924
            
            return self._parent._cast(_5924.OilSealCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5928
            
            return self._parent._cast(_5928.PartToPartShearCouplingHalfCompoundHarmonicAnalysis)

        @property
        def planet_carrier_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5931
            
            return self._parent._cast(_5931.PlanetCarrierCompoundHarmonicAnalysis)

        @property
        def point_load_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5932
            
            return self._parent._cast(_5932.PointLoadCompoundHarmonicAnalysis)

        @property
        def power_load_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5933
            
            return self._parent._cast(_5933.PowerLoadCompoundHarmonicAnalysis)

        @property
        def pulley_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5934
            
            return self._parent._cast(_5934.PulleyCompoundHarmonicAnalysis)

        @property
        def ring_pins_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5935
            
            return self._parent._cast(_5935.RingPinsCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5938
            
            return self._parent._cast(_5938.RollingRingCompoundHarmonicAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5942
            
            return self._parent._cast(_5942.ShaftHubConnectionCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5945
            
            return self._parent._cast(_5945.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def spring_damper_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5950
            
            return self._parent._cast(_5950.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5951
            
            return self._parent._cast(_5951.StraightBevelDiffGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5954
            
            return self._parent._cast(_5954.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5957
            
            return self._parent._cast(_5957.StraightBevelPlanetGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5958
            
            return self._parent._cast(_5958.StraightBevelSunGearCompoundHarmonicAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5960
            
            return self._parent._cast(_5960.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5961
            
            return self._parent._cast(_5961.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5962
            
            return self._parent._cast(_5962.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5965
            
            return self._parent._cast(_5965.TorqueConverterPumpCompoundHarmonicAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5966
            
            return self._parent._cast(_5966.TorqueConverterTurbineCompoundHarmonicAnalysis)

        @property
        def unbalanced_mass_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5967
            
            return self._parent._cast(_5967.UnbalancedMassCompoundHarmonicAnalysis)

        @property
        def virtual_component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5968
            
            return self._parent._cast(_5968.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def worm_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5969
            
            return self._parent._cast(_5969.WormGearCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5972
            
            return self._parent._cast(_5972.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(self) -> 'MountableComponentCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5753.MountableComponentHarmonicAnalysis]':
        """List[MountableComponentHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5753.MountableComponentHarmonicAnalysis]':
        """List[MountableComponentHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MountableComponentCompoundHarmonicAnalysis._Cast_MountableComponentCompoundHarmonicAnalysis':
        return self._Cast_MountableComponentCompoundHarmonicAnalysis(self)
