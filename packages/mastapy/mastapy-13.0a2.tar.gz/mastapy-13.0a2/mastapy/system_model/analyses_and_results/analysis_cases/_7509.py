"""_7509.py

PartFEAnalysis
"""
from mastapy.system_model.analyses_and_results.analysis_cases import _7510
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_FE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'PartFEAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartFEAnalysis',)


class PartFEAnalysis(_7510.PartStaticLoadAnalysisCase):
    """PartFEAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_FE_ANALYSIS

    class _Cast_PartFEAnalysis:
        """Special nested class for casting PartFEAnalysis to subclasses."""

        def __init__(self, parent: 'PartFEAnalysis'):
            self._parent = parent

        @property
        def part_static_load_analysis_case(self):
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
        def abstract_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2664
            
            return self._parent._cast(_2664.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2665
            
            return self._parent._cast(_2665.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2666
            
            return self._parent._cast(_2666.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2669
            
            return self._parent._cast(_2669.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2670
            
            return self._parent._cast(_2670.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2671
            
            return self._parent._cast(_2671.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2677
            
            return self._parent._cast(_2677.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2679
            
            return self._parent._cast(_2679.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2681
            
            return self._parent._cast(_2681.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2682
            
            return self._parent._cast(_2682.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2683
            
            return self._parent._cast(_2683.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2684
            
            return self._parent._cast(_2684.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2686
            
            return self._parent._cast(_2686.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2687
            
            return self._parent._cast(_2687.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2688
            
            return self._parent._cast(_2688.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2689
            
            return self._parent._cast(_2689.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2691
            
            return self._parent._cast(_2691.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2692
            
            return self._parent._cast(_2692.ClutchSystemDeflection)

        @property
        def component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2694
            
            return self._parent._cast(_2694.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2697
            
            return self._parent._cast(_2697.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2698
            
            return self._parent._cast(_2698.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2700
            
            return self._parent._cast(_2700.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2701
            
            return self._parent._cast(_2701.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2704
            
            return self._parent._cast(_2704.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2705
            
            return self._parent._cast(_2705.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2707
            
            return self._parent._cast(_2707.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2709
            
            return self._parent._cast(_2709.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2710
            
            return self._parent._cast(_2710.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2712
            
            return self._parent._cast(_2712.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2713
            
            return self._parent._cast(_2713.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2714
            
            return self._parent._cast(_2714.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2717
            
            return self._parent._cast(_2717.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2721
            
            return self._parent._cast(_2721.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2722
            
            return self._parent._cast(_2722.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2723
            
            return self._parent._cast(_2723.CylindricalGearSetSystemDeflectionWithLTCAResults)

        @property
        def cylindrical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2724
            
            return self._parent._cast(_2724.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2725
            
            return self._parent._cast(_2725.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2726
            
            return self._parent._cast(_2726.CylindricalGearSystemDeflectionWithLTCAResults)

        @property
        def cylindrical_planet_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2729
            
            return self._parent._cast(_2729.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2730
            
            return self._parent._cast(_2730.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2731
            
            return self._parent._cast(_2731.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2734
            
            return self._parent._cast(_2734.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2735
            
            return self._parent._cast(_2735.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2736
            
            return self._parent._cast(_2736.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2737
            
            return self._parent._cast(_2737.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2739
            
            return self._parent._cast(_2739.GearSetSystemDeflection)

        @property
        def gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2740
            
            return self._parent._cast(_2740.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2741
            
            return self._parent._cast(_2741.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2743
            
            return self._parent._cast(_2743.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2744
            
            return self._parent._cast(_2744.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2748
            
            return self._parent._cast(_2748.KlingelnbergCycloPalloidConicalGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2749
            
            return self._parent._cast(_2749.KlingelnbergCycloPalloidConicalGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2751
            
            return self._parent._cast(_2751.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2752
            
            return self._parent._cast(_2752.KlingelnbergCycloPalloidHypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2754
            
            return self._parent._cast(_2754.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2755
            
            return self._parent._cast(_2755.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection)

        @property
        def mass_disc_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2758
            
            return self._parent._cast(_2758.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2759
            
            return self._parent._cast(_2759.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2761
            
            return self._parent._cast(_2761.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2763
            
            return self._parent._cast(_2763.OilSealSystemDeflection)

        @property
        def part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2764
            
            return self._parent._cast(_2764.PartSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2766
            
            return self._parent._cast(_2766.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2767
            
            return self._parent._cast(_2767.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2769
            
            return self._parent._cast(_2769.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2770
            
            return self._parent._cast(_2770.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2771
            
            return self._parent._cast(_2771.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2772
            
            return self._parent._cast(_2772.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2773
            
            return self._parent._cast(_2773.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2776
            
            return self._parent._cast(_2776.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2778
            
            return self._parent._cast(_2778.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2779
            
            return self._parent._cast(_2779.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2780
            
            return self._parent._cast(_2780.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2783
            
            return self._parent._cast(_2783.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2785
            
            return self._parent._cast(_2785.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2787
            
            return self._parent._cast(_2787.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2788
            
            return self._parent._cast(_2788.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2790
            
            return self._parent._cast(_2790.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2791
            
            return self._parent._cast(_2791.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2793
            
            return self._parent._cast(_2793.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2794
            
            return self._parent._cast(_2794.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2796
            
            return self._parent._cast(_2796.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2797
            
            return self._parent._cast(_2797.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2798
            
            return self._parent._cast(_2798.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2799
            
            return self._parent._cast(_2799.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2800
            
            return self._parent._cast(_2800.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2801
            
            return self._parent._cast(_2801.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2802
            
            return self._parent._cast(_2802.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2803
            
            return self._parent._cast(_2803.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2808
            
            return self._parent._cast(_2808.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2809
            
            return self._parent._cast(_2809.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2810
            
            return self._parent._cast(_2810.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2813
            
            return self._parent._cast(_2813.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2814
            
            return self._parent._cast(_2814.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2816
            
            return self._parent._cast(_2816.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2817
            
            return self._parent._cast(_2817.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2819
            
            return self._parent._cast(_2819.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2820
            
            return self._parent._cast(_2820.ZerolBevelGearSystemDeflection)

        @property
        def abstract_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6243
            
            return self._parent._cast(_6243.AbstractAssemblyDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6244
            
            return self._parent._cast(_6244.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6245
            
            return self._parent._cast(_6245.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6247
            
            return self._parent._cast(_6247.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6249
            
            return self._parent._cast(_6249.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6250
            
            return self._parent._cast(_6250.AssemblyDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6251
            
            return self._parent._cast(_6251.BearingDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6253
            
            return self._parent._cast(_6253.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6254
            
            return self._parent._cast(_6254.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6256
            
            return self._parent._cast(_6256.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6257
            
            return self._parent._cast(_6257.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6258
            
            return self._parent._cast(_6258.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6259
            
            return self._parent._cast(_6259.BevelGearDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6261
            
            return self._parent._cast(_6261.BevelGearSetDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6262
            
            return self._parent._cast(_6262.BoltDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6263
            
            return self._parent._cast(_6263.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6265
            
            return self._parent._cast(_6265.ClutchDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6266
            
            return self._parent._cast(_6266.ClutchHalfDynamicAnalysis)

        @property
        def component_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6268
            
            return self._parent._cast(_6268.ComponentDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6270
            
            return self._parent._cast(_6270.ConceptCouplingDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6271
            
            return self._parent._cast(_6271.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6272
            
            return self._parent._cast(_6272.ConceptGearDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6274
            
            return self._parent._cast(_6274.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6275
            
            return self._parent._cast(_6275.ConicalGearDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277
            
            return self._parent._cast(_6277.ConicalGearSetDynamicAnalysis)

        @property
        def connector_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279
            
            return self._parent._cast(_6279.ConnectorDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6281
            
            return self._parent._cast(_6281.CouplingDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282
            
            return self._parent._cast(_6282.CouplingHalfDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6284
            
            return self._parent._cast(_6284.CVTDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285
            
            return self._parent._cast(_6285.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286
            
            return self._parent._cast(_6286.CycloidalAssemblyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288
            
            return self._parent._cast(_6288.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290
            
            return self._parent._cast(_6290.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292
            
            return self._parent._cast(_6292.CylindricalGearSetDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293
            
            return self._parent._cast(_6293.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294
            
            return self._parent._cast(_6294.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296
            
            return self._parent._cast(_6296.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6297
            
            return self._parent._cast(_6297.FaceGearDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299
            
            return self._parent._cast(_6299.FaceGearSetDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6300
            
            return self._parent._cast(_6300.FEPartDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301
            
            return self._parent._cast(_6301.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302
            
            return self._parent._cast(_6302.GearDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304
            
            return self._parent._cast(_6304.GearSetDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305
            
            return self._parent._cast(_6305.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306
            
            return self._parent._cast(_6306.HypoidGearDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308
            
            return self._parent._cast(_6308.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310
            
            return self._parent._cast(_6310.KlingelnbergCycloPalloidConicalGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312
            
            return self._parent._cast(_6312.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313
            
            return self._parent._cast(_6313.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315
            
            return self._parent._cast(_6315.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316
            
            return self._parent._cast(_6316.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318
            
            return self._parent._cast(_6318.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis)

        @property
        def mass_disc_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319
            
            return self._parent._cast(_6319.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320
            
            return self._parent._cast(_6320.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321
            
            return self._parent._cast(_6321.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322
            
            return self._parent._cast(_6322.OilSealDynamicAnalysis)

        @property
        def part_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323
            
            return self._parent._cast(_6323.PartDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325
            
            return self._parent._cast(_6325.PartToPartShearCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326
            
            return self._parent._cast(_6326.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328
            
            return self._parent._cast(_6328.PlanetaryGearSetDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329
            
            return self._parent._cast(_6329.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330
            
            return self._parent._cast(_6330.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331
            
            return self._parent._cast(_6331.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332
            
            return self._parent._cast(_6332.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333
            
            return self._parent._cast(_6333.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335
            
            return self._parent._cast(_6335.RollingRingAssemblyDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337
            
            return self._parent._cast(_6337.RollingRingDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338
            
            return self._parent._cast(_6338.RootAssemblyDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339
            
            return self._parent._cast(_6339.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340
            
            return self._parent._cast(_6340.ShaftHubConnectionDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342
            
            return self._parent._cast(_6342.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343
            
            return self._parent._cast(_6343.SpiralBevelGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345
            
            return self._parent._cast(_6345.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347
            
            return self._parent._cast(_6347.SpringDamperDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348
            
            return self._parent._cast(_6348.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349
            
            return self._parent._cast(_6349.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351
            
            return self._parent._cast(_6351.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352
            
            return self._parent._cast(_6352.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354
            
            return self._parent._cast(_6354.StraightBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355
            
            return self._parent._cast(_6355.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356
            
            return self._parent._cast(_6356.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357
            
            return self._parent._cast(_6357.SynchroniserDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358
            
            return self._parent._cast(_6358.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359
            
            return self._parent._cast(_6359.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360
            
            return self._parent._cast(_6360.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362
            
            return self._parent._cast(_6362.TorqueConverterDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363
            
            return self._parent._cast(_6363.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364
            
            return self._parent._cast(_6364.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365
            
            return self._parent._cast(_6365.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366
            
            return self._parent._cast(_6366.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367
            
            return self._parent._cast(_6367.WormGearDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369
            
            return self._parent._cast(_6369.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370
            
            return self._parent._cast(_6370.ZerolBevelGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372
            
            return self._parent._cast(_6372.ZerolBevelGearSetDynamicAnalysis)

        @property
        def part_fe_analysis(self) -> 'PartFEAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartFEAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PartFEAnalysis._Cast_PartFEAnalysis':
        return self._Cast_PartFEAnalysis(self)
