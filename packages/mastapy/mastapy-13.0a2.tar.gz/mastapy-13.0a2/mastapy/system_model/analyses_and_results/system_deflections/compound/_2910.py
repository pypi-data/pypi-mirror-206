"""_2910.py

PartCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2764
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'PartCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundSystemDeflection',)


class PartCompoundSystemDeflection(_7508.PartCompoundAnalysis):
    """PartCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_PartCompoundSystemDeflection:
        """Special nested class for casting PartCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'PartCompoundSystemDeflection'):
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
        def part_compound_system_deflection(self) -> 'PartCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_2764.PartSystemDeflection]':
        """List[PartSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_2764.PartSystemDeflection]':
        """List[PartSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection':
        return self._Cast_PartCompoundSystemDeflection(self)
