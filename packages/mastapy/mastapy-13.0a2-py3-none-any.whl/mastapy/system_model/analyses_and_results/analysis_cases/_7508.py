"""_7508.py

PartCompoundAnalysis
"""
from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7505
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'PartCompoundAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundAnalysis',)


class PartCompoundAnalysis(_7505.DesignEntityCompoundAnalysis):
    """PartCompoundAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_ANALYSIS

    class _Cast_PartCompoundAnalysis:
        """Special nested class for casting PartCompoundAnalysis to subclasses."""

        def __init__(self, parent: 'PartCompoundAnalysis'):
            self._parent = parent

        @property
        def design_entity_compound_analysis(self):
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2830
            
            return self._parent._cast(_2830.AbstractAssemblyCompoundSystemDeflection)

        @property
        def abstract_shaft_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2831
            
            return self._parent._cast(_2831.AbstractShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2832
            
            return self._parent._cast(_2832.AbstractShaftOrHousingCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2834
            
            return self._parent._cast(_2834.AGMAGleasonConicalGearCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2836
            
            return self._parent._cast(_2836.AGMAGleasonConicalGearSetCompoundSystemDeflection)

        @property
        def assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2837
            
            return self._parent._cast(_2837.AssemblyCompoundSystemDeflection)

        @property
        def bearing_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2838
            
            return self._parent._cast(_2838.BearingCompoundSystemDeflection)

        @property
        def belt_drive_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2840
            
            return self._parent._cast(_2840.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2841
            
            return self._parent._cast(_2841.BevelDifferentialGearCompoundSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2843
            
            return self._parent._cast(_2843.BevelDifferentialGearSetCompoundSystemDeflection)

        @property
        def bevel_differential_planet_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2844
            
            return self._parent._cast(_2844.BevelDifferentialPlanetGearCompoundSystemDeflection)

        @property
        def bevel_differential_sun_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2845
            
            return self._parent._cast(_2845.BevelDifferentialSunGearCompoundSystemDeflection)

        @property
        def bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2846
            
            return self._parent._cast(_2846.BevelGearCompoundSystemDeflection)

        @property
        def bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2848
            
            return self._parent._cast(_2848.BevelGearSetCompoundSystemDeflection)

        @property
        def bolt_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2849
            
            return self._parent._cast(_2849.BoltCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2850
            
            return self._parent._cast(_2850.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2851
            
            return self._parent._cast(_2851.ClutchCompoundSystemDeflection)

        @property
        def clutch_half_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2853
            
            return self._parent._cast(_2853.ClutchHalfCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2855
            
            return self._parent._cast(_2855.ComponentCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2856
            
            return self._parent._cast(_2856.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2858
            
            return self._parent._cast(_2858.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2859
            
            return self._parent._cast(_2859.ConceptGearCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2861
            
            return self._parent._cast(_2861.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2862
            
            return self._parent._cast(_2862.ConicalGearCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2864
            
            return self._parent._cast(_2864.ConicalGearSetCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2866
            
            return self._parent._cast(_2866.ConnectorCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2867
            
            return self._parent._cast(_2867.CouplingCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2869
            
            return self._parent._cast(_2869.CouplingHalfCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2871
            
            return self._parent._cast(_2871.CVTCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2872
            
            return self._parent._cast(_2872.CVTPulleyCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2873
            
            return self._parent._cast(_2873.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cycloidal_disc_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2875
            
            return self._parent._cast(_2875.CycloidalDiscCompoundSystemDeflection)

        @property
        def cylindrical_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2877
            
            return self._parent._cast(_2877.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2879
            
            return self._parent._cast(_2879.CylindricalGearSetCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2880
            
            return self._parent._cast(_2880.CylindricalPlanetGearCompoundSystemDeflection)

        @property
        def datum_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2881
            
            return self._parent._cast(_2881.DatumCompoundSystemDeflection)

        @property
        def external_cad_model_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2883
            
            return self._parent._cast(_2883.ExternalCADModelCompoundSystemDeflection)

        @property
        def face_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2884
            
            return self._parent._cast(_2884.FaceGearCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2886
            
            return self._parent._cast(_2886.FaceGearSetCompoundSystemDeflection)

        @property
        def fe_part_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2887
            
            return self._parent._cast(_2887.FEPartCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2888
            
            return self._parent._cast(_2888.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2889
            
            return self._parent._cast(_2889.GearCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2891
            
            return self._parent._cast(_2891.GearSetCompoundSystemDeflection)

        @property
        def guide_dxf_model_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2892
            
            return self._parent._cast(_2892.GuideDxfModelCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2893
            
            return self._parent._cast(_2893.HypoidGearCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2895
            
            return self._parent._cast(_2895.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2897
            
            return self._parent._cast(_2897.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2899
            
            return self._parent._cast(_2899.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2900
            
            return self._parent._cast(_2900.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2902
            
            return self._parent._cast(_2902.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2903
            
            return self._parent._cast(_2903.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2905
            
            return self._parent._cast(_2905.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection)

        @property
        def mass_disc_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2906
            
            return self._parent._cast(_2906.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2907
            
            return self._parent._cast(_2907.MeasurementComponentCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2908
            
            return self._parent._cast(_2908.MountableComponentCompoundSystemDeflection)

        @property
        def oil_seal_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2909
            
            return self._parent._cast(_2909.OilSealCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2910
            
            return self._parent._cast(_2910.PartCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2911
            
            return self._parent._cast(_2911.PartToPartShearCouplingCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2913
            
            return self._parent._cast(_2913.PartToPartShearCouplingHalfCompoundSystemDeflection)

        @property
        def planetary_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2915
            
            return self._parent._cast(_2915.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def planet_carrier_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2916
            
            return self._parent._cast(_2916.PlanetCarrierCompoundSystemDeflection)

        @property
        def point_load_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2917
            
            return self._parent._cast(_2917.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2918
            
            return self._parent._cast(_2918.PowerLoadCompoundSystemDeflection)

        @property
        def pulley_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2919
            
            return self._parent._cast(_2919.PulleyCompoundSystemDeflection)

        @property
        def ring_pins_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2920
            
            return self._parent._cast(_2920.RingPinsCompoundSystemDeflection)

        @property
        def rolling_ring_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2922
            
            return self._parent._cast(_2922.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2923
            
            return self._parent._cast(_2923.RollingRingCompoundSystemDeflection)

        @property
        def root_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2925
            
            return self._parent._cast(_2925.RootAssemblyCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2926
            
            return self._parent._cast(_2926.ShaftCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2928
            
            return self._parent._cast(_2928.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2930
            
            return self._parent._cast(_2930.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2931
            
            return self._parent._cast(_2931.SpiralBevelGearCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2933
            
            return self._parent._cast(_2933.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2934
            
            return self._parent._cast(_2934.SpringDamperCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2936
            
            return self._parent._cast(_2936.SpringDamperHalfCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2937
            
            return self._parent._cast(_2937.StraightBevelDiffGearCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2939
            
            return self._parent._cast(_2939.StraightBevelDiffGearSetCompoundSystemDeflection)

        @property
        def straight_bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2940
            
            return self._parent._cast(_2940.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2942
            
            return self._parent._cast(_2942.StraightBevelGearSetCompoundSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2943
            
            return self._parent._cast(_2943.StraightBevelPlanetGearCompoundSystemDeflection)

        @property
        def straight_bevel_sun_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2944
            
            return self._parent._cast(_2944.StraightBevelSunGearCompoundSystemDeflection)

        @property
        def synchroniser_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2945
            
            return self._parent._cast(_2945.SynchroniserCompoundSystemDeflection)

        @property
        def synchroniser_half_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2946
            
            return self._parent._cast(_2946.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2947
            
            return self._parent._cast(_2947.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2948
            
            return self._parent._cast(_2948.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2949
            
            return self._parent._cast(_2949.TorqueConverterCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2951
            
            return self._parent._cast(_2951.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2952
            
            return self._parent._cast(_2952.TorqueConverterTurbineCompoundSystemDeflection)

        @property
        def unbalanced_mass_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2953
            
            return self._parent._cast(_2953.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2954
            
            return self._parent._cast(_2954.VirtualComponentCompoundSystemDeflection)

        @property
        def worm_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2955
            
            return self._parent._cast(_2955.WormGearCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2957
            
            return self._parent._cast(_2957.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2958
            
            return self._parent._cast(_2958.ZerolBevelGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2960
            
            return self._parent._cast(_2960.ZerolBevelGearSetCompoundSystemDeflection)

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
        def part_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3174
            
            return self._parent._cast(_3174.PartCompoundSteadyStateSynchronousResponse)

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
        def part_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3433
            
            return self._parent._cast(_3433.PartCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3613
            
            return self._parent._cast(_3613.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3614
            
            return self._parent._cast(_3614.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3615
            
            return self._parent._cast(_3615.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3617
            
            return self._parent._cast(_3617.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3619
            
            return self._parent._cast(_3619.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3620
            
            return self._parent._cast(_3620.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bearing_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3621
            
            return self._parent._cast(_3621.BearingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def belt_drive_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3623
            
            return self._parent._cast(_3623.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3624
            
            return self._parent._cast(_3624.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3626
            
            return self._parent._cast(_3626.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3627
            
            return self._parent._cast(_3627.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3628
            
            return self._parent._cast(_3628.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3629
            
            return self._parent._cast(_3629.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3631
            
            return self._parent._cast(_3631.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bolt_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3632
            
            return self._parent._cast(_3632.BoltCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bolted_joint_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3633
            
            return self._parent._cast(_3633.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3634
            
            return self._parent._cast(_3634.ClutchCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3636
            
            return self._parent._cast(_3636.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3638
            
            return self._parent._cast(_3638.ComponentCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3639
            
            return self._parent._cast(_3639.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3641
            
            return self._parent._cast(_3641.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3642
            
            return self._parent._cast(_3642.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3644
            
            return self._parent._cast(_3644.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3645
            
            return self._parent._cast(_3645.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3647
            
            return self._parent._cast(_3647.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def connector_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3649
            
            return self._parent._cast(_3649.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3650
            
            return self._parent._cast(_3650.CouplingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3652
            
            return self._parent._cast(_3652.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3654
            
            return self._parent._cast(_3654.CVTCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3655
            
            return self._parent._cast(_3655.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3656
            
            return self._parent._cast(_3656.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3658
            
            return self._parent._cast(_3658.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3660
            
            return self._parent._cast(_3660.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3662
            
            return self._parent._cast(_3662.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3663
            
            return self._parent._cast(_3663.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def datum_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3664
            
            return self._parent._cast(_3664.DatumCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def external_cad_model_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3665
            
            return self._parent._cast(_3665.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def face_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3666
            
            return self._parent._cast(_3666.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def face_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3668
            
            return self._parent._cast(_3668.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def fe_part_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3669
            
            return self._parent._cast(_3669.FEPartCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3670
            
            return self._parent._cast(_3670.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3671
            
            return self._parent._cast(_3671.GearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3673
            
            return self._parent._cast(_3673.GearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3674
            
            return self._parent._cast(_3674.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3675
            
            return self._parent._cast(_3675.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3677
            
            return self._parent._cast(_3677.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3679
            
            return self._parent._cast(_3679.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3681
            
            return self._parent._cast(_3681.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3682
            
            return self._parent._cast(_3682.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3684
            
            return self._parent._cast(_3684.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3685
            
            return self._parent._cast(_3685.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3687
            
            return self._parent._cast(_3687.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def mass_disc_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3688
            
            return self._parent._cast(_3688.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def measurement_component_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3689
            
            return self._parent._cast(_3689.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3690
            
            return self._parent._cast(_3690.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def oil_seal_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3691
            
            return self._parent._cast(_3691.OilSealCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3692
            
            return self._parent._cast(_3692.PartCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3693
            
            return self._parent._cast(_3693.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3695
            
            return self._parent._cast(_3695.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3697
            
            return self._parent._cast(_3697.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def planet_carrier_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3698
            
            return self._parent._cast(_3698.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def point_load_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3699
            
            return self._parent._cast(_3699.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def power_load_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3700
            
            return self._parent._cast(_3700.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3701
            
            return self._parent._cast(_3701.PulleyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def ring_pins_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3702
            
            return self._parent._cast(_3702.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3704
            
            return self._parent._cast(_3704.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3705
            
            return self._parent._cast(_3705.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def root_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3707
            
            return self._parent._cast(_3707.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3708
            
            return self._parent._cast(_3708.ShaftCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3709
            
            return self._parent._cast(_3709.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3711
            
            return self._parent._cast(_3711.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3712
            
            return self._parent._cast(_3712.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3714
            
            return self._parent._cast(_3714.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3715
            
            return self._parent._cast(_3715.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3717
            
            return self._parent._cast(_3717.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3718
            
            return self._parent._cast(_3718.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3720
            
            return self._parent._cast(_3720.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3721
            
            return self._parent._cast(_3721.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3723
            
            return self._parent._cast(_3723.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3724
            
            return self._parent._cast(_3724.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3725
            
            return self._parent._cast(_3725.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3726
            
            return self._parent._cast(_3726.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3727
            
            return self._parent._cast(_3727.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3728
            
            return self._parent._cast(_3728.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3729
            
            return self._parent._cast(_3729.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3730
            
            return self._parent._cast(_3730.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3732
            
            return self._parent._cast(_3732.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3733
            
            return self._parent._cast(_3733.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3734
            
            return self._parent._cast(_3734.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def virtual_component_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3735
            
            return self._parent._cast(_3735.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def worm_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3736
            
            return self._parent._cast(_3736.WormGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3738
            
            return self._parent._cast(_3738.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3739
            
            return self._parent._cast(_3739.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3741
            
            return self._parent._cast(_3741.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3874
            
            return self._parent._cast(_3874.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3875
            
            return self._parent._cast(_3875.AbstractShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3876
            
            return self._parent._cast(_3876.AbstractShaftOrHousingCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3878
            
            return self._parent._cast(_3878.AGMAGleasonConicalGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3880
            
            return self._parent._cast(_3880.AGMAGleasonConicalGearSetCompoundStabilityAnalysis)

        @property
        def assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3881
            
            return self._parent._cast(_3881.AssemblyCompoundStabilityAnalysis)

        @property
        def bearing_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3882
            
            return self._parent._cast(_3882.BearingCompoundStabilityAnalysis)

        @property
        def belt_drive_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3884
            
            return self._parent._cast(_3884.BeltDriveCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3885
            
            return self._parent._cast(_3885.BevelDifferentialGearCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3887
            
            return self._parent._cast(_3887.BevelDifferentialGearSetCompoundStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3888
            
            return self._parent._cast(_3888.BevelDifferentialPlanetGearCompoundStabilityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3889
            
            return self._parent._cast(_3889.BevelDifferentialSunGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3890
            
            return self._parent._cast(_3890.BevelGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3892
            
            return self._parent._cast(_3892.BevelGearSetCompoundStabilityAnalysis)

        @property
        def bolt_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3893
            
            return self._parent._cast(_3893.BoltCompoundStabilityAnalysis)

        @property
        def bolted_joint_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3894
            
            return self._parent._cast(_3894.BoltedJointCompoundStabilityAnalysis)

        @property
        def clutch_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3895
            
            return self._parent._cast(_3895.ClutchCompoundStabilityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3897
            
            return self._parent._cast(_3897.ClutchHalfCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3899
            
            return self._parent._cast(_3899.ComponentCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3900
            
            return self._parent._cast(_3900.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3902
            
            return self._parent._cast(_3902.ConceptCouplingHalfCompoundStabilityAnalysis)

        @property
        def concept_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3903
            
            return self._parent._cast(_3903.ConceptGearCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3905
            
            return self._parent._cast(_3905.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3906
            
            return self._parent._cast(_3906.ConicalGearCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3908
            
            return self._parent._cast(_3908.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3910
            
            return self._parent._cast(_3910.ConnectorCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3911
            
            return self._parent._cast(_3911.CouplingCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3913
            
            return self._parent._cast(_3913.CouplingHalfCompoundStabilityAnalysis)

        @property
        def cvt_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3915
            
            return self._parent._cast(_3915.CVTCompoundStabilityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3916
            
            return self._parent._cast(_3916.CVTPulleyCompoundStabilityAnalysis)

        @property
        def cycloidal_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3917
            
            return self._parent._cast(_3917.CycloidalAssemblyCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3919
            
            return self._parent._cast(_3919.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3921
            
            return self._parent._cast(_3921.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3923
            
            return self._parent._cast(_3923.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3924
            
            return self._parent._cast(_3924.CylindricalPlanetGearCompoundStabilityAnalysis)

        @property
        def datum_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3925
            
            return self._parent._cast(_3925.DatumCompoundStabilityAnalysis)

        @property
        def external_cad_model_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3926
            
            return self._parent._cast(_3926.ExternalCADModelCompoundStabilityAnalysis)

        @property
        def face_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3927
            
            return self._parent._cast(_3927.FaceGearCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3929
            
            return self._parent._cast(_3929.FaceGearSetCompoundStabilityAnalysis)

        @property
        def fe_part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3930
            
            return self._parent._cast(_3930.FEPartCompoundStabilityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3931
            
            return self._parent._cast(_3931.FlexiblePinAssemblyCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3932
            
            return self._parent._cast(_3932.GearCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3934
            
            return self._parent._cast(_3934.GearSetCompoundStabilityAnalysis)

        @property
        def guide_dxf_model_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3935
            
            return self._parent._cast(_3935.GuideDxfModelCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3936
            
            return self._parent._cast(_3936.HypoidGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3938
            
            return self._parent._cast(_3938.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3940
            
            return self._parent._cast(_3940.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3942
            
            return self._parent._cast(_3942.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3943
            
            return self._parent._cast(_3943.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3945
            
            return self._parent._cast(_3945.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3946
            
            return self._parent._cast(_3946.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3948
            
            return self._parent._cast(_3948.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def mass_disc_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3949
            
            return self._parent._cast(_3949.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3950
            
            return self._parent._cast(_3950.MeasurementComponentCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3951
            
            return self._parent._cast(_3951.MountableComponentCompoundStabilityAnalysis)

        @property
        def oil_seal_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3952
            
            return self._parent._cast(_3952.OilSealCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3953
            
            return self._parent._cast(_3953.PartCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3954
            
            return self._parent._cast(_3954.PartToPartShearCouplingCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3956
            
            return self._parent._cast(_3956.PartToPartShearCouplingHalfCompoundStabilityAnalysis)

        @property
        def planetary_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3958
            
            return self._parent._cast(_3958.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def planet_carrier_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3959
            
            return self._parent._cast(_3959.PlanetCarrierCompoundStabilityAnalysis)

        @property
        def point_load_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3960
            
            return self._parent._cast(_3960.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3961
            
            return self._parent._cast(_3961.PowerLoadCompoundStabilityAnalysis)

        @property
        def pulley_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3962
            
            return self._parent._cast(_3962.PulleyCompoundStabilityAnalysis)

        @property
        def ring_pins_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3963
            
            return self._parent._cast(_3963.RingPinsCompoundStabilityAnalysis)

        @property
        def rolling_ring_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3965
            
            return self._parent._cast(_3965.RollingRingAssemblyCompoundStabilityAnalysis)

        @property
        def rolling_ring_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3966
            
            return self._parent._cast(_3966.RollingRingCompoundStabilityAnalysis)

        @property
        def root_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3968
            
            return self._parent._cast(_3968.RootAssemblyCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3969
            
            return self._parent._cast(_3969.ShaftCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3970
            
            return self._parent._cast(_3970.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3972
            
            return self._parent._cast(_3972.SpecialisedAssemblyCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3973
            
            return self._parent._cast(_3973.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3975
            
            return self._parent._cast(_3975.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3976
            
            return self._parent._cast(_3976.SpringDamperCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3978
            
            return self._parent._cast(_3978.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3979
            
            return self._parent._cast(_3979.StraightBevelDiffGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3981
            
            return self._parent._cast(_3981.StraightBevelDiffGearSetCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3982
            
            return self._parent._cast(_3982.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3984
            
            return self._parent._cast(_3984.StraightBevelGearSetCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3985
            
            return self._parent._cast(_3985.StraightBevelPlanetGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3986
            
            return self._parent._cast(_3986.StraightBevelSunGearCompoundStabilityAnalysis)

        @property
        def synchroniser_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3987
            
            return self._parent._cast(_3987.SynchroniserCompoundStabilityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3988
            
            return self._parent._cast(_3988.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3989
            
            return self._parent._cast(_3989.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3990
            
            return self._parent._cast(_3990.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3991
            
            return self._parent._cast(_3991.TorqueConverterCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3993
            
            return self._parent._cast(_3993.TorqueConverterPumpCompoundStabilityAnalysis)

        @property
        def torque_converter_turbine_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3994
            
            return self._parent._cast(_3994.TorqueConverterTurbineCompoundStabilityAnalysis)

        @property
        def unbalanced_mass_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3995
            
            return self._parent._cast(_3995.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3996
            
            return self._parent._cast(_3996.VirtualComponentCompoundStabilityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3997
            
            return self._parent._cast(_3997.WormGearCompoundStabilityAnalysis)

        @property
        def worm_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3999
            
            return self._parent._cast(_3999.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4000
            
            return self._parent._cast(_4000.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4002
            
            return self._parent._cast(_4002.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4142
            
            return self._parent._cast(_4142.AbstractAssemblyCompoundPowerFlow)

        @property
        def abstract_shaft_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4143
            
            return self._parent._cast(_4143.AbstractShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4144
            
            return self._parent._cast(_4144.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4146
            
            return self._parent._cast(_4146.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4148
            
            return self._parent._cast(_4148.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4149
            
            return self._parent._cast(_4149.AssemblyCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4150
            
            return self._parent._cast(_4150.BearingCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4152
            
            return self._parent._cast(_4152.BeltDriveCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4153
            
            return self._parent._cast(_4153.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4155
            
            return self._parent._cast(_4155.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4156
            
            return self._parent._cast(_4156.BevelDifferentialPlanetGearCompoundPowerFlow)

        @property
        def bevel_differential_sun_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4157
            
            return self._parent._cast(_4157.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4158
            
            return self._parent._cast(_4158.BevelGearCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4160
            
            return self._parent._cast(_4160.BevelGearSetCompoundPowerFlow)

        @property
        def bolt_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4161
            
            return self._parent._cast(_4161.BoltCompoundPowerFlow)

        @property
        def bolted_joint_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4162
            
            return self._parent._cast(_4162.BoltedJointCompoundPowerFlow)

        @property
        def clutch_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4163
            
            return self._parent._cast(_4163.ClutchCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4165
            
            return self._parent._cast(_4165.ClutchHalfCompoundPowerFlow)

        @property
        def component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4167
            
            return self._parent._cast(_4167.ComponentCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4168
            
            return self._parent._cast(_4168.ConceptCouplingCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4170
            
            return self._parent._cast(_4170.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4171
            
            return self._parent._cast(_4171.ConceptGearCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4173
            
            return self._parent._cast(_4173.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4174
            
            return self._parent._cast(_4174.ConicalGearCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4176
            
            return self._parent._cast(_4176.ConicalGearSetCompoundPowerFlow)

        @property
        def connector_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4178
            
            return self._parent._cast(_4178.ConnectorCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4179
            
            return self._parent._cast(_4179.CouplingCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4181
            
            return self._parent._cast(_4181.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4183
            
            return self._parent._cast(_4183.CVTCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4184
            
            return self._parent._cast(_4184.CVTPulleyCompoundPowerFlow)

        @property
        def cycloidal_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4185
            
            return self._parent._cast(_4185.CycloidalAssemblyCompoundPowerFlow)

        @property
        def cycloidal_disc_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4187
            
            return self._parent._cast(_4187.CycloidalDiscCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4189
            
            return self._parent._cast(_4189.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4191
            
            return self._parent._cast(_4191.CylindricalGearSetCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4192
            
            return self._parent._cast(_4192.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def datum_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4193
            
            return self._parent._cast(_4193.DatumCompoundPowerFlow)

        @property
        def external_cad_model_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4194
            
            return self._parent._cast(_4194.ExternalCADModelCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4195
            
            return self._parent._cast(_4195.FaceGearCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4197
            
            return self._parent._cast(_4197.FaceGearSetCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4198
            
            return self._parent._cast(_4198.FEPartCompoundPowerFlow)

        @property
        def flexible_pin_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4199
            
            return self._parent._cast(_4199.FlexiblePinAssemblyCompoundPowerFlow)

        @property
        def gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4200
            
            return self._parent._cast(_4200.GearCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4202
            
            return self._parent._cast(_4202.GearSetCompoundPowerFlow)

        @property
        def guide_dxf_model_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4203
            
            return self._parent._cast(_4203.GuideDxfModelCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4204
            
            return self._parent._cast(_4204.HypoidGearCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4206
            
            return self._parent._cast(_4206.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4208
            
            return self._parent._cast(_4208.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4210
            
            return self._parent._cast(_4210.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4211
            
            return self._parent._cast(_4211.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4213
            
            return self._parent._cast(_4213.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4214
            
            return self._parent._cast(_4214.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4216
            
            return self._parent._cast(_4216.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow)

        @property
        def mass_disc_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4217
            
            return self._parent._cast(_4217.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4218
            
            return self._parent._cast(_4218.MeasurementComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4219
            
            return self._parent._cast(_4219.MountableComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4220
            
            return self._parent._cast(_4220.OilSealCompoundPowerFlow)

        @property
        def part_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4221
            
            return self._parent._cast(_4221.PartCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4222
            
            return self._parent._cast(_4222.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4224
            
            return self._parent._cast(_4224.PartToPartShearCouplingHalfCompoundPowerFlow)

        @property
        def planetary_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4226
            
            return self._parent._cast(_4226.PlanetaryGearSetCompoundPowerFlow)

        @property
        def planet_carrier_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4227
            
            return self._parent._cast(_4227.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4228
            
            return self._parent._cast(_4228.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4229
            
            return self._parent._cast(_4229.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4230
            
            return self._parent._cast(_4230.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4231
            
            return self._parent._cast(_4231.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4233
            
            return self._parent._cast(_4233.RollingRingAssemblyCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4234
            
            return self._parent._cast(_4234.RollingRingCompoundPowerFlow)

        @property
        def root_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4236
            
            return self._parent._cast(_4236.RootAssemblyCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4237
            
            return self._parent._cast(_4237.ShaftCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4238
            
            return self._parent._cast(_4238.ShaftHubConnectionCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4240
            
            return self._parent._cast(_4240.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4241
            
            return self._parent._cast(_4241.SpiralBevelGearCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4243
            
            return self._parent._cast(_4243.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4244
            
            return self._parent._cast(_4244.SpringDamperCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4246
            
            return self._parent._cast(_4246.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4247
            
            return self._parent._cast(_4247.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4249
            
            return self._parent._cast(_4249.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4250
            
            return self._parent._cast(_4250.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4252
            
            return self._parent._cast(_4252.StraightBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4253
            
            return self._parent._cast(_4253.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4254
            
            return self._parent._cast(_4254.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4255
            
            return self._parent._cast(_4255.SynchroniserCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4256
            
            return self._parent._cast(_4256.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4257
            
            return self._parent._cast(_4257.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4258
            
            return self._parent._cast(_4258.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4259
            
            return self._parent._cast(_4259.TorqueConverterCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4261
            
            return self._parent._cast(_4261.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4262
            
            return self._parent._cast(_4262.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4263
            
            return self._parent._cast(_4263.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4264
            
            return self._parent._cast(_4264.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4265
            
            return self._parent._cast(_4265.WormGearCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4267
            
            return self._parent._cast(_4267.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4268
            
            return self._parent._cast(_4268.ZerolBevelGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4270
            
            return self._parent._cast(_4270.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def abstract_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4418
            
            return self._parent._cast(_4418.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def abstract_shaft_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4419
            
            return self._parent._cast(_4419.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4420
            
            return self._parent._cast(_4420.AbstractShaftOrHousingCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4422
            
            return self._parent._cast(_4422.AGMAGleasonConicalGearCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4424
            
            return self._parent._cast(_4424.AGMAGleasonConicalGearSetCompoundParametricStudyTool)

        @property
        def assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4425
            
            return self._parent._cast(_4425.AssemblyCompoundParametricStudyTool)

        @property
        def bearing_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4426
            
            return self._parent._cast(_4426.BearingCompoundParametricStudyTool)

        @property
        def belt_drive_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4428
            
            return self._parent._cast(_4428.BeltDriveCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4429
            
            return self._parent._cast(_4429.BevelDifferentialGearCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4431
            
            return self._parent._cast(_4431.BevelDifferentialGearSetCompoundParametricStudyTool)

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4432
            
            return self._parent._cast(_4432.BevelDifferentialPlanetGearCompoundParametricStudyTool)

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4433
            
            return self._parent._cast(_4433.BevelDifferentialSunGearCompoundParametricStudyTool)

        @property
        def bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4434
            
            return self._parent._cast(_4434.BevelGearCompoundParametricStudyTool)

        @property
        def bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4436
            
            return self._parent._cast(_4436.BevelGearSetCompoundParametricStudyTool)

        @property
        def bolt_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4437
            
            return self._parent._cast(_4437.BoltCompoundParametricStudyTool)

        @property
        def bolted_joint_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4438
            
            return self._parent._cast(_4438.BoltedJointCompoundParametricStudyTool)

        @property
        def clutch_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4439
            
            return self._parent._cast(_4439.ClutchCompoundParametricStudyTool)

        @property
        def clutch_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4441
            
            return self._parent._cast(_4441.ClutchHalfCompoundParametricStudyTool)

        @property
        def component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4443
            
            return self._parent._cast(_4443.ComponentCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4444
            
            return self._parent._cast(_4444.ConceptCouplingCompoundParametricStudyTool)

        @property
        def concept_coupling_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4446
            
            return self._parent._cast(_4446.ConceptCouplingHalfCompoundParametricStudyTool)

        @property
        def concept_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4447
            
            return self._parent._cast(_4447.ConceptGearCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4449
            
            return self._parent._cast(_4449.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4450
            
            return self._parent._cast(_4450.ConicalGearCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4452
            
            return self._parent._cast(_4452.ConicalGearSetCompoundParametricStudyTool)

        @property
        def connector_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4454
            
            return self._parent._cast(_4454.ConnectorCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4455
            
            return self._parent._cast(_4455.CouplingCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4457
            
            return self._parent._cast(_4457.CouplingHalfCompoundParametricStudyTool)

        @property
        def cvt_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4459
            
            return self._parent._cast(_4459.CVTCompoundParametricStudyTool)

        @property
        def cvt_pulley_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4460
            
            return self._parent._cast(_4460.CVTPulleyCompoundParametricStudyTool)

        @property
        def cycloidal_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4461
            
            return self._parent._cast(_4461.CycloidalAssemblyCompoundParametricStudyTool)

        @property
        def cycloidal_disc_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4463
            
            return self._parent._cast(_4463.CycloidalDiscCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4465
            
            return self._parent._cast(_4465.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4467
            
            return self._parent._cast(_4467.CylindricalGearSetCompoundParametricStudyTool)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4468
            
            return self._parent._cast(_4468.CylindricalPlanetGearCompoundParametricStudyTool)

        @property
        def datum_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4469
            
            return self._parent._cast(_4469.DatumCompoundParametricStudyTool)

        @property
        def external_cad_model_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4470
            
            return self._parent._cast(_4470.ExternalCADModelCompoundParametricStudyTool)

        @property
        def face_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4471
            
            return self._parent._cast(_4471.FaceGearCompoundParametricStudyTool)

        @property
        def face_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4473
            
            return self._parent._cast(_4473.FaceGearSetCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4474
            
            return self._parent._cast(_4474.FEPartCompoundParametricStudyTool)

        @property
        def flexible_pin_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4475
            
            return self._parent._cast(_4475.FlexiblePinAssemblyCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4476
            
            return self._parent._cast(_4476.GearCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4478
            
            return self._parent._cast(_4478.GearSetCompoundParametricStudyTool)

        @property
        def guide_dxf_model_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4479
            
            return self._parent._cast(_4479.GuideDxfModelCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4480
            
            return self._parent._cast(_4480.HypoidGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4482
            
            return self._parent._cast(_4482.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4484
            
            return self._parent._cast(_4484.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4486
            
            return self._parent._cast(_4486.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4487
            
            return self._parent._cast(_4487.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4489
            
            return self._parent._cast(_4489.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4490
            
            return self._parent._cast(_4490.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4492
            
            return self._parent._cast(_4492.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool)

        @property
        def mass_disc_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4493
            
            return self._parent._cast(_4493.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4494
            
            return self._parent._cast(_4494.MeasurementComponentCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4495
            
            return self._parent._cast(_4495.MountableComponentCompoundParametricStudyTool)

        @property
        def oil_seal_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4496
            
            return self._parent._cast(_4496.OilSealCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4497
            
            return self._parent._cast(_4497.PartCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4498
            
            return self._parent._cast(_4498.PartToPartShearCouplingCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4500
            
            return self._parent._cast(_4500.PartToPartShearCouplingHalfCompoundParametricStudyTool)

        @property
        def planetary_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4502
            
            return self._parent._cast(_4502.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def planet_carrier_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4503
            
            return self._parent._cast(_4503.PlanetCarrierCompoundParametricStudyTool)

        @property
        def point_load_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4504
            
            return self._parent._cast(_4504.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4505
            
            return self._parent._cast(_4505.PowerLoadCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4506
            
            return self._parent._cast(_4506.PulleyCompoundParametricStudyTool)

        @property
        def ring_pins_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4507
            
            return self._parent._cast(_4507.RingPinsCompoundParametricStudyTool)

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4509
            
            return self._parent._cast(_4509.RollingRingAssemblyCompoundParametricStudyTool)

        @property
        def rolling_ring_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4510
            
            return self._parent._cast(_4510.RollingRingCompoundParametricStudyTool)

        @property
        def root_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4512
            
            return self._parent._cast(_4512.RootAssemblyCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4513
            
            return self._parent._cast(_4513.ShaftCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4514
            
            return self._parent._cast(_4514.ShaftHubConnectionCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4516
            
            return self._parent._cast(_4516.SpecialisedAssemblyCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4517
            
            return self._parent._cast(_4517.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4519
            
            return self._parent._cast(_4519.SpiralBevelGearSetCompoundParametricStudyTool)

        @property
        def spring_damper_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4520
            
            return self._parent._cast(_4520.SpringDamperCompoundParametricStudyTool)

        @property
        def spring_damper_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4522
            
            return self._parent._cast(_4522.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4523
            
            return self._parent._cast(_4523.StraightBevelDiffGearCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4525
            
            return self._parent._cast(_4525.StraightBevelDiffGearSetCompoundParametricStudyTool)

        @property
        def straight_bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4526
            
            return self._parent._cast(_4526.StraightBevelGearCompoundParametricStudyTool)

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4528
            
            return self._parent._cast(_4528.StraightBevelGearSetCompoundParametricStudyTool)

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4529
            
            return self._parent._cast(_4529.StraightBevelPlanetGearCompoundParametricStudyTool)

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4530
            
            return self._parent._cast(_4530.StraightBevelSunGearCompoundParametricStudyTool)

        @property
        def synchroniser_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4531
            
            return self._parent._cast(_4531.SynchroniserCompoundParametricStudyTool)

        @property
        def synchroniser_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4532
            
            return self._parent._cast(_4532.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4533
            
            return self._parent._cast(_4533.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4534
            
            return self._parent._cast(_4534.SynchroniserSleeveCompoundParametricStudyTool)

        @property
        def torque_converter_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4535
            
            return self._parent._cast(_4535.TorqueConverterCompoundParametricStudyTool)

        @property
        def torque_converter_pump_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4537
            
            return self._parent._cast(_4537.TorqueConverterPumpCompoundParametricStudyTool)

        @property
        def torque_converter_turbine_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4538
            
            return self._parent._cast(_4538.TorqueConverterTurbineCompoundParametricStudyTool)

        @property
        def unbalanced_mass_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4539
            
            return self._parent._cast(_4539.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4540
            
            return self._parent._cast(_4540.VirtualComponentCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4541
            
            return self._parent._cast(_4541.WormGearCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4543
            
            return self._parent._cast(_4543.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4544
            
            return self._parent._cast(_4544.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4546
            
            return self._parent._cast(_4546.ZerolBevelGearSetCompoundParametricStudyTool)

        @property
        def abstract_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4701
            
            return self._parent._cast(_4701.AbstractAssemblyCompoundModalAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4702
            
            return self._parent._cast(_4702.AbstractShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4703
            
            return self._parent._cast(_4703.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4705
            
            return self._parent._cast(_4705.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4707
            
            return self._parent._cast(_4707.AGMAGleasonConicalGearSetCompoundModalAnalysis)

        @property
        def assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4708
            
            return self._parent._cast(_4708.AssemblyCompoundModalAnalysis)

        @property
        def bearing_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4709
            
            return self._parent._cast(_4709.BearingCompoundModalAnalysis)

        @property
        def belt_drive_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4711
            
            return self._parent._cast(_4711.BeltDriveCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4712
            
            return self._parent._cast(_4712.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4714
            
            return self._parent._cast(_4714.BevelDifferentialGearSetCompoundModalAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4715
            
            return self._parent._cast(_4715.BevelDifferentialPlanetGearCompoundModalAnalysis)

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4716
            
            return self._parent._cast(_4716.BevelDifferentialSunGearCompoundModalAnalysis)

        @property
        def bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4717
            
            return self._parent._cast(_4717.BevelGearCompoundModalAnalysis)

        @property
        def bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4719
            
            return self._parent._cast(_4719.BevelGearSetCompoundModalAnalysis)

        @property
        def bolt_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4720
            
            return self._parent._cast(_4720.BoltCompoundModalAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4721
            
            return self._parent._cast(_4721.BoltedJointCompoundModalAnalysis)

        @property
        def clutch_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4722
            
            return self._parent._cast(_4722.ClutchCompoundModalAnalysis)

        @property
        def clutch_half_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4724
            
            return self._parent._cast(_4724.ClutchHalfCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4726
            
            return self._parent._cast(_4726.ComponentCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4727
            
            return self._parent._cast(_4727.ConceptCouplingCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4729
            
            return self._parent._cast(_4729.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4730
            
            return self._parent._cast(_4730.ConceptGearCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4732
            
            return self._parent._cast(_4732.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4733
            
            return self._parent._cast(_4733.ConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4735
            
            return self._parent._cast(_4735.ConicalGearSetCompoundModalAnalysis)

        @property
        def connector_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4737
            
            return self._parent._cast(_4737.ConnectorCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4738
            
            return self._parent._cast(_4738.CouplingCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4740
            
            return self._parent._cast(_4740.CouplingHalfCompoundModalAnalysis)

        @property
        def cvt_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4742
            
            return self._parent._cast(_4742.CVTCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4743
            
            return self._parent._cast(_4743.CVTPulleyCompoundModalAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4744
            
            return self._parent._cast(_4744.CycloidalAssemblyCompoundModalAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4746
            
            return self._parent._cast(_4746.CycloidalDiscCompoundModalAnalysis)

        @property
        def cylindrical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4748
            
            return self._parent._cast(_4748.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4750
            
            return self._parent._cast(_4750.CylindricalGearSetCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4751
            
            return self._parent._cast(_4751.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def datum_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4752
            
            return self._parent._cast(_4752.DatumCompoundModalAnalysis)

        @property
        def external_cad_model_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4753
            
            return self._parent._cast(_4753.ExternalCADModelCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4754
            
            return self._parent._cast(_4754.FaceGearCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4756
            
            return self._parent._cast(_4756.FaceGearSetCompoundModalAnalysis)

        @property
        def fe_part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4757
            
            return self._parent._cast(_4757.FEPartCompoundModalAnalysis)

        @property
        def flexible_pin_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4758
            
            return self._parent._cast(_4758.FlexiblePinAssemblyCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4759
            
            return self._parent._cast(_4759.GearCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4761
            
            return self._parent._cast(_4761.GearSetCompoundModalAnalysis)

        @property
        def guide_dxf_model_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4762
            
            return self._parent._cast(_4762.GuideDxfModelCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4763
            
            return self._parent._cast(_4763.HypoidGearCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4765
            
            return self._parent._cast(_4765.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4767
            
            return self._parent._cast(_4767.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4769
            
            return self._parent._cast(_4769.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4770
            
            return self._parent._cast(_4770.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4772
            
            return self._parent._cast(_4772.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4773
            
            return self._parent._cast(_4773.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4775
            
            return self._parent._cast(_4775.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis)

        @property
        def mass_disc_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4776
            
            return self._parent._cast(_4776.MassDiscCompoundModalAnalysis)

        @property
        def measurement_component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4777
            
            return self._parent._cast(_4777.MeasurementComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4778
            
            return self._parent._cast(_4778.MountableComponentCompoundModalAnalysis)

        @property
        def oil_seal_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4779
            
            return self._parent._cast(_4779.OilSealCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4780
            
            return self._parent._cast(_4780.PartCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4781
            
            return self._parent._cast(_4781.PartToPartShearCouplingCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4783
            
            return self._parent._cast(_4783.PartToPartShearCouplingHalfCompoundModalAnalysis)

        @property
        def planetary_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4785
            
            return self._parent._cast(_4785.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def planet_carrier_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4786
            
            return self._parent._cast(_4786.PlanetCarrierCompoundModalAnalysis)

        @property
        def point_load_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4787
            
            return self._parent._cast(_4787.PointLoadCompoundModalAnalysis)

        @property
        def power_load_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4788
            
            return self._parent._cast(_4788.PowerLoadCompoundModalAnalysis)

        @property
        def pulley_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4789
            
            return self._parent._cast(_4789.PulleyCompoundModalAnalysis)

        @property
        def ring_pins_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4790
            
            return self._parent._cast(_4790.RingPinsCompoundModalAnalysis)

        @property
        def rolling_ring_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4792
            
            return self._parent._cast(_4792.RollingRingAssemblyCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4793
            
            return self._parent._cast(_4793.RollingRingCompoundModalAnalysis)

        @property
        def root_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4795
            
            return self._parent._cast(_4795.RootAssemblyCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4796
            
            return self._parent._cast(_4796.ShaftCompoundModalAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4797
            
            return self._parent._cast(_4797.ShaftHubConnectionCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4799
            
            return self._parent._cast(_4799.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4800
            
            return self._parent._cast(_4800.SpiralBevelGearCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4802
            
            return self._parent._cast(_4802.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def spring_damper_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4803
            
            return self._parent._cast(_4803.SpringDamperCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4805
            
            return self._parent._cast(_4805.SpringDamperHalfCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4806
            
            return self._parent._cast(_4806.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4808
            
            return self._parent._cast(_4808.StraightBevelDiffGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4809
            
            return self._parent._cast(_4809.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4811
            
            return self._parent._cast(_4811.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4812
            
            return self._parent._cast(_4812.StraightBevelPlanetGearCompoundModalAnalysis)

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4813
            
            return self._parent._cast(_4813.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def synchroniser_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4814
            
            return self._parent._cast(_4814.SynchroniserCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4815
            
            return self._parent._cast(_4815.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4816
            
            return self._parent._cast(_4816.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4817
            
            return self._parent._cast(_4817.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4818
            
            return self._parent._cast(_4818.TorqueConverterCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4820
            
            return self._parent._cast(_4820.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4821
            
            return self._parent._cast(_4821.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4822
            
            return self._parent._cast(_4822.UnbalancedMassCompoundModalAnalysis)

        @property
        def virtual_component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4823
            
            return self._parent._cast(_4823.VirtualComponentCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4824
            
            return self._parent._cast(_4824.WormGearCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4826
            
            return self._parent._cast(_4826.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4827
            
            return self._parent._cast(_4827.ZerolBevelGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4829
            
            return self._parent._cast(_4829.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4960
            
            return self._parent._cast(_4960.AbstractAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4961
            
            return self._parent._cast(_4961.AbstractShaftCompoundModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4962
            
            return self._parent._cast(_4962.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4964
            
            return self._parent._cast(_4964.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4966
            
            return self._parent._cast(_4966.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4967
            
            return self._parent._cast(_4967.AssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def bearing_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4968
            
            return self._parent._cast(_4968.BearingCompoundModalAnalysisAtAStiffness)

        @property
        def belt_drive_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4970
            
            return self._parent._cast(_4970.BeltDriveCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4971
            
            return self._parent._cast(_4971.BevelDifferentialGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4973
            
            return self._parent._cast(_4973.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4974
            
            return self._parent._cast(_4974.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4975
            
            return self._parent._cast(_4975.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4976
            
            return self._parent._cast(_4976.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4978
            
            return self._parent._cast(_4978.BevelGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def bolt_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4979
            
            return self._parent._cast(_4979.BoltCompoundModalAnalysisAtAStiffness)

        @property
        def bolted_joint_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4980
            
            return self._parent._cast(_4980.BoltedJointCompoundModalAnalysisAtAStiffness)

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4981
            
            return self._parent._cast(_4981.ClutchCompoundModalAnalysisAtAStiffness)

        @property
        def clutch_half_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4983
            
            return self._parent._cast(_4983.ClutchHalfCompoundModalAnalysisAtAStiffness)

        @property
        def component_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4985
            
            return self._parent._cast(_4985.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4986
            
            return self._parent._cast(_4986.ConceptCouplingCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4988
            
            return self._parent._cast(_4988.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness)

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4989
            
            return self._parent._cast(_4989.ConceptGearCompoundModalAnalysisAtAStiffness)

        @property
        def concept_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4991
            
            return self._parent._cast(_4991.ConceptGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4992
            
            return self._parent._cast(_4992.ConicalGearCompoundModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4994
            
            return self._parent._cast(_4994.ConicalGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def connector_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4996
            
            return self._parent._cast(_4996.ConnectorCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4997
            
            return self._parent._cast(_4997.CouplingCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4999
            
            return self._parent._cast(_4999.CouplingHalfCompoundModalAnalysisAtAStiffness)

        @property
        def cvt_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5001
            
            return self._parent._cast(_5001.CVTCompoundModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5002
            
            return self._parent._cast(_5002.CVTPulleyCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5003
            
            return self._parent._cast(_5003.CycloidalAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5005
            
            return self._parent._cast(_5005.CycloidalDiscCompoundModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5007
            
            return self._parent._cast(_5007.CylindricalGearCompoundModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5009
            
            return self._parent._cast(_5009.CylindricalGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5010
            
            return self._parent._cast(_5010.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness)

        @property
        def datum_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5011
            
            return self._parent._cast(_5011.DatumCompoundModalAnalysisAtAStiffness)

        @property
        def external_cad_model_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5012
            
            return self._parent._cast(_5012.ExternalCADModelCompoundModalAnalysisAtAStiffness)

        @property
        def face_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5013
            
            return self._parent._cast(_5013.FaceGearCompoundModalAnalysisAtAStiffness)

        @property
        def face_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5015
            
            return self._parent._cast(_5015.FaceGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def fe_part_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5016
            
            return self._parent._cast(_5016.FEPartCompoundModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5017
            
            return self._parent._cast(_5017.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5018
            
            return self._parent._cast(_5018.GearCompoundModalAnalysisAtAStiffness)

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5020
            
            return self._parent._cast(_5020.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5021
            
            return self._parent._cast(_5021.GuideDxfModelCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5022
            
            return self._parent._cast(_5022.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5024
            
            return self._parent._cast(_5024.HypoidGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5026
            
            return self._parent._cast(_5026.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5028
            
            return self._parent._cast(_5028.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5029
            
            return self._parent._cast(_5029.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5031
            
            return self._parent._cast(_5031.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5032
            
            return self._parent._cast(_5032.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5034
            
            return self._parent._cast(_5034.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def mass_disc_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5035
            
            return self._parent._cast(_5035.MassDiscCompoundModalAnalysisAtAStiffness)

        @property
        def measurement_component_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5036
            
            return self._parent._cast(_5036.MeasurementComponentCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5037
            
            return self._parent._cast(_5037.MountableComponentCompoundModalAnalysisAtAStiffness)

        @property
        def oil_seal_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5038
            
            return self._parent._cast(_5038.OilSealCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5039
            
            return self._parent._cast(_5039.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5040
            
            return self._parent._cast(_5040.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5042
            
            return self._parent._cast(_5042.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness)

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5044
            
            return self._parent._cast(_5044.PlanetaryGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def planet_carrier_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5045
            
            return self._parent._cast(_5045.PlanetCarrierCompoundModalAnalysisAtAStiffness)

        @property
        def point_load_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5046
            
            return self._parent._cast(_5046.PointLoadCompoundModalAnalysisAtAStiffness)

        @property
        def power_load_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5047
            
            return self._parent._cast(_5047.PowerLoadCompoundModalAnalysisAtAStiffness)

        @property
        def pulley_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5048
            
            return self._parent._cast(_5048.PulleyCompoundModalAnalysisAtAStiffness)

        @property
        def ring_pins_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5049
            
            return self._parent._cast(_5049.RingPinsCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5051
            
            return self._parent._cast(_5051.RollingRingAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5052
            
            return self._parent._cast(_5052.RollingRingCompoundModalAnalysisAtAStiffness)

        @property
        def root_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5054
            
            return self._parent._cast(_5054.RootAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5055
            
            return self._parent._cast(_5055.ShaftCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5056
            
            return self._parent._cast(_5056.ShaftHubConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5058
            
            return self._parent._cast(_5058.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5059
            
            return self._parent._cast(_5059.SpiralBevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5061
            
            return self._parent._cast(_5061.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5062
            
            return self._parent._cast(_5062.SpringDamperCompoundModalAnalysisAtAStiffness)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5064
            
            return self._parent._cast(_5064.SpringDamperHalfCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5065
            
            return self._parent._cast(_5065.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5067
            
            return self._parent._cast(_5067.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5068
            
            return self._parent._cast(_5068.StraightBevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5070
            
            return self._parent._cast(_5070.StraightBevelGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5071
            
            return self._parent._cast(_5071.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5072
            
            return self._parent._cast(_5072.StraightBevelSunGearCompoundModalAnalysisAtAStiffness)

        @property
        def synchroniser_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5073
            
            return self._parent._cast(_5073.SynchroniserCompoundModalAnalysisAtAStiffness)

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5074
            
            return self._parent._cast(_5074.SynchroniserHalfCompoundModalAnalysisAtAStiffness)

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5075
            
            return self._parent._cast(_5075.SynchroniserPartCompoundModalAnalysisAtAStiffness)

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5076
            
            return self._parent._cast(_5076.SynchroniserSleeveCompoundModalAnalysisAtAStiffness)

        @property
        def torque_converter_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5077
            
            return self._parent._cast(_5077.TorqueConverterCompoundModalAnalysisAtAStiffness)

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5079
            
            return self._parent._cast(_5079.TorqueConverterPumpCompoundModalAnalysisAtAStiffness)

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5080
            
            return self._parent._cast(_5080.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness)

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5081
            
            return self._parent._cast(_5081.UnbalancedMassCompoundModalAnalysisAtAStiffness)

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5082
            
            return self._parent._cast(_5082.VirtualComponentCompoundModalAnalysisAtAStiffness)

        @property
        def worm_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5083
            
            return self._parent._cast(_5083.WormGearCompoundModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5085
            
            return self._parent._cast(_5085.WormGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5086
            
            return self._parent._cast(_5086.ZerolBevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5088
            
            return self._parent._cast(_5088.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness)

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
        def part_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5297
            
            return self._parent._cast(_5297.PartCompoundModalAnalysisAtASpeed)

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
        def abstract_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5499
            
            return self._parent._cast(_5499.AbstractAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5500
            
            return self._parent._cast(_5500.AbstractShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5501
            
            return self._parent._cast(_5501.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5503
            
            return self._parent._cast(_5503.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5505
            
            return self._parent._cast(_5505.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5506
            
            return self._parent._cast(_5506.AssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def bearing_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5507
            
            return self._parent._cast(_5507.BearingCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_drive_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5509
            
            return self._parent._cast(_5509.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5510
            
            return self._parent._cast(_5510.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5512
            
            return self._parent._cast(_5512.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5513
            
            return self._parent._cast(_5513.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5514
            
            return self._parent._cast(_5514.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5515
            
            return self._parent._cast(_5515.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5517
            
            return self._parent._cast(_5517.BevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def bolt_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5518
            
            return self._parent._cast(_5518.BoltCompoundMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5519
            
            return self._parent._cast(_5519.BoltedJointCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5520
            
            return self._parent._cast(_5520.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5522
            
            return self._parent._cast(_5522.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5524
            
            return self._parent._cast(_5524.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5525
            
            return self._parent._cast(_5525.ConceptCouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5527
            
            return self._parent._cast(_5527.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5528
            
            return self._parent._cast(_5528.ConceptGearCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5530
            
            return self._parent._cast(_5530.ConceptGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5531
            
            return self._parent._cast(_5531.ConicalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5533
            
            return self._parent._cast(_5533.ConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def connector_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5535
            
            return self._parent._cast(_5535.ConnectorCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5536
            
            return self._parent._cast(_5536.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5538
            
            return self._parent._cast(_5538.CouplingHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5540
            
            return self._parent._cast(_5540.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5541
            
            return self._parent._cast(_5541.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5542
            
            return self._parent._cast(_5542.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5544
            
            return self._parent._cast(_5544.CycloidalDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5546
            
            return self._parent._cast(_5546.CylindricalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5548
            
            return self._parent._cast(_5548.CylindricalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5549
            
            return self._parent._cast(_5549.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis)

        @property
        def datum_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5550
            
            return self._parent._cast(_5550.DatumCompoundMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5551
            
            return self._parent._cast(_5551.ExternalCADModelCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5552
            
            return self._parent._cast(_5552.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5554
            
            return self._parent._cast(_5554.FaceGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def fe_part_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5555
            
            return self._parent._cast(_5555.FEPartCompoundMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5556
            
            return self._parent._cast(_5556.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5557
            
            return self._parent._cast(_5557.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5559
            
            return self._parent._cast(_5559.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5560
            
            return self._parent._cast(_5560.GuideDxfModelCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5561
            
            return self._parent._cast(_5561.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5563
            
            return self._parent._cast(_5563.HypoidGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5565
            
            return self._parent._cast(_5565.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5567
            
            return self._parent._cast(_5567.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5568
            
            return self._parent._cast(_5568.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5570
            
            return self._parent._cast(_5570.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5571
            
            return self._parent._cast(_5571.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5573
            
            return self._parent._cast(_5573.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def mass_disc_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5574
            
            return self._parent._cast(_5574.MassDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5575
            
            return self._parent._cast(_5575.MeasurementComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5576
            
            return self._parent._cast(_5576.MountableComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def oil_seal_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5577
            
            return self._parent._cast(_5577.OilSealCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5578
            
            return self._parent._cast(_5578.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5579
            
            return self._parent._cast(_5579.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5581
            
            return self._parent._cast(_5581.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5583
            
            return self._parent._cast(_5583.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def planet_carrier_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5584
            
            return self._parent._cast(_5584.PlanetCarrierCompoundMultibodyDynamicsAnalysis)

        @property
        def point_load_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5585
            
            return self._parent._cast(_5585.PointLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def power_load_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5586
            
            return self._parent._cast(_5586.PowerLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def pulley_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5587
            
            return self._parent._cast(_5587.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5588
            
            return self._parent._cast(_5588.RingPinsCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5590
            
            return self._parent._cast(_5590.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5591
            
            return self._parent._cast(_5591.RollingRingCompoundMultibodyDynamicsAnalysis)

        @property
        def root_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5593
            
            return self._parent._cast(_5593.RootAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5594
            
            return self._parent._cast(_5594.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5595
            
            return self._parent._cast(_5595.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5597
            
            return self._parent._cast(_5597.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5598
            
            return self._parent._cast(_5598.SpiralBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5600
            
            return self._parent._cast(_5600.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def spring_damper_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5601
            
            return self._parent._cast(_5601.SpringDamperCompoundMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5603
            
            return self._parent._cast(_5603.SpringDamperHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5604
            
            return self._parent._cast(_5604.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5606
            
            return self._parent._cast(_5606.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5607
            
            return self._parent._cast(_5607.StraightBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5609
            
            return self._parent._cast(_5609.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5610
            
            return self._parent._cast(_5610.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5611
            
            return self._parent._cast(_5611.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis)

        @property
        def synchroniser_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5612
            
            return self._parent._cast(_5612.SynchroniserCompoundMultibodyDynamicsAnalysis)

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5613
            
            return self._parent._cast(_5613.SynchroniserHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5614
            
            return self._parent._cast(_5614.SynchroniserPartCompoundMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5615
            
            return self._parent._cast(_5615.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis)

        @property
        def torque_converter_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5616
            
            return self._parent._cast(_5616.TorqueConverterCompoundMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5618
            
            return self._parent._cast(_5618.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis)

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5619
            
            return self._parent._cast(_5619.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis)

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5620
            
            return self._parent._cast(_5620.UnbalancedMassCompoundMultibodyDynamicsAnalysis)

        @property
        def virtual_component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5621
            
            return self._parent._cast(_5621.VirtualComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5622
            
            return self._parent._cast(_5622.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5624
            
            return self._parent._cast(_5624.WormGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5625
            
            return self._parent._cast(_5625.ZerolBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5627
            
            return self._parent._cast(_5627.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5846
            
            return self._parent._cast(_5846.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5847
            
            return self._parent._cast(_5847.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5848
            
            return self._parent._cast(_5848.AbstractShaftOrHousingCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5850
            
            return self._parent._cast(_5850.AGMAGleasonConicalGearCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5852
            
            return self._parent._cast(_5852.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis)

        @property
        def assembly_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5853
            
            return self._parent._cast(_5853.AssemblyCompoundHarmonicAnalysis)

        @property
        def bearing_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5854
            
            return self._parent._cast(_5854.BearingCompoundHarmonicAnalysis)

        @property
        def belt_drive_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5856
            
            return self._parent._cast(_5856.BeltDriveCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5857
            
            return self._parent._cast(_5857.BevelDifferentialGearCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5859
            
            return self._parent._cast(_5859.BevelDifferentialGearSetCompoundHarmonicAnalysis)

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
        def bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5864
            
            return self._parent._cast(_5864.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def bolt_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5865
            
            return self._parent._cast(_5865.BoltCompoundHarmonicAnalysis)

        @property
        def bolted_joint_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5866
            
            return self._parent._cast(_5866.BoltedJointCompoundHarmonicAnalysis)

        @property
        def clutch_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5867
            
            return self._parent._cast(_5867.ClutchCompoundHarmonicAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5869
            
            return self._parent._cast(_5869.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5871
            
            return self._parent._cast(_5871.ComponentCompoundHarmonicAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5872
            
            return self._parent._cast(_5872.ConceptCouplingCompoundHarmonicAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5874
            
            return self._parent._cast(_5874.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def concept_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5875
            
            return self._parent._cast(_5875.ConceptGearCompoundHarmonicAnalysis)

        @property
        def concept_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5877
            
            return self._parent._cast(_5877.ConceptGearSetCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5878
            
            return self._parent._cast(_5878.ConicalGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5880
            
            return self._parent._cast(_5880.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def connector_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5882
            
            return self._parent._cast(_5882.ConnectorCompoundHarmonicAnalysis)

        @property
        def coupling_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5883
            
            return self._parent._cast(_5883.CouplingCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5885
            
            return self._parent._cast(_5885.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5887
            
            return self._parent._cast(_5887.CVTCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5888
            
            return self._parent._cast(_5888.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def cycloidal_assembly_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5889
            
            return self._parent._cast(_5889.CycloidalAssemblyCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5891
            
            return self._parent._cast(_5891.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5893
            
            return self._parent._cast(_5893.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5895
            
            return self._parent._cast(_5895.CylindricalGearSetCompoundHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5896
            
            return self._parent._cast(_5896.CylindricalPlanetGearCompoundHarmonicAnalysis)

        @property
        def datum_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5897
            
            return self._parent._cast(_5897.DatumCompoundHarmonicAnalysis)

        @property
        def external_cad_model_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5898
            
            return self._parent._cast(_5898.ExternalCADModelCompoundHarmonicAnalysis)

        @property
        def face_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5899
            
            return self._parent._cast(_5899.FaceGearCompoundHarmonicAnalysis)

        @property
        def face_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5901
            
            return self._parent._cast(_5901.FaceGearSetCompoundHarmonicAnalysis)

        @property
        def fe_part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5902
            
            return self._parent._cast(_5902.FEPartCompoundHarmonicAnalysis)

        @property
        def flexible_pin_assembly_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5903
            
            return self._parent._cast(_5903.FlexiblePinAssemblyCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5904
            
            return self._parent._cast(_5904.GearCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5906
            
            return self._parent._cast(_5906.GearSetCompoundHarmonicAnalysis)

        @property
        def guide_dxf_model_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5907
            
            return self._parent._cast(_5907.GuideDxfModelCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5908
            
            return self._parent._cast(_5908.HypoidGearCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5910
            
            return self._parent._cast(_5910.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5912
            
            return self._parent._cast(_5912.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5914
            
            return self._parent._cast(_5914.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5915
            
            return self._parent._cast(_5915.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5917
            
            return self._parent._cast(_5917.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5918
            
            return self._parent._cast(_5918.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5920
            
            return self._parent._cast(_5920.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def mass_disc_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5921
            
            return self._parent._cast(_5921.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5922
            
            return self._parent._cast(_5922.MeasurementComponentCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5923
            
            return self._parent._cast(_5923.MountableComponentCompoundHarmonicAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5924
            
            return self._parent._cast(_5924.OilSealCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5925
            
            return self._parent._cast(_5925.PartCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5926
            
            return self._parent._cast(_5926.PartToPartShearCouplingCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5928
            
            return self._parent._cast(_5928.PartToPartShearCouplingHalfCompoundHarmonicAnalysis)

        @property
        def planetary_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5930
            
            return self._parent._cast(_5930.PlanetaryGearSetCompoundHarmonicAnalysis)

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
        def rolling_ring_assembly_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5937
            
            return self._parent._cast(_5937.RollingRingAssemblyCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5938
            
            return self._parent._cast(_5938.RollingRingCompoundHarmonicAnalysis)

        @property
        def root_assembly_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5940
            
            return self._parent._cast(_5940.RootAssemblyCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5941
            
            return self._parent._cast(_5941.ShaftCompoundHarmonicAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5942
            
            return self._parent._cast(_5942.ShaftHubConnectionCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5944
            
            return self._parent._cast(_5944.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5945
            
            return self._parent._cast(_5945.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5947
            
            return self._parent._cast(_5947.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def spring_damper_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5948
            
            return self._parent._cast(_5948.SpringDamperCompoundHarmonicAnalysis)

        @property
        def spring_damper_half_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5950
            
            return self._parent._cast(_5950.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5951
            
            return self._parent._cast(_5951.StraightBevelDiffGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5953
            
            return self._parent._cast(_5953.StraightBevelDiffGearSetCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5954
            
            return self._parent._cast(_5954.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5956
            
            return self._parent._cast(_5956.StraightBevelGearSetCompoundHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5957
            
            return self._parent._cast(_5957.StraightBevelPlanetGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5958
            
            return self._parent._cast(_5958.StraightBevelSunGearCompoundHarmonicAnalysis)

        @property
        def synchroniser_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5959
            
            return self._parent._cast(_5959.SynchroniserCompoundHarmonicAnalysis)

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
        def torque_converter_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5963
            
            return self._parent._cast(_5963.TorqueConverterCompoundHarmonicAnalysis)

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
        def worm_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5971
            
            return self._parent._cast(_5971.WormGearSetCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5972
            
            return self._parent._cast(_5972.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5974
            
            return self._parent._cast(_5974.ZerolBevelGearSetCompoundHarmonicAnalysis)

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
        def part_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6184
            
            return self._parent._cast(_6184.PartCompoundHarmonicAnalysisOfSingleExcitation)

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
        def abstract_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6373
            
            return self._parent._cast(_6373.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_shaft_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6374
            
            return self._parent._cast(_6374.AbstractShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6375
            
            return self._parent._cast(_6375.AbstractShaftOrHousingCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6377
            
            return self._parent._cast(_6377.AGMAGleasonConicalGearCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6379
            
            return self._parent._cast(_6379.AGMAGleasonConicalGearSetCompoundDynamicAnalysis)

        @property
        def assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6380
            
            return self._parent._cast(_6380.AssemblyCompoundDynamicAnalysis)

        @property
        def bearing_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6381
            
            return self._parent._cast(_6381.BearingCompoundDynamicAnalysis)

        @property
        def belt_drive_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6383
            
            return self._parent._cast(_6383.BeltDriveCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6384
            
            return self._parent._cast(_6384.BevelDifferentialGearCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6386
            
            return self._parent._cast(_6386.BevelDifferentialGearSetCompoundDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6387
            
            return self._parent._cast(_6387.BevelDifferentialPlanetGearCompoundDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6388
            
            return self._parent._cast(_6388.BevelDifferentialSunGearCompoundDynamicAnalysis)

        @property
        def bevel_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6389
            
            return self._parent._cast(_6389.BevelGearCompoundDynamicAnalysis)

        @property
        def bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6391
            
            return self._parent._cast(_6391.BevelGearSetCompoundDynamicAnalysis)

        @property
        def bolt_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6392
            
            return self._parent._cast(_6392.BoltCompoundDynamicAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6393
            
            return self._parent._cast(_6393.BoltedJointCompoundDynamicAnalysis)

        @property
        def clutch_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6394
            
            return self._parent._cast(_6394.ClutchCompoundDynamicAnalysis)

        @property
        def clutch_half_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6396
            
            return self._parent._cast(_6396.ClutchHalfCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6398
            
            return self._parent._cast(_6398.ComponentCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6399
            
            return self._parent._cast(_6399.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def concept_coupling_half_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6401
            
            return self._parent._cast(_6401.ConceptCouplingHalfCompoundDynamicAnalysis)

        @property
        def concept_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6402
            
            return self._parent._cast(_6402.ConceptGearCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6404
            
            return self._parent._cast(_6404.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6405
            
            return self._parent._cast(_6405.ConicalGearCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6407
            
            return self._parent._cast(_6407.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def connector_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6409
            
            return self._parent._cast(_6409.ConnectorCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6410
            
            return self._parent._cast(_6410.CouplingCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6412
            
            return self._parent._cast(_6412.CouplingHalfCompoundDynamicAnalysis)

        @property
        def cvt_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6414
            
            return self._parent._cast(_6414.CVTCompoundDynamicAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6415
            
            return self._parent._cast(_6415.CVTPulleyCompoundDynamicAnalysis)

        @property
        def cycloidal_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6416
            
            return self._parent._cast(_6416.CycloidalAssemblyCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6418
            
            return self._parent._cast(_6418.CycloidalDiscCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6420
            
            return self._parent._cast(_6420.CylindricalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6422
            
            return self._parent._cast(_6422.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6423
            
            return self._parent._cast(_6423.CylindricalPlanetGearCompoundDynamicAnalysis)

        @property
        def datum_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6424
            
            return self._parent._cast(_6424.DatumCompoundDynamicAnalysis)

        @property
        def external_cad_model_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6425
            
            return self._parent._cast(_6425.ExternalCADModelCompoundDynamicAnalysis)

        @property
        def face_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6426
            
            return self._parent._cast(_6426.FaceGearCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6428
            
            return self._parent._cast(_6428.FaceGearSetCompoundDynamicAnalysis)

        @property
        def fe_part_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6429
            
            return self._parent._cast(_6429.FEPartCompoundDynamicAnalysis)

        @property
        def flexible_pin_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6430
            
            return self._parent._cast(_6430.FlexiblePinAssemblyCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6431
            
            return self._parent._cast(_6431.GearCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6433
            
            return self._parent._cast(_6433.GearSetCompoundDynamicAnalysis)

        @property
        def guide_dxf_model_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6434
            
            return self._parent._cast(_6434.GuideDxfModelCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6435
            
            return self._parent._cast(_6435.HypoidGearCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6437
            
            return self._parent._cast(_6437.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6439
            
            return self._parent._cast(_6439.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6441
            
            return self._parent._cast(_6441.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6442
            
            return self._parent._cast(_6442.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6444
            
            return self._parent._cast(_6444.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6445
            
            return self._parent._cast(_6445.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6447
            
            return self._parent._cast(_6447.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def mass_disc_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6448
            
            return self._parent._cast(_6448.MassDiscCompoundDynamicAnalysis)

        @property
        def measurement_component_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6449
            
            return self._parent._cast(_6449.MeasurementComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6450
            
            return self._parent._cast(_6450.MountableComponentCompoundDynamicAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6451
            
            return self._parent._cast(_6451.OilSealCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6452
            
            return self._parent._cast(_6452.PartCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6453
            
            return self._parent._cast(_6453.PartToPartShearCouplingCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6455
            
            return self._parent._cast(_6455.PartToPartShearCouplingHalfCompoundDynamicAnalysis)

        @property
        def planetary_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6457
            
            return self._parent._cast(_6457.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def planet_carrier_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6458
            
            return self._parent._cast(_6458.PlanetCarrierCompoundDynamicAnalysis)

        @property
        def point_load_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6459
            
            return self._parent._cast(_6459.PointLoadCompoundDynamicAnalysis)

        @property
        def power_load_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6460
            
            return self._parent._cast(_6460.PowerLoadCompoundDynamicAnalysis)

        @property
        def pulley_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6461
            
            return self._parent._cast(_6461.PulleyCompoundDynamicAnalysis)

        @property
        def ring_pins_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6462
            
            return self._parent._cast(_6462.RingPinsCompoundDynamicAnalysis)

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6464
            
            return self._parent._cast(_6464.RollingRingAssemblyCompoundDynamicAnalysis)

        @property
        def rolling_ring_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6465
            
            return self._parent._cast(_6465.RollingRingCompoundDynamicAnalysis)

        @property
        def root_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6467
            
            return self._parent._cast(_6467.RootAssemblyCompoundDynamicAnalysis)

        @property
        def shaft_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6468
            
            return self._parent._cast(_6468.ShaftCompoundDynamicAnalysis)

        @property
        def shaft_hub_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6469
            
            return self._parent._cast(_6469.ShaftHubConnectionCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6471
            
            return self._parent._cast(_6471.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6472
            
            return self._parent._cast(_6472.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6474
            
            return self._parent._cast(_6474.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6475
            
            return self._parent._cast(_6475.SpringDamperCompoundDynamicAnalysis)

        @property
        def spring_damper_half_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6477
            
            return self._parent._cast(_6477.SpringDamperHalfCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6478
            
            return self._parent._cast(_6478.StraightBevelDiffGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6480
            
            return self._parent._cast(_6480.StraightBevelDiffGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6481
            
            return self._parent._cast(_6481.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6483
            
            return self._parent._cast(_6483.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6484
            
            return self._parent._cast(_6484.StraightBevelPlanetGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6485
            
            return self._parent._cast(_6485.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def synchroniser_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6486
            
            return self._parent._cast(_6486.SynchroniserCompoundDynamicAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6487
            
            return self._parent._cast(_6487.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6488
            
            return self._parent._cast(_6488.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6489
            
            return self._parent._cast(_6489.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6490
            
            return self._parent._cast(_6490.TorqueConverterCompoundDynamicAnalysis)

        @property
        def torque_converter_pump_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6492
            
            return self._parent._cast(_6492.TorqueConverterPumpCompoundDynamicAnalysis)

        @property
        def torque_converter_turbine_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6493
            
            return self._parent._cast(_6493.TorqueConverterTurbineCompoundDynamicAnalysis)

        @property
        def unbalanced_mass_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6494
            
            return self._parent._cast(_6494.UnbalancedMassCompoundDynamicAnalysis)

        @property
        def virtual_component_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6495
            
            return self._parent._cast(_6495.VirtualComponentCompoundDynamicAnalysis)

        @property
        def worm_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6496
            
            return self._parent._cast(_6496.WormGearCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6498
            
            return self._parent._cast(_6498.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6499
            
            return self._parent._cast(_6499.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6501
            
            return self._parent._cast(_6501.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6639
            
            return self._parent._cast(_6639.AbstractAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6640
            
            return self._parent._cast(_6640.AbstractShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6641
            
            return self._parent._cast(_6641.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6643
            
            return self._parent._cast(_6643.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6645
            
            return self._parent._cast(_6645.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6646
            
            return self._parent._cast(_6646.AssemblyCompoundCriticalSpeedAnalysis)

        @property
        def bearing_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6647
            
            return self._parent._cast(_6647.BearingCompoundCriticalSpeedAnalysis)

        @property
        def belt_drive_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6649
            
            return self._parent._cast(_6649.BeltDriveCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6650
            
            return self._parent._cast(_6650.BevelDifferentialGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6652
            
            return self._parent._cast(_6652.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6653
            
            return self._parent._cast(_6653.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6654
            
            return self._parent._cast(_6654.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6655
            
            return self._parent._cast(_6655.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6657
            
            return self._parent._cast(_6657.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def bolt_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6658
            
            return self._parent._cast(_6658.BoltCompoundCriticalSpeedAnalysis)

        @property
        def bolted_joint_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6659
            
            return self._parent._cast(_6659.BoltedJointCompoundCriticalSpeedAnalysis)

        @property
        def clutch_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6660
            
            return self._parent._cast(_6660.ClutchCompoundCriticalSpeedAnalysis)

        @property
        def clutch_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6662
            
            return self._parent._cast(_6662.ClutchHalfCompoundCriticalSpeedAnalysis)

        @property
        def component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6664
            
            return self._parent._cast(_6664.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6665
            
            return self._parent._cast(_6665.ConceptCouplingCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6667
            
            return self._parent._cast(_6667.ConceptCouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6668
            
            return self._parent._cast(_6668.ConceptGearCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6670
            
            return self._parent._cast(_6670.ConceptGearSetCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6671
            
            return self._parent._cast(_6671.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6673
            
            return self._parent._cast(_6673.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def connector_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6675
            
            return self._parent._cast(_6675.ConnectorCompoundCriticalSpeedAnalysis)

        @property
        def coupling_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6676
            
            return self._parent._cast(_6676.CouplingCompoundCriticalSpeedAnalysis)

        @property
        def coupling_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6678
            
            return self._parent._cast(_6678.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def cvt_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6680
            
            return self._parent._cast(_6680.CVTCompoundCriticalSpeedAnalysis)

        @property
        def cvt_pulley_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6681
            
            return self._parent._cast(_6681.CVTPulleyCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6682
            
            return self._parent._cast(_6682.CycloidalAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6684
            
            return self._parent._cast(_6684.CycloidalDiscCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6686
            
            return self._parent._cast(_6686.CylindricalGearCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6688
            
            return self._parent._cast(_6688.CylindricalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6689
            
            return self._parent._cast(_6689.CylindricalPlanetGearCompoundCriticalSpeedAnalysis)

        @property
        def datum_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6690
            
            return self._parent._cast(_6690.DatumCompoundCriticalSpeedAnalysis)

        @property
        def external_cad_model_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6691
            
            return self._parent._cast(_6691.ExternalCADModelCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6692
            
            return self._parent._cast(_6692.FaceGearCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6694
            
            return self._parent._cast(_6694.FaceGearSetCompoundCriticalSpeedAnalysis)

        @property
        def fe_part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6695
            
            return self._parent._cast(_6695.FEPartCompoundCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6696
            
            return self._parent._cast(_6696.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6697
            
            return self._parent._cast(_6697.GearCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6699
            
            return self._parent._cast(_6699.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6700
            
            return self._parent._cast(_6700.GuideDxfModelCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6701
            
            return self._parent._cast(_6701.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6703
            
            return self._parent._cast(_6703.HypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6705
            
            return self._parent._cast(_6705.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6707
            
            return self._parent._cast(_6707.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6708
            
            return self._parent._cast(_6708.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6710
            
            return self._parent._cast(_6710.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6711
            
            return self._parent._cast(_6711.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6713
            
            return self._parent._cast(_6713.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def mass_disc_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6714
            
            return self._parent._cast(_6714.MassDiscCompoundCriticalSpeedAnalysis)

        @property
        def measurement_component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6715
            
            return self._parent._cast(_6715.MeasurementComponentCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6716
            
            return self._parent._cast(_6716.MountableComponentCompoundCriticalSpeedAnalysis)

        @property
        def oil_seal_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6717
            
            return self._parent._cast(_6717.OilSealCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6718
            
            return self._parent._cast(_6718.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6719
            
            return self._parent._cast(_6719.PartToPartShearCouplingCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6721
            
            return self._parent._cast(_6721.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def planetary_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6723
            
            return self._parent._cast(_6723.PlanetaryGearSetCompoundCriticalSpeedAnalysis)

        @property
        def planet_carrier_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6724
            
            return self._parent._cast(_6724.PlanetCarrierCompoundCriticalSpeedAnalysis)

        @property
        def point_load_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6725
            
            return self._parent._cast(_6725.PointLoadCompoundCriticalSpeedAnalysis)

        @property
        def power_load_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6726
            
            return self._parent._cast(_6726.PowerLoadCompoundCriticalSpeedAnalysis)

        @property
        def pulley_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6727
            
            return self._parent._cast(_6727.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def ring_pins_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6728
            
            return self._parent._cast(_6728.RingPinsCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6730
            
            return self._parent._cast(_6730.RollingRingAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6731
            
            return self._parent._cast(_6731.RollingRingCompoundCriticalSpeedAnalysis)

        @property
        def root_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6733
            
            return self._parent._cast(_6733.RootAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def shaft_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6734
            
            return self._parent._cast(_6734.ShaftCompoundCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6735
            
            return self._parent._cast(_6735.ShaftHubConnectionCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6737
            
            return self._parent._cast(_6737.SpecialisedAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6738
            
            return self._parent._cast(_6738.SpiralBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6740
            
            return self._parent._cast(_6740.SpiralBevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6741
            
            return self._parent._cast(_6741.SpringDamperCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6743
            
            return self._parent._cast(_6743.SpringDamperHalfCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6744
            
            return self._parent._cast(_6744.StraightBevelDiffGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6746
            
            return self._parent._cast(_6746.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6747
            
            return self._parent._cast(_6747.StraightBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6749
            
            return self._parent._cast(_6749.StraightBevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6750
            
            return self._parent._cast(_6750.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6751
            
            return self._parent._cast(_6751.StraightBevelSunGearCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6752
            
            return self._parent._cast(_6752.SynchroniserCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_half_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6753
            
            return self._parent._cast(_6753.SynchroniserHalfCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6754
            
            return self._parent._cast(_6754.SynchroniserPartCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6755
            
            return self._parent._cast(_6755.SynchroniserSleeveCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6756
            
            return self._parent._cast(_6756.TorqueConverterCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6758
            
            return self._parent._cast(_6758.TorqueConverterPumpCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6759
            
            return self._parent._cast(_6759.TorqueConverterTurbineCompoundCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6760
            
            return self._parent._cast(_6760.UnbalancedMassCompoundCriticalSpeedAnalysis)

        @property
        def virtual_component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6761
            
            return self._parent._cast(_6761.VirtualComponentCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6762
            
            return self._parent._cast(_6762.WormGearCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6764
            
            return self._parent._cast(_6764.WormGearSetCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6765
            
            return self._parent._cast(_6765.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6767
            
            return self._parent._cast(_6767.ZerolBevelGearSetCompoundCriticalSpeedAnalysis)

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
        def part_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7182
            
            return self._parent._cast(_7182.PartCompoundAdvancedTimeSteppingAnalysisForModulation)

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
        def abstract_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7368
            
            return self._parent._cast(_7368.AbstractAssemblyCompoundAdvancedSystemDeflection)

        @property
        def abstract_shaft_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7369
            
            return self._parent._cast(_7369.AbstractShaftCompoundAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7370
            
            return self._parent._cast(_7370.AbstractShaftOrHousingCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7372
            
            return self._parent._cast(_7372.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7374
            
            return self._parent._cast(_7374.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection)

        @property
        def assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7375
            
            return self._parent._cast(_7375.AssemblyCompoundAdvancedSystemDeflection)

        @property
        def bearing_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7376
            
            return self._parent._cast(_7376.BearingCompoundAdvancedSystemDeflection)

        @property
        def belt_drive_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7378
            
            return self._parent._cast(_7378.BeltDriveCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7379
            
            return self._parent._cast(_7379.BevelDifferentialGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7381
            
            return self._parent._cast(_7381.BevelDifferentialGearSetCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7382
            
            return self._parent._cast(_7382.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7383
            
            return self._parent._cast(_7383.BevelDifferentialSunGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7384
            
            return self._parent._cast(_7384.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7386
            
            return self._parent._cast(_7386.BevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def bolt_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7387
            
            return self._parent._cast(_7387.BoltCompoundAdvancedSystemDeflection)

        @property
        def bolted_joint_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7388
            
            return self._parent._cast(_7388.BoltedJointCompoundAdvancedSystemDeflection)

        @property
        def clutch_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7389
            
            return self._parent._cast(_7389.ClutchCompoundAdvancedSystemDeflection)

        @property
        def clutch_half_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7391
            
            return self._parent._cast(_7391.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7393
            
            return self._parent._cast(_7393.ComponentCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7394
            
            return self._parent._cast(_7394.ConceptCouplingCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_half_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7396
            
            return self._parent._cast(_7396.ConceptCouplingHalfCompoundAdvancedSystemDeflection)

        @property
        def concept_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7397
            
            return self._parent._cast(_7397.ConceptGearCompoundAdvancedSystemDeflection)

        @property
        def concept_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7399
            
            return self._parent._cast(_7399.ConceptGearSetCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7400
            
            return self._parent._cast(_7400.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7402
            
            return self._parent._cast(_7402.ConicalGearSetCompoundAdvancedSystemDeflection)

        @property
        def connector_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7404
            
            return self._parent._cast(_7404.ConnectorCompoundAdvancedSystemDeflection)

        @property
        def coupling_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7405
            
            return self._parent._cast(_7405.CouplingCompoundAdvancedSystemDeflection)

        @property
        def coupling_half_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7407
            
            return self._parent._cast(_7407.CouplingHalfCompoundAdvancedSystemDeflection)

        @property
        def cvt_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7409
            
            return self._parent._cast(_7409.CVTCompoundAdvancedSystemDeflection)

        @property
        def cvt_pulley_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7410
            
            return self._parent._cast(_7410.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7411
            
            return self._parent._cast(_7411.CycloidalAssemblyCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_disc_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7413
            
            return self._parent._cast(_7413.CycloidalDiscCompoundAdvancedSystemDeflection)

        @property
        def cylindrical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7415
            
            return self._parent._cast(_7415.CylindricalGearCompoundAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7417
            
            return self._parent._cast(_7417.CylindricalGearSetCompoundAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7418
            
            return self._parent._cast(_7418.CylindricalPlanetGearCompoundAdvancedSystemDeflection)

        @property
        def datum_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7419
            
            return self._parent._cast(_7419.DatumCompoundAdvancedSystemDeflection)

        @property
        def external_cad_model_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7420
            
            return self._parent._cast(_7420.ExternalCADModelCompoundAdvancedSystemDeflection)

        @property
        def face_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7421
            
            return self._parent._cast(_7421.FaceGearCompoundAdvancedSystemDeflection)

        @property
        def face_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7423
            
            return self._parent._cast(_7423.FaceGearSetCompoundAdvancedSystemDeflection)

        @property
        def fe_part_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7424
            
            return self._parent._cast(_7424.FEPartCompoundAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7425
            
            return self._parent._cast(_7425.FlexiblePinAssemblyCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7426
            
            return self._parent._cast(_7426.GearCompoundAdvancedSystemDeflection)

        @property
        def gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7428
            
            return self._parent._cast(_7428.GearSetCompoundAdvancedSystemDeflection)

        @property
        def guide_dxf_model_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7429
            
            return self._parent._cast(_7429.GuideDxfModelCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7430
            
            return self._parent._cast(_7430.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7432
            
            return self._parent._cast(_7432.HypoidGearSetCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7434
            
            return self._parent._cast(_7434.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7436
            
            return self._parent._cast(_7436.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7437
            
            return self._parent._cast(_7437.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7439
            
            return self._parent._cast(_7439.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7440
            
            return self._parent._cast(_7440.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7442
            
            return self._parent._cast(_7442.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def mass_disc_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7443
            
            return self._parent._cast(_7443.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7444
            
            return self._parent._cast(_7444.MeasurementComponentCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7445
            
            return self._parent._cast(_7445.MountableComponentCompoundAdvancedSystemDeflection)

        @property
        def oil_seal_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7446
            
            return self._parent._cast(_7446.OilSealCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7447
            
            return self._parent._cast(_7447.PartCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7448
            
            return self._parent._cast(_7448.PartToPartShearCouplingCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7450
            
            return self._parent._cast(_7450.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection)

        @property
        def planetary_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7452
            
            return self._parent._cast(_7452.PlanetaryGearSetCompoundAdvancedSystemDeflection)

        @property
        def planet_carrier_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7453
            
            return self._parent._cast(_7453.PlanetCarrierCompoundAdvancedSystemDeflection)

        @property
        def point_load_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7454
            
            return self._parent._cast(_7454.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7455
            
            return self._parent._cast(_7455.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def pulley_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7456
            
            return self._parent._cast(_7456.PulleyCompoundAdvancedSystemDeflection)

        @property
        def ring_pins_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7457
            
            return self._parent._cast(_7457.RingPinsCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7459
            
            return self._parent._cast(_7459.RollingRingAssemblyCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7460
            
            return self._parent._cast(_7460.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def root_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7462
            
            return self._parent._cast(_7462.RootAssemblyCompoundAdvancedSystemDeflection)

        @property
        def shaft_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7463
            
            return self._parent._cast(_7463.ShaftCompoundAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7464
            
            return self._parent._cast(_7464.ShaftHubConnectionCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7466
            
            return self._parent._cast(_7466.SpecialisedAssemblyCompoundAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7467
            
            return self._parent._cast(_7467.SpiralBevelGearCompoundAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7469
            
            return self._parent._cast(_7469.SpiralBevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def spring_damper_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7470
            
            return self._parent._cast(_7470.SpringDamperCompoundAdvancedSystemDeflection)

        @property
        def spring_damper_half_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7472
            
            return self._parent._cast(_7472.SpringDamperHalfCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7473
            
            return self._parent._cast(_7473.StraightBevelDiffGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7475
            
            return self._parent._cast(_7475.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7476
            
            return self._parent._cast(_7476.StraightBevelGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7478
            
            return self._parent._cast(_7478.StraightBevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7479
            
            return self._parent._cast(_7479.StraightBevelPlanetGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7480
            
            return self._parent._cast(_7480.StraightBevelSunGearCompoundAdvancedSystemDeflection)

        @property
        def synchroniser_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7481
            
            return self._parent._cast(_7481.SynchroniserCompoundAdvancedSystemDeflection)

        @property
        def synchroniser_half_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7482
            
            return self._parent._cast(_7482.SynchroniserHalfCompoundAdvancedSystemDeflection)

        @property
        def synchroniser_part_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7483
            
            return self._parent._cast(_7483.SynchroniserPartCompoundAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7484
            
            return self._parent._cast(_7484.SynchroniserSleeveCompoundAdvancedSystemDeflection)

        @property
        def torque_converter_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7485
            
            return self._parent._cast(_7485.TorqueConverterCompoundAdvancedSystemDeflection)

        @property
        def torque_converter_pump_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7487
            
            return self._parent._cast(_7487.TorqueConverterPumpCompoundAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7488
            
            return self._parent._cast(_7488.TorqueConverterTurbineCompoundAdvancedSystemDeflection)

        @property
        def unbalanced_mass_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7489
            
            return self._parent._cast(_7489.UnbalancedMassCompoundAdvancedSystemDeflection)

        @property
        def virtual_component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7490
            
            return self._parent._cast(_7490.VirtualComponentCompoundAdvancedSystemDeflection)

        @property
        def worm_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7491
            
            return self._parent._cast(_7491.WormGearCompoundAdvancedSystemDeflection)

        @property
        def worm_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7493
            
            return self._parent._cast(_7493.WormGearSetCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7494
            
            return self._parent._cast(_7494.ZerolBevelGearCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7496
            
            return self._parent._cast(_7496.ZerolBevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(self) -> 'PartCompoundAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartCompoundAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing(self) -> 'Image':
        """Image: 'TwoDDrawing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TwoDDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def cast_to(self) -> 'PartCompoundAnalysis._Cast_PartCompoundAnalysis':
        return self._Cast_PartCompoundAnalysis(self)
