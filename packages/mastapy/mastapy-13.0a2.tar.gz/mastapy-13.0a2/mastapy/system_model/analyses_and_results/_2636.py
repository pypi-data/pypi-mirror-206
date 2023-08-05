"""_2636.py

PartAnalysis
"""
from mastapy.system_model.analyses_and_results import _2632
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'PartAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartAnalysis',)


class PartAnalysis(_2632.DesignEntitySingleContextAnalysis):
    """PartAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_ANALYSIS

    class _Cast_PartAnalysis:
        """Special nested class for casting PartAnalysis to subclasses."""

        def __init__(self, parent: 'PartAnalysis'):
            self._parent = parent

        @property
        def design_entity_single_context_analysis(self):
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
        def abstract_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2962
            
            return self._parent._cast(_2962.AbstractAssemblySteadyStateSynchronousResponse)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2963
            
            return self._parent._cast(_2963.AbstractShaftOrHousingSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2964
            
            return self._parent._cast(_2964.AbstractShaftSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2967
            
            return self._parent._cast(_2967.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2968
            
            return self._parent._cast(_2968.AGMAGleasonConicalGearSteadyStateSynchronousResponse)

        @property
        def assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2969
            
            return self._parent._cast(_2969.AssemblySteadyStateSynchronousResponse)

        @property
        def bearing_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2970
            
            return self._parent._cast(_2970.BearingSteadyStateSynchronousResponse)

        @property
        def belt_drive_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2972
            
            return self._parent._cast(_2972.BeltDriveSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2974
            
            return self._parent._cast(_2974.BevelDifferentialGearSetSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2975
            
            return self._parent._cast(_2975.BevelDifferentialGearSteadyStateSynchronousResponse)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2976
            
            return self._parent._cast(_2976.BevelDifferentialPlanetGearSteadyStateSynchronousResponse)

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2977
            
            return self._parent._cast(_2977.BevelDifferentialSunGearSteadyStateSynchronousResponse)

        @property
        def bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2979
            
            return self._parent._cast(_2979.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2980
            
            return self._parent._cast(_2980.BevelGearSteadyStateSynchronousResponse)

        @property
        def bolted_joint_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2981
            
            return self._parent._cast(_2981.BoltedJointSteadyStateSynchronousResponse)

        @property
        def bolt_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2982
            
            return self._parent._cast(_2982.BoltSteadyStateSynchronousResponse)

        @property
        def clutch_half_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2984
            
            return self._parent._cast(_2984.ClutchHalfSteadyStateSynchronousResponse)

        @property
        def clutch_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2985
            
            return self._parent._cast(_2985.ClutchSteadyStateSynchronousResponse)

        @property
        def component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2987
            
            return self._parent._cast(_2987.ComponentSteadyStateSynchronousResponse)

        @property
        def concept_coupling_half_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2989
            
            return self._parent._cast(_2989.ConceptCouplingHalfSteadyStateSynchronousResponse)

        @property
        def concept_coupling_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2990
            
            return self._parent._cast(_2990.ConceptCouplingSteadyStateSynchronousResponse)

        @property
        def concept_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2992
            
            return self._parent._cast(_2992.ConceptGearSetSteadyStateSynchronousResponse)

        @property
        def concept_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2993
            
            return self._parent._cast(_2993.ConceptGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2995
            
            return self._parent._cast(_2995.ConicalGearSetSteadyStateSynchronousResponse)

        @property
        def conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2996
            
            return self._parent._cast(_2996.ConicalGearSteadyStateSynchronousResponse)

        @property
        def connector_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2998
            
            return self._parent._cast(_2998.ConnectorSteadyStateSynchronousResponse)

        @property
        def coupling_half_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3000
            
            return self._parent._cast(_3000.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def coupling_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3001
            
            return self._parent._cast(_3001.CouplingSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3003
            
            return self._parent._cast(_3003.CVTPulleySteadyStateSynchronousResponse)

        @property
        def cvt_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3004
            
            return self._parent._cast(_3004.CVTSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3005
            
            return self._parent._cast(_3005.CycloidalAssemblySteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3008
            
            return self._parent._cast(_3008.CycloidalDiscSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3010
            
            return self._parent._cast(_3010.CylindricalGearSetSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3011
            
            return self._parent._cast(_3011.CylindricalGearSteadyStateSynchronousResponse)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3012
            
            return self._parent._cast(_3012.CylindricalPlanetGearSteadyStateSynchronousResponse)

        @property
        def datum_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3013
            
            return self._parent._cast(_3013.DatumSteadyStateSynchronousResponse)

        @property
        def external_cad_model_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3015
            
            return self._parent._cast(_3015.ExternalCADModelSteadyStateSynchronousResponse)

        @property
        def face_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3017
            
            return self._parent._cast(_3017.FaceGearSetSteadyStateSynchronousResponse)

        @property
        def face_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3018
            
            return self._parent._cast(_3018.FaceGearSteadyStateSynchronousResponse)

        @property
        def fe_part_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3019
            
            return self._parent._cast(_3019.FEPartSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3020
            
            return self._parent._cast(_3020.FlexiblePinAssemblySteadyStateSynchronousResponse)

        @property
        def gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3022
            
            return self._parent._cast(_3022.GearSetSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3023
            
            return self._parent._cast(_3023.GearSteadyStateSynchronousResponse)

        @property
        def guide_dxf_model_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3024
            
            return self._parent._cast(_3024.GuideDxfModelSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3026
            
            return self._parent._cast(_3026.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3027
            
            return self._parent._cast(_3027.HypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3030
            
            return self._parent._cast(_3030.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3031
            
            return self._parent._cast(_3031.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3033
            
            return self._parent._cast(_3033.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3034
            
            return self._parent._cast(_3034.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3036
            
            return self._parent._cast(_3036.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3037
            
            return self._parent._cast(_3037.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse)

        @property
        def mass_disc_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3038
            
            return self._parent._cast(_3038.MassDiscSteadyStateSynchronousResponse)

        @property
        def measurement_component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3039
            
            return self._parent._cast(_3039.MeasurementComponentSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3040
            
            return self._parent._cast(_3040.MountableComponentSteadyStateSynchronousResponse)

        @property
        def oil_seal_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3041
            
            return self._parent._cast(_3041.OilSealSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3042
            
            return self._parent._cast(_3042.PartSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3044
            
            return self._parent._cast(_3044.PartToPartShearCouplingHalfSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3045
            
            return self._parent._cast(_3045.PartToPartShearCouplingSteadyStateSynchronousResponse)

        @property
        def planetary_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3047
            
            return self._parent._cast(_3047.PlanetaryGearSetSteadyStateSynchronousResponse)

        @property
        def planet_carrier_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3048
            
            return self._parent._cast(_3048.PlanetCarrierSteadyStateSynchronousResponse)

        @property
        def point_load_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3049
            
            return self._parent._cast(_3049.PointLoadSteadyStateSynchronousResponse)

        @property
        def power_load_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3050
            
            return self._parent._cast(_3050.PowerLoadSteadyStateSynchronousResponse)

        @property
        def pulley_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3051
            
            return self._parent._cast(_3051.PulleySteadyStateSynchronousResponse)

        @property
        def ring_pins_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3052
            
            return self._parent._cast(_3052.RingPinsSteadyStateSynchronousResponse)

        @property
        def rolling_ring_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3054
            
            return self._parent._cast(_3054.RollingRingAssemblySteadyStateSynchronousResponse)

        @property
        def rolling_ring_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3056
            
            return self._parent._cast(_3056.RollingRingSteadyStateSynchronousResponse)

        @property
        def root_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3057
            
            return self._parent._cast(_3057.RootAssemblySteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3058
            
            return self._parent._cast(_3058.ShaftHubConnectionSteadyStateSynchronousResponse)

        @property
        def shaft_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3059
            
            return self._parent._cast(_3059.ShaftSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3061
            
            return self._parent._cast(_3061.SpecialisedAssemblySteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3063
            
            return self._parent._cast(_3063.SpiralBevelGearSetSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3064
            
            return self._parent._cast(_3064.SpiralBevelGearSteadyStateSynchronousResponse)

        @property
        def spring_damper_half_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3066
            
            return self._parent._cast(_3066.SpringDamperHalfSteadyStateSynchronousResponse)

        @property
        def spring_damper_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3067
            
            return self._parent._cast(_3067.SpringDamperSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3072
            
            return self._parent._cast(_3072.StraightBevelDiffGearSetSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3073
            
            return self._parent._cast(_3073.StraightBevelDiffGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3075
            
            return self._parent._cast(_3075.StraightBevelGearSetSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3076
            
            return self._parent._cast(_3076.StraightBevelGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3077
            
            return self._parent._cast(_3077.StraightBevelPlanetGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3078
            
            return self._parent._cast(_3078.StraightBevelSunGearSteadyStateSynchronousResponse)

        @property
        def synchroniser_half_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3079
            
            return self._parent._cast(_3079.SynchroniserHalfSteadyStateSynchronousResponse)

        @property
        def synchroniser_part_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3080
            
            return self._parent._cast(_3080.SynchroniserPartSteadyStateSynchronousResponse)

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3081
            
            return self._parent._cast(_3081.SynchroniserSleeveSteadyStateSynchronousResponse)

        @property
        def synchroniser_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3082
            
            return self._parent._cast(_3082.SynchroniserSteadyStateSynchronousResponse)

        @property
        def torque_converter_pump_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3084
            
            return self._parent._cast(_3084.TorqueConverterPumpSteadyStateSynchronousResponse)

        @property
        def torque_converter_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3085
            
            return self._parent._cast(_3085.TorqueConverterSteadyStateSynchronousResponse)

        @property
        def torque_converter_turbine_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3086
            
            return self._parent._cast(_3086.TorqueConverterTurbineSteadyStateSynchronousResponse)

        @property
        def unbalanced_mass_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3087
            
            return self._parent._cast(_3087.UnbalancedMassSteadyStateSynchronousResponse)

        @property
        def virtual_component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3088
            
            return self._parent._cast(_3088.VirtualComponentSteadyStateSynchronousResponse)

        @property
        def worm_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3090
            
            return self._parent._cast(_3090.WormGearSetSteadyStateSynchronousResponse)

        @property
        def worm_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3091
            
            return self._parent._cast(_3091.WormGearSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3093
            
            return self._parent._cast(_3093.ZerolBevelGearSetSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3094
            
            return self._parent._cast(_3094.ZerolBevelGearSteadyStateSynchronousResponse)

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3224
            
            return self._parent._cast(_3224.AbstractAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3225
            
            return self._parent._cast(_3225.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_shaft_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3226
            
            return self._parent._cast(_3226.AbstractShaftSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3229
            
            return self._parent._cast(_3229.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3230
            
            return self._parent._cast(_3230.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3231
            
            return self._parent._cast(_3231.AssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def bearing_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3232
            
            return self._parent._cast(_3232.BearingSteadyStateSynchronousResponseOnAShaft)

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3234
            
            return self._parent._cast(_3234.BeltDriveSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3236
            
            return self._parent._cast(_3236.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft)

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
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3241
            
            return self._parent._cast(_3241.BevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3242
            
            return self._parent._cast(_3242.BevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def bolted_joint_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3243
            
            return self._parent._cast(_3243.BoltedJointSteadyStateSynchronousResponseOnAShaft)

        @property
        def bolt_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3244
            
            return self._parent._cast(_3244.BoltSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3246
            
            return self._parent._cast(_3246.ClutchHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3247
            
            return self._parent._cast(_3247.ClutchSteadyStateSynchronousResponseOnAShaft)

        @property
        def component_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3249
            
            return self._parent._cast(_3249.ComponentSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3251
            
            return self._parent._cast(_3251.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3252
            
            return self._parent._cast(_3252.ConceptCouplingSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3254
            
            return self._parent._cast(_3254.ConceptGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3255
            
            return self._parent._cast(_3255.ConceptGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3257
            
            return self._parent._cast(_3257.ConicalGearSetSteadyStateSynchronousResponseOnAShaft)

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
        def coupling_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3263
            
            return self._parent._cast(_3263.CouplingSteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3265
            
            return self._parent._cast(_3265.CVTPulleySteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3266
            
            return self._parent._cast(_3266.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3267
            
            return self._parent._cast(_3267.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_disc_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3270
            
            return self._parent._cast(_3270.CycloidalDiscSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3272
            
            return self._parent._cast(_3272.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3273
            
            return self._parent._cast(_3273.CylindricalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3274
            
            return self._parent._cast(_3274.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def datum_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3275
            
            return self._parent._cast(_3275.DatumSteadyStateSynchronousResponseOnAShaft)

        @property
        def external_cad_model_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3276
            
            return self._parent._cast(_3276.ExternalCADModelSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3278
            
            return self._parent._cast(_3278.FaceGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3279
            
            return self._parent._cast(_3279.FaceGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def fe_part_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3280
            
            return self._parent._cast(_3280.FEPartSteadyStateSynchronousResponseOnAShaft)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3281
            
            return self._parent._cast(_3281.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3283
            
            return self._parent._cast(_3283.GearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3284
            
            return self._parent._cast(_3284.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def guide_dxf_model_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3285
            
            return self._parent._cast(_3285.GuideDxfModelSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3287
            
            return self._parent._cast(_3287.HypoidGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3288
            
            return self._parent._cast(_3288.HypoidGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3291
            
            return self._parent._cast(_3291.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3292
            
            return self._parent._cast(_3292.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3294
            
            return self._parent._cast(_3294.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3295
            
            return self._parent._cast(_3295.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3297
            
            return self._parent._cast(_3297.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft)

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
        def mountable_component_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3301
            
            return self._parent._cast(_3301.MountableComponentSteadyStateSynchronousResponseOnAShaft)

        @property
        def oil_seal_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3302
            
            return self._parent._cast(_3302.OilSealSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3303
            
            return self._parent._cast(_3303.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3305
            
            return self._parent._cast(_3305.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3306
            
            return self._parent._cast(_3306.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft)

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3308
            
            return self._parent._cast(_3308.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft)

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
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3315
            
            return self._parent._cast(_3315.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def rolling_ring_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3317
            
            return self._parent._cast(_3317.RollingRingSteadyStateSynchronousResponseOnAShaft)

        @property
        def root_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3318
            
            return self._parent._cast(_3318.RootAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_hub_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3319
            
            return self._parent._cast(_3319.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3320
            
            return self._parent._cast(_3320.ShaftSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3322
            
            return self._parent._cast(_3322.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3324
            
            return self._parent._cast(_3324.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3325
            
            return self._parent._cast(_3325.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_half_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3327
            
            return self._parent._cast(_3327.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3328
            
            return self._parent._cast(_3328.SpringDamperSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3331
            
            return self._parent._cast(_3331.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3332
            
            return self._parent._cast(_3332.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3334
            
            return self._parent._cast(_3334.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft)

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
        def synchroniser_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3341
            
            return self._parent._cast(_3341.SynchroniserSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_pump_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3343
            
            return self._parent._cast(_3343.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3344
            
            return self._parent._cast(_3344.TorqueConverterSteadyStateSynchronousResponseOnAShaft)

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
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3349
            
            return self._parent._cast(_3349.WormGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def worm_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3350
            
            return self._parent._cast(_3350.WormGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3352
            
            return self._parent._cast(_3352.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3353
            
            return self._parent._cast(_3353.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3483
            
            return self._parent._cast(_3483.AbstractAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3484
            
            return self._parent._cast(_3484.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3485
            
            return self._parent._cast(_3485.AbstractShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3488
            
            return self._parent._cast(_3488.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3489
            
            return self._parent._cast(_3489.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3490
            
            return self._parent._cast(_3490.AssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3491
            
            return self._parent._cast(_3491.BearingSteadyStateSynchronousResponseAtASpeed)

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3493
            
            return self._parent._cast(_3493.BeltDriveSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3495
            
            return self._parent._cast(_3495.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3496
            
            return self._parent._cast(_3496.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3497
            
            return self._parent._cast(_3497.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3498
            
            return self._parent._cast(_3498.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3500
            
            return self._parent._cast(_3500.BevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3501
            
            return self._parent._cast(_3501.BevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def bolted_joint_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3502
            
            return self._parent._cast(_3502.BoltedJointSteadyStateSynchronousResponseAtASpeed)

        @property
        def bolt_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3503
            
            return self._parent._cast(_3503.BoltSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3505
            
            return self._parent._cast(_3505.ClutchHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3506
            
            return self._parent._cast(_3506.ClutchSteadyStateSynchronousResponseAtASpeed)

        @property
        def component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3508
            
            return self._parent._cast(_3508.ComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3510
            
            return self._parent._cast(_3510.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3511
            
            return self._parent._cast(_3511.ConceptCouplingSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3513
            
            return self._parent._cast(_3513.ConceptGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def concept_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3514
            
            return self._parent._cast(_3514.ConceptGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3516
            
            return self._parent._cast(_3516.ConicalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3517
            
            return self._parent._cast(_3517.ConicalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def connector_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3519
            
            return self._parent._cast(_3519.ConnectorSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3521
            
            return self._parent._cast(_3521.CouplingHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3522
            
            return self._parent._cast(_3522.CouplingSteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3524
            
            return self._parent._cast(_3524.CVTPulleySteadyStateSynchronousResponseAtASpeed)

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3525
            
            return self._parent._cast(_3525.CVTSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3526
            
            return self._parent._cast(_3526.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3529
            
            return self._parent._cast(_3529.CycloidalDiscSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3531
            
            return self._parent._cast(_3531.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3532
            
            return self._parent._cast(_3532.CylindricalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3533
            
            return self._parent._cast(_3533.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def datum_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3534
            
            return self._parent._cast(_3534.DatumSteadyStateSynchronousResponseAtASpeed)

        @property
        def external_cad_model_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3535
            
            return self._parent._cast(_3535.ExternalCADModelSteadyStateSynchronousResponseAtASpeed)

        @property
        def face_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3537
            
            return self._parent._cast(_3537.FaceGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3538
            
            return self._parent._cast(_3538.FaceGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def fe_part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3539
            
            return self._parent._cast(_3539.FEPartSteadyStateSynchronousResponseAtASpeed)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3540
            
            return self._parent._cast(_3540.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3542
            
            return self._parent._cast(_3542.GearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3543
            
            return self._parent._cast(_3543.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def guide_dxf_model_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3544
            
            return self._parent._cast(_3544.GuideDxfModelSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3546
            
            return self._parent._cast(_3546.HypoidGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3547
            
            return self._parent._cast(_3547.HypoidGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3550
            
            return self._parent._cast(_3550.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3551
            
            return self._parent._cast(_3551.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3553
            
            return self._parent._cast(_3553.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3554
            
            return self._parent._cast(_3554.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3556
            
            return self._parent._cast(_3556.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3557
            
            return self._parent._cast(_3557.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3558
            
            return self._parent._cast(_3558.MassDiscSteadyStateSynchronousResponseAtASpeed)

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3559
            
            return self._parent._cast(_3559.MeasurementComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3560
            
            return self._parent._cast(_3560.MountableComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3561
            
            return self._parent._cast(_3561.OilSealSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3562
            
            return self._parent._cast(_3562.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3564
            
            return self._parent._cast(_3564.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3565
            
            return self._parent._cast(_3565.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed)

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3567
            
            return self._parent._cast(_3567.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3568
            
            return self._parent._cast(_3568.PlanetCarrierSteadyStateSynchronousResponseAtASpeed)

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3569
            
            return self._parent._cast(_3569.PointLoadSteadyStateSynchronousResponseAtASpeed)

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3570
            
            return self._parent._cast(_3570.PowerLoadSteadyStateSynchronousResponseAtASpeed)

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3571
            
            return self._parent._cast(_3571.PulleySteadyStateSynchronousResponseAtASpeed)

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3572
            
            return self._parent._cast(_3572.RingPinsSteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3574
            
            return self._parent._cast(_3574.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3576
            
            return self._parent._cast(_3576.RollingRingSteadyStateSynchronousResponseAtASpeed)

        @property
        def root_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3577
            
            return self._parent._cast(_3577.RootAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3578
            
            return self._parent._cast(_3578.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3579
            
            return self._parent._cast(_3579.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3581
            
            return self._parent._cast(_3581.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3583
            
            return self._parent._cast(_3583.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3584
            
            return self._parent._cast(_3584.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3586
            
            return self._parent._cast(_3586.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def spring_damper_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3587
            
            return self._parent._cast(_3587.SpringDamperSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3590
            
            return self._parent._cast(_3590.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3591
            
            return self._parent._cast(_3591.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3593
            
            return self._parent._cast(_3593.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3594
            
            return self._parent._cast(_3594.StraightBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3595
            
            return self._parent._cast(_3595.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3596
            
            return self._parent._cast(_3596.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3597
            
            return self._parent._cast(_3597.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3598
            
            return self._parent._cast(_3598.SynchroniserPartSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3599
            
            return self._parent._cast(_3599.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed)

        @property
        def synchroniser_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3600
            
            return self._parent._cast(_3600.SynchroniserSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3602
            
            return self._parent._cast(_3602.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3603
            
            return self._parent._cast(_3603.TorqueConverterSteadyStateSynchronousResponseAtASpeed)

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3604
            
            return self._parent._cast(_3604.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed)

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3605
            
            return self._parent._cast(_3605.UnbalancedMassSteadyStateSynchronousResponseAtASpeed)

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3606
            
            return self._parent._cast(_3606.VirtualComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def worm_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3608
            
            return self._parent._cast(_3608.WormGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def worm_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3609
            
            return self._parent._cast(_3609.WormGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3611
            
            return self._parent._cast(_3611.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3612
            
            return self._parent._cast(_3612.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3742
            
            return self._parent._cast(_3742.AbstractAssemblyStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3743
            
            return self._parent._cast(_3743.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def abstract_shaft_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3744
            
            return self._parent._cast(_3744.AbstractShaftStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3747
            
            return self._parent._cast(_3747.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3748
            
            return self._parent._cast(_3748.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3749
            
            return self._parent._cast(_3749.AssemblyStabilityAnalysis)

        @property
        def bearing_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3750
            
            return self._parent._cast(_3750.BearingStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3752
            
            return self._parent._cast(_3752.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3754
            
            return self._parent._cast(_3754.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3755
            
            return self._parent._cast(_3755.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3756
            
            return self._parent._cast(_3756.BevelDifferentialPlanetGearStabilityAnalysis)

        @property
        def bevel_differential_sun_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3757
            
            return self._parent._cast(_3757.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3759
            
            return self._parent._cast(_3759.BevelGearSetStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3760
            
            return self._parent._cast(_3760.BevelGearStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3761
            
            return self._parent._cast(_3761.BoltedJointStabilityAnalysis)

        @property
        def bolt_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3762
            
            return self._parent._cast(_3762.BoltStabilityAnalysis)

        @property
        def clutch_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3764
            
            return self._parent._cast(_3764.ClutchHalfStabilityAnalysis)

        @property
        def clutch_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3765
            
            return self._parent._cast(_3765.ClutchStabilityAnalysis)

        @property
        def component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3767
            
            return self._parent._cast(_3767.ComponentStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3769
            
            return self._parent._cast(_3769.ConceptCouplingHalfStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3770
            
            return self._parent._cast(_3770.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3772
            
            return self._parent._cast(_3772.ConceptGearSetStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3773
            
            return self._parent._cast(_3773.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3775
            
            return self._parent._cast(_3775.ConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3776
            
            return self._parent._cast(_3776.ConicalGearStabilityAnalysis)

        @property
        def connector_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3778
            
            return self._parent._cast(_3778.ConnectorStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3780
            
            return self._parent._cast(_3780.CouplingHalfStabilityAnalysis)

        @property
        def coupling_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3781
            
            return self._parent._cast(_3781.CouplingStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3784
            
            return self._parent._cast(_3784.CVTPulleyStabilityAnalysis)

        @property
        def cvt_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3785
            
            return self._parent._cast(_3785.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3786
            
            return self._parent._cast(_3786.CycloidalAssemblyStabilityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3789
            
            return self._parent._cast(_3789.CycloidalDiscStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3791
            
            return self._parent._cast(_3791.CylindricalGearSetStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3792
            
            return self._parent._cast(_3792.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3793
            
            return self._parent._cast(_3793.CylindricalPlanetGearStabilityAnalysis)

        @property
        def datum_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3794
            
            return self._parent._cast(_3794.DatumStabilityAnalysis)

        @property
        def external_cad_model_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3795
            
            return self._parent._cast(_3795.ExternalCADModelStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3797
            
            return self._parent._cast(_3797.FaceGearSetStabilityAnalysis)

        @property
        def face_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3798
            
            return self._parent._cast(_3798.FaceGearStabilityAnalysis)

        @property
        def fe_part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3799
            
            return self._parent._cast(_3799.FEPartStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3800
            
            return self._parent._cast(_3800.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3802
            
            return self._parent._cast(_3802.GearSetStabilityAnalysis)

        @property
        def gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3803
            
            return self._parent._cast(_3803.GearStabilityAnalysis)

        @property
        def guide_dxf_model_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3804
            
            return self._parent._cast(_3804.GuideDxfModelStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3806
            
            return self._parent._cast(_3806.HypoidGearSetStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3807
            
            return self._parent._cast(_3807.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3810
            
            return self._parent._cast(_3810.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3811
            
            return self._parent._cast(_3811.KlingelnbergCycloPalloidConicalGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3813
            
            return self._parent._cast(_3813.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3814
            
            return self._parent._cast(_3814.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3816
            
            return self._parent._cast(_3816.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3817
            
            return self._parent._cast(_3817.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis)

        @property
        def mass_disc_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3818
            
            return self._parent._cast(_3818.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3819
            
            return self._parent._cast(_3819.MeasurementComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3820
            
            return self._parent._cast(_3820.MountableComponentStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3821
            
            return self._parent._cast(_3821.OilSealStabilityAnalysis)

        @property
        def part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3822
            
            return self._parent._cast(_3822.PartStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3824
            
            return self._parent._cast(_3824.PartToPartShearCouplingHalfStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3825
            
            return self._parent._cast(_3825.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3827
            
            return self._parent._cast(_3827.PlanetaryGearSetStabilityAnalysis)

        @property
        def planet_carrier_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3828
            
            return self._parent._cast(_3828.PlanetCarrierStabilityAnalysis)

        @property
        def point_load_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3829
            
            return self._parent._cast(_3829.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3830
            
            return self._parent._cast(_3830.PowerLoadStabilityAnalysis)

        @property
        def pulley_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3831
            
            return self._parent._cast(_3831.PulleyStabilityAnalysis)

        @property
        def ring_pins_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3832
            
            return self._parent._cast(_3832.RingPinsStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3834
            
            return self._parent._cast(_3834.RollingRingAssemblyStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3836
            
            return self._parent._cast(_3836.RollingRingStabilityAnalysis)

        @property
        def root_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3837
            
            return self._parent._cast(_3837.RootAssemblyStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3838
            
            return self._parent._cast(_3838.ShaftHubConnectionStabilityAnalysis)

        @property
        def shaft_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3839
            
            return self._parent._cast(_3839.ShaftStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3841
            
            return self._parent._cast(_3841.SpecialisedAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3843
            
            return self._parent._cast(_3843.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3844
            
            return self._parent._cast(_3844.SpiralBevelGearStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3846
            
            return self._parent._cast(_3846.SpringDamperHalfStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3847
            
            return self._parent._cast(_3847.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3851
            
            return self._parent._cast(_3851.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3852
            
            return self._parent._cast(_3852.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3854
            
            return self._parent._cast(_3854.StraightBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3855
            
            return self._parent._cast(_3855.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3856
            
            return self._parent._cast(_3856.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3857
            
            return self._parent._cast(_3857.StraightBevelSunGearStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3858
            
            return self._parent._cast(_3858.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3859
            
            return self._parent._cast(_3859.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3860
            
            return self._parent._cast(_3860.SynchroniserSleeveStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3861
            
            return self._parent._cast(_3861.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3863
            
            return self._parent._cast(_3863.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3864
            
            return self._parent._cast(_3864.TorqueConverterStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3865
            
            return self._parent._cast(_3865.TorqueConverterTurbineStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3866
            
            return self._parent._cast(_3866.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3867
            
            return self._parent._cast(_3867.VirtualComponentStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3869
            
            return self._parent._cast(_3869.WormGearSetStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3870
            
            return self._parent._cast(_3870.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3872
            
            return self._parent._cast(_3872.ZerolBevelGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3873
            
            return self._parent._cast(_3873.ZerolBevelGearStabilityAnalysis)

        @property
        def abstract_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4009
            
            return self._parent._cast(_4009.AbstractAssemblyPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4010
            
            return self._parent._cast(_4010.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4011
            
            return self._parent._cast(_4011.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4014
            
            return self._parent._cast(_4014.AGMAGleasonConicalGearPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4015
            
            return self._parent._cast(_4015.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4016
            
            return self._parent._cast(_4016.AssemblyPowerFlow)

        @property
        def bearing_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4017
            
            return self._parent._cast(_4017.BearingPowerFlow)

        @property
        def belt_drive_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4019
            
            return self._parent._cast(_4019.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4021
            
            return self._parent._cast(_4021.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4022
            
            return self._parent._cast(_4022.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4023
            
            return self._parent._cast(_4023.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4024
            
            return self._parent._cast(_4024.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4026
            
            return self._parent._cast(_4026.BevelGearPowerFlow)

        @property
        def bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4027
            
            return self._parent._cast(_4027.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4028
            
            return self._parent._cast(_4028.BoltedJointPowerFlow)

        @property
        def bolt_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4029
            
            return self._parent._cast(_4029.BoltPowerFlow)

        @property
        def clutch_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4031
            
            return self._parent._cast(_4031.ClutchHalfPowerFlow)

        @property
        def clutch_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4032
            
            return self._parent._cast(_4032.ClutchPowerFlow)

        @property
        def component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4034
            
            return self._parent._cast(_4034.ComponentPowerFlow)

        @property
        def concept_coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4036
            
            return self._parent._cast(_4036.ConceptCouplingHalfPowerFlow)

        @property
        def concept_coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4037
            
            return self._parent._cast(_4037.ConceptCouplingPowerFlow)

        @property
        def concept_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4039
            
            return self._parent._cast(_4039.ConceptGearPowerFlow)

        @property
        def concept_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4040
            
            return self._parent._cast(_4040.ConceptGearSetPowerFlow)

        @property
        def conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4042
            
            return self._parent._cast(_4042.ConicalGearPowerFlow)

        @property
        def conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4043
            
            return self._parent._cast(_4043.ConicalGearSetPowerFlow)

        @property
        def connector_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4045
            
            return self._parent._cast(_4045.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4047
            
            return self._parent._cast(_4047.CouplingHalfPowerFlow)

        @property
        def coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4048
            
            return self._parent._cast(_4048.CouplingPowerFlow)

        @property
        def cvt_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4050
            
            return self._parent._cast(_4050.CVTPowerFlow)

        @property
        def cvt_pulley_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4051
            
            return self._parent._cast(_4051.CVTPulleyPowerFlow)

        @property
        def cycloidal_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4052
            
            return self._parent._cast(_4052.CycloidalAssemblyPowerFlow)

        @property
        def cycloidal_disc_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4055
            
            return self._parent._cast(_4055.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4058
            
            return self._parent._cast(_4058.CylindricalGearPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4059
            
            return self._parent._cast(_4059.CylindricalGearSetPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4060
            
            return self._parent._cast(_4060.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4061
            
            return self._parent._cast(_4061.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4062
            
            return self._parent._cast(_4062.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4064
            
            return self._parent._cast(_4064.FaceGearPowerFlow)

        @property
        def face_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4065
            
            return self._parent._cast(_4065.FaceGearSetPowerFlow)

        @property
        def fe_part_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4066
            
            return self._parent._cast(_4066.FEPartPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4067
            
            return self._parent._cast(_4067.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4069
            
            return self._parent._cast(_4069.GearPowerFlow)

        @property
        def gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4070
            
            return self._parent._cast(_4070.GearSetPowerFlow)

        @property
        def guide_dxf_model_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4071
            
            return self._parent._cast(_4071.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4073
            
            return self._parent._cast(_4073.HypoidGearPowerFlow)

        @property
        def hypoid_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4074
            
            return self._parent._cast(_4074.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4077
            
            return self._parent._cast(_4077.KlingelnbergCycloPalloidConicalGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4078
            
            return self._parent._cast(_4078.KlingelnbergCycloPalloidConicalGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4080
            
            return self._parent._cast(_4080.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4081
            
            return self._parent._cast(_4081.KlingelnbergCycloPalloidHypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4083
            
            return self._parent._cast(_4083.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4084
            
            return self._parent._cast(_4084.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow)

        @property
        def mass_disc_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4085
            
            return self._parent._cast(_4085.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4086
            
            return self._parent._cast(_4086.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4087
            
            return self._parent._cast(_4087.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4088
            
            return self._parent._cast(_4088.OilSealPowerFlow)

        @property
        def part_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4089
            
            return self._parent._cast(_4089.PartPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4091
            
            return self._parent._cast(_4091.PartToPartShearCouplingHalfPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4092
            
            return self._parent._cast(_4092.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4094
            
            return self._parent._cast(_4094.PlanetaryGearSetPowerFlow)

        @property
        def planet_carrier_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4095
            
            return self._parent._cast(_4095.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4096
            
            return self._parent._cast(_4096.PointLoadPowerFlow)

        @property
        def power_load_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4099
            
            return self._parent._cast(_4099.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4100
            
            return self._parent._cast(_4100.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4101
            
            return self._parent._cast(_4101.RingPinsPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4103
            
            return self._parent._cast(_4103.RollingRingAssemblyPowerFlow)

        @property
        def rolling_ring_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4105
            
            return self._parent._cast(_4105.RollingRingPowerFlow)

        @property
        def root_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4106
            
            return self._parent._cast(_4106.RootAssemblyPowerFlow)

        @property
        def shaft_hub_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4107
            
            return self._parent._cast(_4107.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4108
            
            return self._parent._cast(_4108.ShaftPowerFlow)

        @property
        def specialised_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4110
            
            return self._parent._cast(_4110.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4112
            
            return self._parent._cast(_4112.SpiralBevelGearPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4113
            
            return self._parent._cast(_4113.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4115
            
            return self._parent._cast(_4115.SpringDamperHalfPowerFlow)

        @property
        def spring_damper_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4116
            
            return self._parent._cast(_4116.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4118
            
            return self._parent._cast(_4118.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4119
            
            return self._parent._cast(_4119.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4121
            
            return self._parent._cast(_4121.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4122
            
            return self._parent._cast(_4122.StraightBevelGearSetPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4123
            
            return self._parent._cast(_4123.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4124
            
            return self._parent._cast(_4124.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4125
            
            return self._parent._cast(_4125.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4126
            
            return self._parent._cast(_4126.SynchroniserPartPowerFlow)

        @property
        def synchroniser_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4127
            
            return self._parent._cast(_4127.SynchroniserPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4128
            
            return self._parent._cast(_4128.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4131
            
            return self._parent._cast(_4131.TorqueConverterPowerFlow)

        @property
        def torque_converter_pump_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4132
            
            return self._parent._cast(_4132.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4133
            
            return self._parent._cast(_4133.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4134
            
            return self._parent._cast(_4134.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4135
            
            return self._parent._cast(_4135.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4137
            
            return self._parent._cast(_4137.WormGearPowerFlow)

        @property
        def worm_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4138
            
            return self._parent._cast(_4138.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4140
            
            return self._parent._cast(_4140.ZerolBevelGearPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4141
            
            return self._parent._cast(_4141.ZerolBevelGearSetPowerFlow)

        @property
        def abstract_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4271
            
            return self._parent._cast(_4271.AbstractAssemblyParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4272
            
            return self._parent._cast(_4272.AbstractShaftOrHousingParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4273
            
            return self._parent._cast(_4273.AbstractShaftParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4276
            
            return self._parent._cast(_4276.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4277
            
            return self._parent._cast(_4277.AGMAGleasonConicalGearSetParametricStudyTool)

        @property
        def assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4278
            
            return self._parent._cast(_4278.AssemblyParametricStudyTool)

        @property
        def bearing_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4279
            
            return self._parent._cast(_4279.BearingParametricStudyTool)

        @property
        def belt_drive_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4281
            
            return self._parent._cast(_4281.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4283
            
            return self._parent._cast(_4283.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4284
            
            return self._parent._cast(_4284.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4285
            
            return self._parent._cast(_4285.BevelDifferentialPlanetGearParametricStudyTool)

        @property
        def bevel_differential_sun_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4286
            
            return self._parent._cast(_4286.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4288
            
            return self._parent._cast(_4288.BevelGearParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4289
            
            return self._parent._cast(_4289.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4290
            
            return self._parent._cast(_4290.BoltedJointParametricStudyTool)

        @property
        def bolt_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4291
            
            return self._parent._cast(_4291.BoltParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4293
            
            return self._parent._cast(_4293.ClutchHalfParametricStudyTool)

        @property
        def clutch_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4294
            
            return self._parent._cast(_4294.ClutchParametricStudyTool)

        @property
        def component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4296
            
            return self._parent._cast(_4296.ComponentParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4298
            
            return self._parent._cast(_4298.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4299
            
            return self._parent._cast(_4299.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4301
            
            return self._parent._cast(_4301.ConceptGearParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4302
            
            return self._parent._cast(_4302.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4304
            
            return self._parent._cast(_4304.ConicalGearParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4305
            
            return self._parent._cast(_4305.ConicalGearSetParametricStudyTool)

        @property
        def connector_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4307
            
            return self._parent._cast(_4307.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4309
            
            return self._parent._cast(_4309.CouplingHalfParametricStudyTool)

        @property
        def coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4310
            
            return self._parent._cast(_4310.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4312
            
            return self._parent._cast(_4312.CVTParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4313
            
            return self._parent._cast(_4313.CVTPulleyParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4314
            
            return self._parent._cast(_4314.CycloidalAssemblyParametricStudyTool)

        @property
        def cycloidal_disc_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4316
            
            return self._parent._cast(_4316.CycloidalDiscParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4319
            
            return self._parent._cast(_4319.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4320
            
            return self._parent._cast(_4320.CylindricalGearSetParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4321
            
            return self._parent._cast(_4321.CylindricalPlanetGearParametricStudyTool)

        @property
        def datum_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4322
            
            return self._parent._cast(_4322.DatumParametricStudyTool)

        @property
        def external_cad_model_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4330
            
            return self._parent._cast(_4330.ExternalCADModelParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4332
            
            return self._parent._cast(_4332.FaceGearParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4333
            
            return self._parent._cast(_4333.FaceGearSetParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4334
            
            return self._parent._cast(_4334.FEPartParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4335
            
            return self._parent._cast(_4335.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4337
            
            return self._parent._cast(_4337.GearParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4338
            
            return self._parent._cast(_4338.GearSetParametricStudyTool)

        @property
        def guide_dxf_model_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4339
            
            return self._parent._cast(_4339.GuideDxfModelParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4341
            
            return self._parent._cast(_4341.HypoidGearParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4342
            
            return self._parent._cast(_4342.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4345
            
            return self._parent._cast(_4345.KlingelnbergCycloPalloidConicalGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4346
            
            return self._parent._cast(_4346.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4348
            
            return self._parent._cast(_4348.KlingelnbergCycloPalloidHypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4349
            
            return self._parent._cast(_4349.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4351
            
            return self._parent._cast(_4351.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4352
            
            return self._parent._cast(_4352.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool)

        @property
        def mass_disc_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4353
            
            return self._parent._cast(_4353.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4354
            
            return self._parent._cast(_4354.MeasurementComponentParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4356
            
            return self._parent._cast(_4356.MountableComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4357
            
            return self._parent._cast(_4357.OilSealParametricStudyTool)

        @property
        def part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4368
            
            return self._parent._cast(_4368.PartParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4370
            
            return self._parent._cast(_4370.PartToPartShearCouplingHalfParametricStudyTool)

        @property
        def part_to_part_shear_coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4371
            
            return self._parent._cast(_4371.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4373
            
            return self._parent._cast(_4373.PlanetaryGearSetParametricStudyTool)

        @property
        def planet_carrier_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4374
            
            return self._parent._cast(_4374.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4375
            
            return self._parent._cast(_4375.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4376
            
            return self._parent._cast(_4376.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4377
            
            return self._parent._cast(_4377.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4378
            
            return self._parent._cast(_4378.RingPinsParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4380
            
            return self._parent._cast(_4380.RollingRingAssemblyParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4382
            
            return self._parent._cast(_4382.RollingRingParametricStudyTool)

        @property
        def root_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4383
            
            return self._parent._cast(_4383.RootAssemblyParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4384
            
            return self._parent._cast(_4384.ShaftHubConnectionParametricStudyTool)

        @property
        def shaft_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4385
            
            return self._parent._cast(_4385.ShaftParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4387
            
            return self._parent._cast(_4387.SpecialisedAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4389
            
            return self._parent._cast(_4389.SpiralBevelGearParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4390
            
            return self._parent._cast(_4390.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4392
            
            return self._parent._cast(_4392.SpringDamperHalfParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4393
            
            return self._parent._cast(_4393.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4395
            
            return self._parent._cast(_4395.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4396
            
            return self._parent._cast(_4396.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4398
            
            return self._parent._cast(_4398.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4399
            
            return self._parent._cast(_4399.StraightBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4400
            
            return self._parent._cast(_4400.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4401
            
            return self._parent._cast(_4401.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4402
            
            return self._parent._cast(_4402.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4403
            
            return self._parent._cast(_4403.SynchroniserParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4404
            
            return self._parent._cast(_4404.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4405
            
            return self._parent._cast(_4405.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4407
            
            return self._parent._cast(_4407.TorqueConverterParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4408
            
            return self._parent._cast(_4408.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4409
            
            return self._parent._cast(_4409.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4410
            
            return self._parent._cast(_4410.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4411
            
            return self._parent._cast(_4411.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4413
            
            return self._parent._cast(_4413.WormGearParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4414
            
            return self._parent._cast(_4414.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4416
            
            return self._parent._cast(_4416.ZerolBevelGearParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4417
            
            return self._parent._cast(_4417.ZerolBevelGearSetParametricStudyTool)

        @property
        def abstract_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4547
            
            return self._parent._cast(_4547.AbstractAssemblyModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4548
            
            return self._parent._cast(_4548.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4549
            
            return self._parent._cast(_4549.AbstractShaftOrHousingModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4552
            
            return self._parent._cast(_4552.AGMAGleasonConicalGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4553
            
            return self._parent._cast(_4553.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4554
            
            return self._parent._cast(_4554.AssemblyModalAnalysis)

        @property
        def bearing_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4555
            
            return self._parent._cast(_4555.BearingModalAnalysis)

        @property
        def belt_drive_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4557
            
            return self._parent._cast(_4557.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4559
            
            return self._parent._cast(_4559.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4560
            
            return self._parent._cast(_4560.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4561
            
            return self._parent._cast(_4561.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4562
            
            return self._parent._cast(_4562.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4564
            
            return self._parent._cast(_4564.BevelGearModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4565
            
            return self._parent._cast(_4565.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4566
            
            return self._parent._cast(_4566.BoltedJointModalAnalysis)

        @property
        def bolt_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4567
            
            return self._parent._cast(_4567.BoltModalAnalysis)

        @property
        def clutch_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4569
            
            return self._parent._cast(_4569.ClutchHalfModalAnalysis)

        @property
        def clutch_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4570
            
            return self._parent._cast(_4570.ClutchModalAnalysis)

        @property
        def component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572
            
            return self._parent._cast(_4572.ComponentModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574
            
            return self._parent._cast(_4574.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_coupling_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4575
            
            return self._parent._cast(_4575.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4577
            
            return self._parent._cast(_4577.ConceptGearModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578
            
            return self._parent._cast(_4578.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580
            
            return self._parent._cast(_4580.ConicalGearModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581
            
            return self._parent._cast(_4581.ConicalGearSetModalAnalysis)

        @property
        def connector_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4583
            
            return self._parent._cast(_4583.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586
            
            return self._parent._cast(_4586.CouplingHalfModalAnalysis)

        @property
        def coupling_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4587
            
            return self._parent._cast(_4587.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4589
            
            return self._parent._cast(_4589.CVTModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590
            
            return self._parent._cast(_4590.CVTPulleyModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4591
            
            return self._parent._cast(_4591.CycloidalAssemblyModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593
            
            return self._parent._cast(_4593.CycloidalDiscModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596
            
            return self._parent._cast(_4596.CylindricalGearModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597
            
            return self._parent._cast(_4597.CylindricalGearSetModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598
            
            return self._parent._cast(_4598.CylindricalPlanetGearModalAnalysis)

        @property
        def datum_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599
            
            return self._parent._cast(_4599.DatumModalAnalysis)

        @property
        def external_cad_model_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602
            
            return self._parent._cast(_4602.ExternalCADModelModalAnalysis)

        @property
        def face_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604
            
            return self._parent._cast(_4604.FaceGearModalAnalysis)

        @property
        def face_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605
            
            return self._parent._cast(_4605.FaceGearSetModalAnalysis)

        @property
        def fe_part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606
            
            return self._parent._cast(_4606.FEPartModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607
            
            return self._parent._cast(_4607.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610
            
            return self._parent._cast(_4610.GearModalAnalysis)

        @property
        def gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611
            
            return self._parent._cast(_4611.GearSetModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612
            
            return self._parent._cast(_4612.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614
            
            return self._parent._cast(_4614.HypoidGearModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615
            
            return self._parent._cast(_4615.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618
            
            return self._parent._cast(_4618.KlingelnbergCycloPalloidConicalGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619
            
            return self._parent._cast(_4619.KlingelnbergCycloPalloidConicalGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4621
            
            return self._parent._cast(_4621.KlingelnbergCycloPalloidHypoidGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622
            
            return self._parent._cast(_4622.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4624
            
            return self._parent._cast(_4624.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625
            
            return self._parent._cast(_4625.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis)

        @property
        def mass_disc_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626
            
            return self._parent._cast(_4626.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4627
            
            return self._parent._cast(_4627.MeasurementComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631
            
            return self._parent._cast(_4631.MountableComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633
            
            return self._parent._cast(_4633.OilSealModalAnalysis)

        @property
        def part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635
            
            return self._parent._cast(_4635.PartModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637
            
            return self._parent._cast(_4637.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638
            
            return self._parent._cast(_4638.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640
            
            return self._parent._cast(_4640.PlanetaryGearSetModalAnalysis)

        @property
        def planet_carrier_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641
            
            return self._parent._cast(_4641.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642
            
            return self._parent._cast(_4642.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643
            
            return self._parent._cast(_4643.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644
            
            return self._parent._cast(_4644.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645
            
            return self._parent._cast(_4645.RingPinsModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647
            
            return self._parent._cast(_4647.RollingRingAssemblyModalAnalysis)

        @property
        def rolling_ring_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649
            
            return self._parent._cast(_4649.RollingRingModalAnalysis)

        @property
        def root_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4650
            
            return self._parent._cast(_4650.RootAssemblyModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651
            
            return self._parent._cast(_4651.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4652
            
            return self._parent._cast(_4652.ShaftModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655
            
            return self._parent._cast(_4655.SpecialisedAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657
            
            return self._parent._cast(_4657.SpiralBevelGearModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658
            
            return self._parent._cast(_4658.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660
            
            return self._parent._cast(_4660.SpringDamperHalfModalAnalysis)

        @property
        def spring_damper_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661
            
            return self._parent._cast(_4661.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663
            
            return self._parent._cast(_4663.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664
            
            return self._parent._cast(_4664.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666
            
            return self._parent._cast(_4666.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667
            
            return self._parent._cast(_4667.StraightBevelGearSetModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668
            
            return self._parent._cast(_4668.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4669
            
            return self._parent._cast(_4669.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670
            
            return self._parent._cast(_4670.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671
            
            return self._parent._cast(_4671.SynchroniserModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672
            
            return self._parent._cast(_4672.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673
            
            return self._parent._cast(_4673.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675
            
            return self._parent._cast(_4675.TorqueConverterModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4676
            
            return self._parent._cast(_4676.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4677
            
            return self._parent._cast(_4677.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678
            
            return self._parent._cast(_4678.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679
            
            return self._parent._cast(_4679.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684
            
            return self._parent._cast(_4684.WormGearModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685
            
            return self._parent._cast(_4685.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687
            
            return self._parent._cast(_4687.ZerolBevelGearModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688
            
            return self._parent._cast(_4688.ZerolBevelGearSetModalAnalysis)

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4830
            
            return self._parent._cast(_4830.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4831
            
            return self._parent._cast(_4831.AbstractShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4832
            
            return self._parent._cast(_4832.AbstractShaftOrHousingModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4835
            
            return self._parent._cast(_4835.AGMAGleasonConicalGearModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4836
            
            return self._parent._cast(_4836.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness)

        @property
        def assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4837
            
            return self._parent._cast(_4837.AssemblyModalAnalysisAtAStiffness)

        @property
        def bearing_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4838
            
            return self._parent._cast(_4838.BearingModalAnalysisAtAStiffness)

        @property
        def belt_drive_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4840
            
            return self._parent._cast(_4840.BeltDriveModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4842
            
            return self._parent._cast(_4842.BevelDifferentialGearModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4843
            
            return self._parent._cast(_4843.BevelDifferentialGearSetModalAnalysisAtAStiffness)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4844
            
            return self._parent._cast(_4844.BevelDifferentialPlanetGearModalAnalysisAtAStiffness)

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4845
            
            return self._parent._cast(_4845.BevelDifferentialSunGearModalAnalysisAtAStiffness)

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4847
            
            return self._parent._cast(_4847.BevelGearModalAnalysisAtAStiffness)

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4848
            
            return self._parent._cast(_4848.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def bolted_joint_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4849
            
            return self._parent._cast(_4849.BoltedJointModalAnalysisAtAStiffness)

        @property
        def bolt_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4850
            
            return self._parent._cast(_4850.BoltModalAnalysisAtAStiffness)

        @property
        def clutch_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4852
            
            return self._parent._cast(_4852.ClutchHalfModalAnalysisAtAStiffness)

        @property
        def clutch_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4853
            
            return self._parent._cast(_4853.ClutchModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4855
            
            return self._parent._cast(_4855.ComponentModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4857
            
            return self._parent._cast(_4857.ConceptCouplingHalfModalAnalysisAtAStiffness)

        @property
        def concept_coupling_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4858
            
            return self._parent._cast(_4858.ConceptCouplingModalAnalysisAtAStiffness)

        @property
        def concept_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4860
            
            return self._parent._cast(_4860.ConceptGearModalAnalysisAtAStiffness)

        @property
        def concept_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4861
            
            return self._parent._cast(_4861.ConceptGearSetModalAnalysisAtAStiffness)

        @property
        def conical_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4863
            
            return self._parent._cast(_4863.ConicalGearModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4864
            
            return self._parent._cast(_4864.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def connector_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4866
            
            return self._parent._cast(_4866.ConnectorModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4868
            
            return self._parent._cast(_4868.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def coupling_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4869
            
            return self._parent._cast(_4869.CouplingModalAnalysisAtAStiffness)

        @property
        def cvt_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4871
            
            return self._parent._cast(_4871.CVTModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4872
            
            return self._parent._cast(_4872.CVTPulleyModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4873
            
            return self._parent._cast(_4873.CycloidalAssemblyModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4875
            
            return self._parent._cast(_4875.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4878
            
            return self._parent._cast(_4878.CylindricalGearModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4879
            
            return self._parent._cast(_4879.CylindricalGearSetModalAnalysisAtAStiffness)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4880
            
            return self._parent._cast(_4880.CylindricalPlanetGearModalAnalysisAtAStiffness)

        @property
        def datum_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4881
            
            return self._parent._cast(_4881.DatumModalAnalysisAtAStiffness)

        @property
        def external_cad_model_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4883
            
            return self._parent._cast(_4883.ExternalCADModelModalAnalysisAtAStiffness)

        @property
        def face_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4885
            
            return self._parent._cast(_4885.FaceGearModalAnalysisAtAStiffness)

        @property
        def face_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4886
            
            return self._parent._cast(_4886.FaceGearSetModalAnalysisAtAStiffness)

        @property
        def fe_part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4887
            
            return self._parent._cast(_4887.FEPartModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4888
            
            return self._parent._cast(_4888.FlexiblePinAssemblyModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4890
            
            return self._parent._cast(_4890.GearModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4891
            
            return self._parent._cast(_4891.GearSetModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4892
            
            return self._parent._cast(_4892.GuideDxfModelModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4894
            
            return self._parent._cast(_4894.HypoidGearModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4895
            
            return self._parent._cast(_4895.HypoidGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4898
            
            return self._parent._cast(_4898.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4899
            
            return self._parent._cast(_4899.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4901
            
            return self._parent._cast(_4901.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4902
            
            return self._parent._cast(_4902.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4904
            
            return self._parent._cast(_4904.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4905
            
            return self._parent._cast(_4905.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def mass_disc_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4906
            
            return self._parent._cast(_4906.MassDiscModalAnalysisAtAStiffness)

        @property
        def measurement_component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4907
            
            return self._parent._cast(_4907.MeasurementComponentModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4908
            
            return self._parent._cast(_4908.MountableComponentModalAnalysisAtAStiffness)

        @property
        def oil_seal_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4909
            
            return self._parent._cast(_4909.OilSealModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4910
            
            return self._parent._cast(_4910.PartModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4912
            
            return self._parent._cast(_4912.PartToPartShearCouplingHalfModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4913
            
            return self._parent._cast(_4913.PartToPartShearCouplingModalAnalysisAtAStiffness)

        @property
        def planetary_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4915
            
            return self._parent._cast(_4915.PlanetaryGearSetModalAnalysisAtAStiffness)

        @property
        def planet_carrier_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4916
            
            return self._parent._cast(_4916.PlanetCarrierModalAnalysisAtAStiffness)

        @property
        def point_load_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4917
            
            return self._parent._cast(_4917.PointLoadModalAnalysisAtAStiffness)

        @property
        def power_load_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4918
            
            return self._parent._cast(_4918.PowerLoadModalAnalysisAtAStiffness)

        @property
        def pulley_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4919
            
            return self._parent._cast(_4919.PulleyModalAnalysisAtAStiffness)

        @property
        def ring_pins_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4920
            
            return self._parent._cast(_4920.RingPinsModalAnalysisAtAStiffness)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4922
            
            return self._parent._cast(_4922.RollingRingAssemblyModalAnalysisAtAStiffness)

        @property
        def rolling_ring_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4924
            
            return self._parent._cast(_4924.RollingRingModalAnalysisAtAStiffness)

        @property
        def root_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4925
            
            return self._parent._cast(_4925.RootAssemblyModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4926
            
            return self._parent._cast(_4926.ShaftHubConnectionModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4927
            
            return self._parent._cast(_4927.ShaftModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4929
            
            return self._parent._cast(_4929.SpecialisedAssemblyModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4931
            
            return self._parent._cast(_4931.SpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4932
            
            return self._parent._cast(_4932.SpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def spring_damper_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4934
            
            return self._parent._cast(_4934.SpringDamperHalfModalAnalysisAtAStiffness)

        @property
        def spring_damper_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4935
            
            return self._parent._cast(_4935.SpringDamperModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4937
            
            return self._parent._cast(_4937.StraightBevelDiffGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4938
            
            return self._parent._cast(_4938.StraightBevelDiffGearSetModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4940
            
            return self._parent._cast(_4940.StraightBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4941
            
            return self._parent._cast(_4941.StraightBevelGearSetModalAnalysisAtAStiffness)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4942
            
            return self._parent._cast(_4942.StraightBevelPlanetGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4943
            
            return self._parent._cast(_4943.StraightBevelSunGearModalAnalysisAtAStiffness)

        @property
        def synchroniser_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4944
            
            return self._parent._cast(_4944.SynchroniserHalfModalAnalysisAtAStiffness)

        @property
        def synchroniser_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4945
            
            return self._parent._cast(_4945.SynchroniserModalAnalysisAtAStiffness)

        @property
        def synchroniser_part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4946
            
            return self._parent._cast(_4946.SynchroniserPartModalAnalysisAtAStiffness)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4947
            
            return self._parent._cast(_4947.SynchroniserSleeveModalAnalysisAtAStiffness)

        @property
        def torque_converter_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4949
            
            return self._parent._cast(_4949.TorqueConverterModalAnalysisAtAStiffness)

        @property
        def torque_converter_pump_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4950
            
            return self._parent._cast(_4950.TorqueConverterPumpModalAnalysisAtAStiffness)

        @property
        def torque_converter_turbine_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4951
            
            return self._parent._cast(_4951.TorqueConverterTurbineModalAnalysisAtAStiffness)

        @property
        def unbalanced_mass_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4952
            
            return self._parent._cast(_4952.UnbalancedMassModalAnalysisAtAStiffness)

        @property
        def virtual_component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4953
            
            return self._parent._cast(_4953.VirtualComponentModalAnalysisAtAStiffness)

        @property
        def worm_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4955
            
            return self._parent._cast(_4955.WormGearModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4956
            
            return self._parent._cast(_4956.WormGearSetModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4958
            
            return self._parent._cast(_4958.ZerolBevelGearModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4959
            
            return self._parent._cast(_4959.ZerolBevelGearSetModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5089
            
            return self._parent._cast(_5089.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_shaft_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5090
            
            return self._parent._cast(_5090.AbstractShaftModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5091
            
            return self._parent._cast(_5091.AbstractShaftOrHousingModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5094
            
            return self._parent._cast(_5094.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5095
            
            return self._parent._cast(_5095.AGMAGleasonConicalGearSetModalAnalysisAtASpeed)

        @property
        def assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5096
            
            return self._parent._cast(_5096.AssemblyModalAnalysisAtASpeed)

        @property
        def bearing_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5097
            
            return self._parent._cast(_5097.BearingModalAnalysisAtASpeed)

        @property
        def belt_drive_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5099
            
            return self._parent._cast(_5099.BeltDriveModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5101
            
            return self._parent._cast(_5101.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5102
            
            return self._parent._cast(_5102.BevelDifferentialGearSetModalAnalysisAtASpeed)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5103
            
            return self._parent._cast(_5103.BevelDifferentialPlanetGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5104
            
            return self._parent._cast(_5104.BevelDifferentialSunGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5106
            
            return self._parent._cast(_5106.BevelGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5107
            
            return self._parent._cast(_5107.BevelGearSetModalAnalysisAtASpeed)

        @property
        def bolted_joint_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5108
            
            return self._parent._cast(_5108.BoltedJointModalAnalysisAtASpeed)

        @property
        def bolt_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5109
            
            return self._parent._cast(_5109.BoltModalAnalysisAtASpeed)

        @property
        def clutch_half_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5111
            
            return self._parent._cast(_5111.ClutchHalfModalAnalysisAtASpeed)

        @property
        def clutch_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5112
            
            return self._parent._cast(_5112.ClutchModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5114
            
            return self._parent._cast(_5114.ComponentModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5116
            
            return self._parent._cast(_5116.ConceptCouplingHalfModalAnalysisAtASpeed)

        @property
        def concept_coupling_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5117
            
            return self._parent._cast(_5117.ConceptCouplingModalAnalysisAtASpeed)

        @property
        def concept_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5119
            
            return self._parent._cast(_5119.ConceptGearModalAnalysisAtASpeed)

        @property
        def concept_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5120
            
            return self._parent._cast(_5120.ConceptGearSetModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5122
            
            return self._parent._cast(_5122.ConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5123
            
            return self._parent._cast(_5123.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def connector_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5125
            
            return self._parent._cast(_5125.ConnectorModalAnalysisAtASpeed)

        @property
        def coupling_half_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5127
            
            return self._parent._cast(_5127.CouplingHalfModalAnalysisAtASpeed)

        @property
        def coupling_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5128
            
            return self._parent._cast(_5128.CouplingModalAnalysisAtASpeed)

        @property
        def cvt_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5130
            
            return self._parent._cast(_5130.CVTModalAnalysisAtASpeed)

        @property
        def cvt_pulley_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5131
            
            return self._parent._cast(_5131.CVTPulleyModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5132
            
            return self._parent._cast(_5132.CycloidalAssemblyModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5134
            
            return self._parent._cast(_5134.CycloidalDiscModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5137
            
            return self._parent._cast(_5137.CylindricalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5138
            
            return self._parent._cast(_5138.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5139
            
            return self._parent._cast(_5139.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def datum_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5140
            
            return self._parent._cast(_5140.DatumModalAnalysisAtASpeed)

        @property
        def external_cad_model_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5141
            
            return self._parent._cast(_5141.ExternalCADModelModalAnalysisAtASpeed)

        @property
        def face_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5143
            
            return self._parent._cast(_5143.FaceGearModalAnalysisAtASpeed)

        @property
        def face_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5144
            
            return self._parent._cast(_5144.FaceGearSetModalAnalysisAtASpeed)

        @property
        def fe_part_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5145
            
            return self._parent._cast(_5145.FEPartModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5146
            
            return self._parent._cast(_5146.FlexiblePinAssemblyModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5148
            
            return self._parent._cast(_5148.GearModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5149
            
            return self._parent._cast(_5149.GearSetModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5150
            
            return self._parent._cast(_5150.GuideDxfModelModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5152
            
            return self._parent._cast(_5152.HypoidGearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5153
            
            return self._parent._cast(_5153.HypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5156
            
            return self._parent._cast(_5156.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5157
            
            return self._parent._cast(_5157.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5159
            
            return self._parent._cast(_5159.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5160
            
            return self._parent._cast(_5160.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5162
            
            return self._parent._cast(_5162.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5163
            
            return self._parent._cast(_5163.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def mass_disc_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5164
            
            return self._parent._cast(_5164.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5165
            
            return self._parent._cast(_5165.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5166
            
            return self._parent._cast(_5166.MountableComponentModalAnalysisAtASpeed)

        @property
        def oil_seal_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5167
            
            return self._parent._cast(_5167.OilSealModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5168
            
            return self._parent._cast(_5168.PartModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5170
            
            return self._parent._cast(_5170.PartToPartShearCouplingHalfModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5171
            
            return self._parent._cast(_5171.PartToPartShearCouplingModalAnalysisAtASpeed)

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5173
            
            return self._parent._cast(_5173.PlanetaryGearSetModalAnalysisAtASpeed)

        @property
        def planet_carrier_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5174
            
            return self._parent._cast(_5174.PlanetCarrierModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5175
            
            return self._parent._cast(_5175.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5176
            
            return self._parent._cast(_5176.PowerLoadModalAnalysisAtASpeed)

        @property
        def pulley_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5177
            
            return self._parent._cast(_5177.PulleyModalAnalysisAtASpeed)

        @property
        def ring_pins_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5178
            
            return self._parent._cast(_5178.RingPinsModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5180
            
            return self._parent._cast(_5180.RollingRingAssemblyModalAnalysisAtASpeed)

        @property
        def rolling_ring_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5182
            
            return self._parent._cast(_5182.RollingRingModalAnalysisAtASpeed)

        @property
        def root_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5183
            
            return self._parent._cast(_5183.RootAssemblyModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5184
            
            return self._parent._cast(_5184.ShaftHubConnectionModalAnalysisAtASpeed)

        @property
        def shaft_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5185
            
            return self._parent._cast(_5185.ShaftModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5187
            
            return self._parent._cast(_5187.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5189
            
            return self._parent._cast(_5189.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5190
            
            return self._parent._cast(_5190.SpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def spring_damper_half_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5192
            
            return self._parent._cast(_5192.SpringDamperHalfModalAnalysisAtASpeed)

        @property
        def spring_damper_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5193
            
            return self._parent._cast(_5193.SpringDamperModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5195
            
            return self._parent._cast(_5195.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5196
            
            return self._parent._cast(_5196.StraightBevelDiffGearSetModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5198
            
            return self._parent._cast(_5198.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5199
            
            return self._parent._cast(_5199.StraightBevelGearSetModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5200
            
            return self._parent._cast(_5200.StraightBevelPlanetGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5201
            
            return self._parent._cast(_5201.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def synchroniser_half_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5202
            
            return self._parent._cast(_5202.SynchroniserHalfModalAnalysisAtASpeed)

        @property
        def synchroniser_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5203
            
            return self._parent._cast(_5203.SynchroniserModalAnalysisAtASpeed)

        @property
        def synchroniser_part_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5204
            
            return self._parent._cast(_5204.SynchroniserPartModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5205
            
            return self._parent._cast(_5205.SynchroniserSleeveModalAnalysisAtASpeed)

        @property
        def torque_converter_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5207
            
            return self._parent._cast(_5207.TorqueConverterModalAnalysisAtASpeed)

        @property
        def torque_converter_pump_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5208
            
            return self._parent._cast(_5208.TorqueConverterPumpModalAnalysisAtASpeed)

        @property
        def torque_converter_turbine_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5209
            
            return self._parent._cast(_5209.TorqueConverterTurbineModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5210
            
            return self._parent._cast(_5210.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5211
            
            return self._parent._cast(_5211.VirtualComponentModalAnalysisAtASpeed)

        @property
        def worm_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5213
            
            return self._parent._cast(_5213.WormGearModalAnalysisAtASpeed)

        @property
        def worm_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5214
            
            return self._parent._cast(_5214.WormGearSetModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5216
            
            return self._parent._cast(_5216.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5217
            
            return self._parent._cast(_5217.ZerolBevelGearSetModalAnalysisAtASpeed)

        @property
        def abstract_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5347
            
            return self._parent._cast(_5347.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5348
            
            return self._parent._cast(_5348.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5349
            
            return self._parent._cast(_5349.AbstractShaftOrHousingMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5352
            
            return self._parent._cast(_5352.AGMAGleasonConicalGearMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5353
            
            return self._parent._cast(_5353.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5355
            
            return self._parent._cast(_5355.AssemblyMultibodyDynamicsAnalysis)

        @property
        def bearing_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5356
            
            return self._parent._cast(_5356.BearingMultibodyDynamicsAnalysis)

        @property
        def belt_drive_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5359
            
            return self._parent._cast(_5359.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5361
            
            return self._parent._cast(_5361.BevelDifferentialGearMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5362
            
            return self._parent._cast(_5362.BevelDifferentialGearSetMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5363
            
            return self._parent._cast(_5363.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5364
            
            return self._parent._cast(_5364.BevelDifferentialSunGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5366
            
            return self._parent._cast(_5366.BevelGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5367
            
            return self._parent._cast(_5367.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5368
            
            return self._parent._cast(_5368.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def bolt_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5369
            
            return self._parent._cast(_5369.BoltMultibodyDynamicsAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5371
            
            return self._parent._cast(_5371.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5372
            
            return self._parent._cast(_5372.ClutchMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5375
            
            return self._parent._cast(_5375.ComponentMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5377
            
            return self._parent._cast(_5377.ConceptCouplingHalfMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378
            
            return self._parent._cast(_5378.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5380
            
            return self._parent._cast(_5380.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5381
            
            return self._parent._cast(_5381.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5383
            
            return self._parent._cast(_5383.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384
            
            return self._parent._cast(_5384.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5386
            
            return self._parent._cast(_5386.ConnectorMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5388
            
            return self._parent._cast(_5388.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389
            
            return self._parent._cast(_5389.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5391
            
            return self._parent._cast(_5391.CVTMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392
            
            return self._parent._cast(_5392.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393
            
            return self._parent._cast(_5393.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5395
            
            return self._parent._cast(_5395.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398
            
            return self._parent._cast(_5398.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399
            
            return self._parent._cast(_5399.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400
            
            return self._parent._cast(_5400.CylindricalPlanetGearMultibodyDynamicsAnalysis)

        @property
        def datum_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401
            
            return self._parent._cast(_5401.DatumMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5402
            
            return self._parent._cast(_5402.ExternalCADModelMultibodyDynamicsAnalysis)

        @property
        def face_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404
            
            return self._parent._cast(_5404.FaceGearMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5405
            
            return self._parent._cast(_5405.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def fe_part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406
            
            return self._parent._cast(_5406.FEPartMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407
            
            return self._parent._cast(_5407.FlexiblePinAssemblyMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410
            
            return self._parent._cast(_5410.GearMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411
            
            return self._parent._cast(_5411.GearSetMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412
            
            return self._parent._cast(_5412.GuideDxfModelMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414
            
            return self._parent._cast(_5414.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415
            
            return self._parent._cast(_5415.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422
            
            return self._parent._cast(_5422.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5423
            
            return self._parent._cast(_5423.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425
            
            return self._parent._cast(_5425.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5426
            
            return self._parent._cast(_5426.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428
            
            return self._parent._cast(_5428.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5429
            
            return self._parent._cast(_5429.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def mass_disc_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430
            
            return self._parent._cast(_5430.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5434
            
            return self._parent._cast(_5434.MeasurementComponentMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435
            
            return self._parent._cast(_5435.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def oil_seal_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436
            
            return self._parent._cast(_5436.OilSealMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437
            
            return self._parent._cast(_5437.PartMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439
            
            return self._parent._cast(_5439.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440
            
            return self._parent._cast(_5440.PartToPartShearCouplingMultibodyDynamicsAnalysis)

        @property
        def planetary_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5442
            
            return self._parent._cast(_5442.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def planet_carrier_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5443
            
            return self._parent._cast(_5443.PlanetCarrierMultibodyDynamicsAnalysis)

        @property
        def point_load_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5444
            
            return self._parent._cast(_5444.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445
            
            return self._parent._cast(_5445.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def pulley_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5446
            
            return self._parent._cast(_5446.PulleyMultibodyDynamicsAnalysis)

        @property
        def ring_pins_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5447
            
            return self._parent._cast(_5447.RingPinsMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449
            
            return self._parent._cast(_5449.RollingRingAssemblyMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451
            
            return self._parent._cast(_5451.RollingRingMultibodyDynamicsAnalysis)

        @property
        def root_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452
            
            return self._parent._cast(_5452.RootAssemblyMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455
            
            return self._parent._cast(_5455.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5456
            
            return self._parent._cast(_5456.ShaftMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5459
            
            return self._parent._cast(_5459.SpecialisedAssemblyMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461
            
            return self._parent._cast(_5461.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5462
            
            return self._parent._cast(_5462.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464
            
            return self._parent._cast(_5464.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5465
            
            return self._parent._cast(_5465.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467
            
            return self._parent._cast(_5467.StraightBevelDiffGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5468
            
            return self._parent._cast(_5468.StraightBevelDiffGearSetMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470
            
            return self._parent._cast(_5470.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471
            
            return self._parent._cast(_5471.StraightBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472
            
            return self._parent._cast(_5472.StraightBevelPlanetGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473
            
            return self._parent._cast(_5473.StraightBevelSunGearMultibodyDynamicsAnalysis)

        @property
        def synchroniser_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5474
            
            return self._parent._cast(_5474.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475
            
            return self._parent._cast(_5475.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476
            
            return self._parent._cast(_5476.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477
            
            return self._parent._cast(_5477.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5480
            
            return self._parent._cast(_5480.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5481
            
            return self._parent._cast(_5481.TorqueConverterPumpMultibodyDynamicsAnalysis)

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5483
            
            return self._parent._cast(_5483.TorqueConverterTurbineMultibodyDynamicsAnalysis)

        @property
        def unbalanced_mass_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5484
            
            return self._parent._cast(_5484.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485
            
            return self._parent._cast(_5485.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488
            
            return self._parent._cast(_5488.WormGearMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489
            
            return self._parent._cast(_5489.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491
            
            return self._parent._cast(_5491.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492
            
            return self._parent._cast(_5492.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5648
            
            return self._parent._cast(_5648.AbstractAssemblyHarmonicAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5650
            
            return self._parent._cast(_5650.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5651
            
            return self._parent._cast(_5651.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5653
            
            return self._parent._cast(_5653.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5655
            
            return self._parent._cast(_5655.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5656
            
            return self._parent._cast(_5656.AssemblyHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5657
            
            return self._parent._cast(_5657.BearingHarmonicAnalysis)

        @property
        def belt_drive_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5659
            
            return self._parent._cast(_5659.BeltDriveHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5660
            
            return self._parent._cast(_5660.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5662
            
            return self._parent._cast(_5662.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5663
            
            return self._parent._cast(_5663.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5664
            
            return self._parent._cast(_5664.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5665
            
            return self._parent._cast(_5665.BevelGearHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5667
            
            return self._parent._cast(_5667.BevelGearSetHarmonicAnalysis)

        @property
        def bolted_joint_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5668
            
            return self._parent._cast(_5668.BoltedJointHarmonicAnalysis)

        @property
        def bolt_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5669
            
            return self._parent._cast(_5669.BoltHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5671
            
            return self._parent._cast(_5671.ClutchHalfHarmonicAnalysis)

        @property
        def clutch_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5672
            
            return self._parent._cast(_5672.ClutchHarmonicAnalysis)

        @property
        def component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5675
            
            return self._parent._cast(_5675.ComponentHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5677
            
            return self._parent._cast(_5677.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5678
            
            return self._parent._cast(_5678.ConceptCouplingHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5679
            
            return self._parent._cast(_5679.ConceptGearHarmonicAnalysis)

        @property
        def concept_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5681
            
            return self._parent._cast(_5681.ConceptGearSetHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5682
            
            return self._parent._cast(_5682.ConicalGearHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5684
            
            return self._parent._cast(_5684.ConicalGearSetHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5686
            
            return self._parent._cast(_5686.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5688
            
            return self._parent._cast(_5688.CouplingHalfHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5689
            
            return self._parent._cast(_5689.CouplingHarmonicAnalysis)

        @property
        def cvt_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5691
            
            return self._parent._cast(_5691.CVTHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5692
            
            return self._parent._cast(_5692.CVTPulleyHarmonicAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5693
            
            return self._parent._cast(_5693.CycloidalAssemblyHarmonicAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5695
            
            return self._parent._cast(_5695.CycloidalDiscHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5697
            
            return self._parent._cast(_5697.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5699
            
            return self._parent._cast(_5699.CylindricalGearSetHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5700
            
            return self._parent._cast(_5700.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def datum_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5701
            
            return self._parent._cast(_5701.DatumHarmonicAnalysis)

        @property
        def external_cad_model_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5715
            
            return self._parent._cast(_5715.ExternalCADModelHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5716
            
            return self._parent._cast(_5716.FaceGearHarmonicAnalysis)

        @property
        def face_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5718
            
            return self._parent._cast(_5718.FaceGearSetHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5719
            
            return self._parent._cast(_5719.FEPartHarmonicAnalysis)

        @property
        def flexible_pin_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5720
            
            return self._parent._cast(_5720.FlexiblePinAssemblyHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5722
            
            return self._parent._cast(_5722.GearHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5727
            
            return self._parent._cast(_5727.GearSetHarmonicAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5729
            
            return self._parent._cast(_5729.GuideDxfModelHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5738
            
            return self._parent._cast(_5738.HypoidGearHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5740
            
            return self._parent._cast(_5740.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5742
            
            return self._parent._cast(_5742.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5744
            
            return self._parent._cast(_5744.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5745
            
            return self._parent._cast(_5745.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5747
            
            return self._parent._cast(_5747.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5748
            
            return self._parent._cast(_5748.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5750
            
            return self._parent._cast(_5750.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis)

        @property
        def mass_disc_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5751
            
            return self._parent._cast(_5751.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5752
            
            return self._parent._cast(_5752.MeasurementComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5753
            
            return self._parent._cast(_5753.MountableComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5754
            
            return self._parent._cast(_5754.OilSealHarmonicAnalysis)

        @property
        def part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5755
            
            return self._parent._cast(_5755.PartHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5757
            
            return self._parent._cast(_5757.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5758
            
            return self._parent._cast(_5758.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5761
            
            return self._parent._cast(_5761.PlanetaryGearSetHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5762
            
            return self._parent._cast(_5762.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5763
            
            return self._parent._cast(_5763.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5764
            
            return self._parent._cast(_5764.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5765
            
            return self._parent._cast(_5765.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5767
            
            return self._parent._cast(_5767.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5769
            
            return self._parent._cast(_5769.RollingRingAssemblyHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5771
            
            return self._parent._cast(_5771.RollingRingHarmonicAnalysis)

        @property
        def root_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5772
            
            return self._parent._cast(_5772.RootAssemblyHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5773
            
            return self._parent._cast(_5773.ShaftHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5774
            
            return self._parent._cast(_5774.ShaftHubConnectionHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5777
            
            return self._parent._cast(_5777.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5779
            
            return self._parent._cast(_5779.SpiralBevelGearHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5781
            
            return self._parent._cast(_5781.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5783
            
            return self._parent._cast(_5783.SpringDamperHalfHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5784
            
            return self._parent._cast(_5784.SpringDamperHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5786
            
            return self._parent._cast(_5786.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5788
            
            return self._parent._cast(_5788.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5789
            
            return self._parent._cast(_5789.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5791
            
            return self._parent._cast(_5791.StraightBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5792
            
            return self._parent._cast(_5792.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5793
            
            return self._parent._cast(_5793.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5794
            
            return self._parent._cast(_5794.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5795
            
            return self._parent._cast(_5795.SynchroniserHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5796
            
            return self._parent._cast(_5796.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5797
            
            return self._parent._cast(_5797.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5799
            
            return self._parent._cast(_5799.TorqueConverterHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5800
            
            return self._parent._cast(_5800.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5801
            
            return self._parent._cast(_5801.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5803
            
            return self._parent._cast(_5803.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5804
            
            return self._parent._cast(_5804.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5805
            
            return self._parent._cast(_5805.WormGearHarmonicAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807
            
            return self._parent._cast(_5807.WormGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5808
            
            return self._parent._cast(_5808.ZerolBevelGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5810
            
            return self._parent._cast(_5810.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5975
            
            return self._parent._cast(_5975.AbstractAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5976
            
            return self._parent._cast(_5976.AbstractShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5977
            
            return self._parent._cast(_5977.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5979
            
            return self._parent._cast(_5979.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5981
            
            return self._parent._cast(_5981.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5982
            
            return self._parent._cast(_5982.AssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def bearing_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5983
            
            return self._parent._cast(_5983.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5985
            
            return self._parent._cast(_5985.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5986
            
            return self._parent._cast(_5986.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5988
            
            return self._parent._cast(_5988.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5989
            
            return self._parent._cast(_5989.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5990
            
            return self._parent._cast(_5990.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5991
            
            return self._parent._cast(_5991.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5993
            
            return self._parent._cast(_5993.BevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5994
            
            return self._parent._cast(_5994.BoltedJointHarmonicAnalysisOfSingleExcitation)

        @property
        def bolt_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5995
            
            return self._parent._cast(_5995.BoltHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5997
            
            return self._parent._cast(_5997.ClutchHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5998
            
            return self._parent._cast(_5998.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6000
            
            return self._parent._cast(_6000.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6002
            
            return self._parent._cast(_6002.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6003
            
            return self._parent._cast(_6003.ConceptCouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6004
            
            return self._parent._cast(_6004.ConceptGearHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6006
            
            return self._parent._cast(_6006.ConceptGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6007
            
            return self._parent._cast(_6007.ConicalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6009
            
            return self._parent._cast(_6009.ConicalGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def connector_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6011
            
            return self._parent._cast(_6011.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6013
            
            return self._parent._cast(_6013.CouplingHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6014
            
            return self._parent._cast(_6014.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6016
            
            return self._parent._cast(_6016.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6017
            
            return self._parent._cast(_6017.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6018
            
            return self._parent._cast(_6018.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6020
            
            return self._parent._cast(_6020.CycloidalDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6022
            
            return self._parent._cast(_6022.CylindricalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6024
            
            return self._parent._cast(_6024.CylindricalGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6025
            
            return self._parent._cast(_6025.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation)

        @property
        def datum_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6026
            
            return self._parent._cast(_6026.DatumHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6027
            
            return self._parent._cast(_6027.ExternalCADModelHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6028
            
            return self._parent._cast(_6028.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6030
            
            return self._parent._cast(_6030.FaceGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def fe_part_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6031
            
            return self._parent._cast(_6031.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6032
            
            return self._parent._cast(_6032.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6033
            
            return self._parent._cast(_6033.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6035
            
            return self._parent._cast(_6035.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6036
            
            return self._parent._cast(_6036.GuideDxfModelHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6038
            
            return self._parent._cast(_6038.HypoidGearHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6040
            
            return self._parent._cast(_6040.HypoidGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6042
            
            return self._parent._cast(_6042.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6044
            
            return self._parent._cast(_6044.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6045
            
            return self._parent._cast(_6045.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6047
            
            return self._parent._cast(_6047.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6048
            
            return self._parent._cast(_6048.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6050
            
            return self._parent._cast(_6050.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6051
            
            return self._parent._cast(_6051.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6052
            
            return self._parent._cast(_6052.MeasurementComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6053
            
            return self._parent._cast(_6053.MountableComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6054
            
            return self._parent._cast(_6054.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6055
            
            return self._parent._cast(_6055.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6057
            
            return self._parent._cast(_6057.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6058
            
            return self._parent._cast(_6058.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6060
            
            return self._parent._cast(_6060.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6061
            
            return self._parent._cast(_6061.PlanetCarrierHarmonicAnalysisOfSingleExcitation)

        @property
        def point_load_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6062
            
            return self._parent._cast(_6062.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6063
            
            return self._parent._cast(_6063.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6064
            
            return self._parent._cast(_6064.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6065
            
            return self._parent._cast(_6065.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6067
            
            return self._parent._cast(_6067.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6069
            
            return self._parent._cast(_6069.RollingRingHarmonicAnalysisOfSingleExcitation)

        @property
        def root_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6070
            
            return self._parent._cast(_6070.RootAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6071
            
            return self._parent._cast(_6071.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6072
            
            return self._parent._cast(_6072.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6074
            
            return self._parent._cast(_6074.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6075
            
            return self._parent._cast(_6075.SpiralBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6077
            
            return self._parent._cast(_6077.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6079
            
            return self._parent._cast(_6079.SpringDamperHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6080
            
            return self._parent._cast(_6080.SpringDamperHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6081
            
            return self._parent._cast(_6081.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6083
            
            return self._parent._cast(_6083.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6084
            
            return self._parent._cast(_6084.StraightBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6086
            
            return self._parent._cast(_6086.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6087
            
            return self._parent._cast(_6087.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6088
            
            return self._parent._cast(_6088.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6089
            
            return self._parent._cast(_6089.SynchroniserHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6090
            
            return self._parent._cast(_6090.SynchroniserHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6091
            
            return self._parent._cast(_6091.SynchroniserPartHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6092
            
            return self._parent._cast(_6092.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6094
            
            return self._parent._cast(_6094.TorqueConverterHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6095
            
            return self._parent._cast(_6095.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation)

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6096
            
            return self._parent._cast(_6096.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation)

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6097
            
            return self._parent._cast(_6097.UnbalancedMassHarmonicAnalysisOfSingleExcitation)

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6098
            
            return self._parent._cast(_6098.VirtualComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6099
            
            return self._parent._cast(_6099.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6101
            
            return self._parent._cast(_6101.WormGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6102
            
            return self._parent._cast(_6102.ZerolBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6104
            
            return self._parent._cast(_6104.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation)

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
        def abstract_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6508
            
            return self._parent._cast(_6508.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_shaft_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6509
            
            return self._parent._cast(_6509.AbstractShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6510
            
            return self._parent._cast(_6510.AbstractShaftOrHousingCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6512
            
            return self._parent._cast(_6512.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6514
            
            return self._parent._cast(_6514.AGMAGleasonConicalGearSetCriticalSpeedAnalysis)

        @property
        def assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6515
            
            return self._parent._cast(_6515.AssemblyCriticalSpeedAnalysis)

        @property
        def bearing_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6516
            
            return self._parent._cast(_6516.BearingCriticalSpeedAnalysis)

        @property
        def belt_drive_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6518
            
            return self._parent._cast(_6518.BeltDriveCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6519
            
            return self._parent._cast(_6519.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6521
            
            return self._parent._cast(_6521.BevelDifferentialGearSetCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6522
            
            return self._parent._cast(_6522.BevelDifferentialPlanetGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6523
            
            return self._parent._cast(_6523.BevelDifferentialSunGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6524
            
            return self._parent._cast(_6524.BevelGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6526
            
            return self._parent._cast(_6526.BevelGearSetCriticalSpeedAnalysis)

        @property
        def bolt_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6527
            
            return self._parent._cast(_6527.BoltCriticalSpeedAnalysis)

        @property
        def bolted_joint_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6528
            
            return self._parent._cast(_6528.BoltedJointCriticalSpeedAnalysis)

        @property
        def clutch_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6530
            
            return self._parent._cast(_6530.ClutchCriticalSpeedAnalysis)

        @property
        def clutch_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6531
            
            return self._parent._cast(_6531.ClutchHalfCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6533
            
            return self._parent._cast(_6533.ComponentCriticalSpeedAnalysis)

        @property
        def concept_coupling_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6535
            
            return self._parent._cast(_6535.ConceptCouplingCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6536
            
            return self._parent._cast(_6536.ConceptCouplingHalfCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6537
            
            return self._parent._cast(_6537.ConceptGearCriticalSpeedAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6539
            
            return self._parent._cast(_6539.ConceptGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6540
            
            return self._parent._cast(_6540.ConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6542
            
            return self._parent._cast(_6542.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def connector_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6544
            
            return self._parent._cast(_6544.ConnectorCriticalSpeedAnalysis)

        @property
        def coupling_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6546
            
            return self._parent._cast(_6546.CouplingCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6547
            
            return self._parent._cast(_6547.CouplingHalfCriticalSpeedAnalysis)

        @property
        def cvt_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6551
            
            return self._parent._cast(_6551.CVTCriticalSpeedAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6552
            
            return self._parent._cast(_6552.CVTPulleyCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6553
            
            return self._parent._cast(_6553.CycloidalAssemblyCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6555
            
            return self._parent._cast(_6555.CycloidalDiscCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6557
            
            return self._parent._cast(_6557.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6559
            
            return self._parent._cast(_6559.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6560
            
            return self._parent._cast(_6560.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def datum_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6561
            
            return self._parent._cast(_6561.DatumCriticalSpeedAnalysis)

        @property
        def external_cad_model_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6562
            
            return self._parent._cast(_6562.ExternalCADModelCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6563
            
            return self._parent._cast(_6563.FaceGearCriticalSpeedAnalysis)

        @property
        def face_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6565
            
            return self._parent._cast(_6565.FaceGearSetCriticalSpeedAnalysis)

        @property
        def fe_part_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6566
            
            return self._parent._cast(_6566.FEPartCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6567
            
            return self._parent._cast(_6567.FlexiblePinAssemblyCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6568
            
            return self._parent._cast(_6568.GearCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6570
            
            return self._parent._cast(_6570.GearSetCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6571
            
            return self._parent._cast(_6571.GuideDxfModelCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6572
            
            return self._parent._cast(_6572.HypoidGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6574
            
            return self._parent._cast(_6574.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6576
            
            return self._parent._cast(_6576.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6578
            
            return self._parent._cast(_6578.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6579
            
            return self._parent._cast(_6579.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6581
            
            return self._parent._cast(_6581.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6582
            
            return self._parent._cast(_6582.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6584
            
            return self._parent._cast(_6584.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def mass_disc_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6585
            
            return self._parent._cast(_6585.MassDiscCriticalSpeedAnalysis)

        @property
        def measurement_component_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6586
            
            return self._parent._cast(_6586.MeasurementComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6587
            
            return self._parent._cast(_6587.MountableComponentCriticalSpeedAnalysis)

        @property
        def oil_seal_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6588
            
            return self._parent._cast(_6588.OilSealCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6589
            
            return self._parent._cast(_6589.PartCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6591
            
            return self._parent._cast(_6591.PartToPartShearCouplingCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6592
            
            return self._parent._cast(_6592.PartToPartShearCouplingHalfCriticalSpeedAnalysis)

        @property
        def planetary_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6594
            
            return self._parent._cast(_6594.PlanetaryGearSetCriticalSpeedAnalysis)

        @property
        def planet_carrier_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6595
            
            return self._parent._cast(_6595.PlanetCarrierCriticalSpeedAnalysis)

        @property
        def point_load_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6596
            
            return self._parent._cast(_6596.PointLoadCriticalSpeedAnalysis)

        @property
        def power_load_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6597
            
            return self._parent._cast(_6597.PowerLoadCriticalSpeedAnalysis)

        @property
        def pulley_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6598
            
            return self._parent._cast(_6598.PulleyCriticalSpeedAnalysis)

        @property
        def ring_pins_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6599
            
            return self._parent._cast(_6599.RingPinsCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6601
            
            return self._parent._cast(_6601.RollingRingAssemblyCriticalSpeedAnalysis)

        @property
        def rolling_ring_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6603
            
            return self._parent._cast(_6603.RollingRingCriticalSpeedAnalysis)

        @property
        def root_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6604
            
            return self._parent._cast(_6604.RootAssemblyCriticalSpeedAnalysis)

        @property
        def shaft_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6605
            
            return self._parent._cast(_6605.ShaftCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6606
            
            return self._parent._cast(_6606.ShaftHubConnectionCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6608
            
            return self._parent._cast(_6608.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6609
            
            return self._parent._cast(_6609.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6611
            
            return self._parent._cast(_6611.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def spring_damper_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6613
            
            return self._parent._cast(_6613.SpringDamperCriticalSpeedAnalysis)

        @property
        def spring_damper_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6614
            
            return self._parent._cast(_6614.SpringDamperHalfCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6615
            
            return self._parent._cast(_6615.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6617
            
            return self._parent._cast(_6617.StraightBevelDiffGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6618
            
            return self._parent._cast(_6618.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6620
            
            return self._parent._cast(_6620.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6621
            
            return self._parent._cast(_6621.StraightBevelPlanetGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6622
            
            return self._parent._cast(_6622.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def synchroniser_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6623
            
            return self._parent._cast(_6623.SynchroniserCriticalSpeedAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6624
            
            return self._parent._cast(_6624.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6625
            
            return self._parent._cast(_6625.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6626
            
            return self._parent._cast(_6626.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def torque_converter_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6628
            
            return self._parent._cast(_6628.TorqueConverterCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6629
            
            return self._parent._cast(_6629.TorqueConverterPumpCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6630
            
            return self._parent._cast(_6630.TorqueConverterTurbineCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6631
            
            return self._parent._cast(_6631.UnbalancedMassCriticalSpeedAnalysis)

        @property
        def virtual_component_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6632
            
            return self._parent._cast(_6632.VirtualComponentCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6633
            
            return self._parent._cast(_6633.WormGearCriticalSpeedAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6635
            
            return self._parent._cast(_6635.WormGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6636
            
            return self._parent._cast(_6636.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6638
            
            return self._parent._cast(_6638.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def abstract_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6771
            
            return self._parent._cast(_6771.AbstractAssemblyLoadCase)

        @property
        def abstract_shaft_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6772
            
            return self._parent._cast(_6772.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6773
            
            return self._parent._cast(_6773.AbstractShaftOrHousingLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6778
            
            return self._parent._cast(_6778.AGMAGleasonConicalGearLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6780
            
            return self._parent._cast(_6780.AGMAGleasonConicalGearSetLoadCase)

        @property
        def assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6783
            
            return self._parent._cast(_6783.AssemblyLoadCase)

        @property
        def bearing_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6784
            
            return self._parent._cast(_6784.BearingLoadCase)

        @property
        def belt_drive_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6786
            
            return self._parent._cast(_6786.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6787
            
            return self._parent._cast(_6787.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6789
            
            return self._parent._cast(_6789.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6790
            
            return self._parent._cast(_6790.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6791
            
            return self._parent._cast(_6791.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6792
            
            return self._parent._cast(_6792.BevelGearLoadCase)

        @property
        def bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6794
            
            return self._parent._cast(_6794.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6795
            
            return self._parent._cast(_6795.BoltedJointLoadCase)

        @property
        def bolt_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6796
            
            return self._parent._cast(_6796.BoltLoadCase)

        @property
        def clutch_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6798
            
            return self._parent._cast(_6798.ClutchHalfLoadCase)

        @property
        def clutch_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6799
            
            return self._parent._cast(_6799.ClutchLoadCase)

        @property
        def component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6801
            
            return self._parent._cast(_6801.ComponentLoadCase)

        @property
        def concept_coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6803
            
            return self._parent._cast(_6803.ConceptCouplingHalfLoadCase)

        @property
        def concept_coupling_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6804
            
            return self._parent._cast(_6804.ConceptCouplingLoadCase)

        @property
        def concept_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6805
            
            return self._parent._cast(_6805.ConceptGearLoadCase)

        @property
        def concept_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6807
            
            return self._parent._cast(_6807.ConceptGearSetLoadCase)

        @property
        def conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6808
            
            return self._parent._cast(_6808.ConicalGearLoadCase)

        @property
        def conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6812
            
            return self._parent._cast(_6812.ConicalGearSetLoadCase)

        @property
        def connector_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6814
            
            return self._parent._cast(_6814.ConnectorLoadCase)

        @property
        def coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6816
            
            return self._parent._cast(_6816.CouplingHalfLoadCase)

        @property
        def coupling_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6817
            
            return self._parent._cast(_6817.CouplingLoadCase)

        @property
        def cvt_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6819
            
            return self._parent._cast(_6819.CVTLoadCase)

        @property
        def cvt_pulley_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6820
            
            return self._parent._cast(_6820.CVTPulleyLoadCase)

        @property
        def cycloidal_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6821
            
            return self._parent._cast(_6821.CycloidalAssemblyLoadCase)

        @property
        def cycloidal_disc_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6823
            
            return self._parent._cast(_6823.CycloidalDiscLoadCase)

        @property
        def cylindrical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6825
            
            return self._parent._cast(_6825.CylindricalGearLoadCase)

        @property
        def cylindrical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6829
            
            return self._parent._cast(_6829.CylindricalGearSetLoadCase)

        @property
        def cylindrical_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6830
            
            return self._parent._cast(_6830.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6833
            
            return self._parent._cast(_6833.DatumLoadCase)

        @property
        def external_cad_model_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6847
            
            return self._parent._cast(_6847.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6848
            
            return self._parent._cast(_6848.FaceGearLoadCase)

        @property
        def face_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6850
            
            return self._parent._cast(_6850.FaceGearSetLoadCase)

        @property
        def fe_part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6851
            
            return self._parent._cast(_6851.FEPartLoadCase)

        @property
        def flexible_pin_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6852
            
            return self._parent._cast(_6852.FlexiblePinAssemblyLoadCase)

        @property
        def gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6854
            
            return self._parent._cast(_6854.GearLoadCase)

        @property
        def gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6859
            
            return self._parent._cast(_6859.GearSetLoadCase)

        @property
        def guide_dxf_model_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6860
            
            return self._parent._cast(_6860.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6869
            
            return self._parent._cast(_6869.HypoidGearLoadCase)

        @property
        def hypoid_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6871
            
            return self._parent._cast(_6871.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6876
            
            return self._parent._cast(_6876.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6878
            
            return self._parent._cast(_6878.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6879
            
            return self._parent._cast(_6879.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6881
            
            return self._parent._cast(_6881.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6882
            
            return self._parent._cast(_6882.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6884
            
            return self._parent._cast(_6884.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        @property
        def mass_disc_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6885
            
            return self._parent._cast(_6885.MassDiscLoadCase)

        @property
        def measurement_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6886
            
            return self._parent._cast(_6886.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6888
            
            return self._parent._cast(_6888.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6890
            
            return self._parent._cast(_6890.OilSealLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.PartLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6894
            
            return self._parent._cast(_6894.PartToPartShearCouplingHalfLoadCase)

        @property
        def part_to_part_shear_coupling_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6895
            
            return self._parent._cast(_6895.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6897
            
            return self._parent._cast(_6897.PlanetaryGearSetLoadCase)

        @property
        def planet_carrier_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6899
            
            return self._parent._cast(_6899.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6902
            
            return self._parent._cast(_6902.PointLoadLoadCase)

        @property
        def power_load_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6903
            
            return self._parent._cast(_6903.PowerLoadLoadCase)

        @property
        def pulley_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6904
            
            return self._parent._cast(_6904.PulleyLoadCase)

        @property
        def ring_pins_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6907
            
            return self._parent._cast(_6907.RingPinsLoadCase)

        @property
        def rolling_ring_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6909
            
            return self._parent._cast(_6909.RollingRingAssemblyLoadCase)

        @property
        def rolling_ring_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6911
            
            return self._parent._cast(_6911.RollingRingLoadCase)

        @property
        def root_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6912
            
            return self._parent._cast(_6912.RootAssemblyLoadCase)

        @property
        def shaft_hub_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6913
            
            return self._parent._cast(_6913.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6914
            
            return self._parent._cast(_6914.ShaftLoadCase)

        @property
        def specialised_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6916
            
            return self._parent._cast(_6916.SpecialisedAssemblyLoadCase)

        @property
        def spiral_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6917
            
            return self._parent._cast(_6917.SpiralBevelGearLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6919
            
            return self._parent._cast(_6919.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6921
            
            return self._parent._cast(_6921.SpringDamperHalfLoadCase)

        @property
        def spring_damper_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6922
            
            return self._parent._cast(_6922.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6923
            
            return self._parent._cast(_6923.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6925
            
            return self._parent._cast(_6925.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6926
            
            return self._parent._cast(_6926.StraightBevelGearLoadCase)

        @property
        def straight_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6928
            
            return self._parent._cast(_6928.StraightBevelGearSetLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6929
            
            return self._parent._cast(_6929.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6930
            
            return self._parent._cast(_6930.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6931
            
            return self._parent._cast(_6931.SynchroniserHalfLoadCase)

        @property
        def synchroniser_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6932
            
            return self._parent._cast(_6932.SynchroniserLoadCase)

        @property
        def synchroniser_part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6933
            
            return self._parent._cast(_6933.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6934
            
            return self._parent._cast(_6934.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6937
            
            return self._parent._cast(_6937.TorqueConverterLoadCase)

        @property
        def torque_converter_pump_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6938
            
            return self._parent._cast(_6938.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6939
            
            return self._parent._cast(_6939.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6944
            
            return self._parent._cast(_6944.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6945
            
            return self._parent._cast(_6945.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6946
            
            return self._parent._cast(_6946.WormGearLoadCase)

        @property
        def worm_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6948
            
            return self._parent._cast(_6948.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6949
            
            return self._parent._cast(_6949.ZerolBevelGearLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6951
            
            return self._parent._cast(_6951.ZerolBevelGearSetLoadCase)

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6969
            
            return self._parent._cast(_6969.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6970
            
            return self._parent._cast(_6970.AbstractShaftAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6971
            
            return self._parent._cast(_6971.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6976
            
            return self._parent._cast(_6976.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6978
            
            return self._parent._cast(_6978.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6979
            
            return self._parent._cast(_6979.AssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bearing_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6981
            
            return self._parent._cast(_6981.BearingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6983
            
            return self._parent._cast(_6983.BeltDriveAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6984
            
            return self._parent._cast(_6984.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6986
            
            return self._parent._cast(_6986.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6987
            
            return self._parent._cast(_6987.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6988
            
            return self._parent._cast(_6988.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6989
            
            return self._parent._cast(_6989.BevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6991
            
            return self._parent._cast(_6991.BevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bolt_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6992
            
            return self._parent._cast(_6992.BoltAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bolted_joint_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6993
            
            return self._parent._cast(_6993.BoltedJointAdvancedTimeSteppingAnalysisForModulation)

        @property
        def clutch_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6994
            
            return self._parent._cast(_6994.ClutchAdvancedTimeSteppingAnalysisForModulation)

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6996
            
            return self._parent._cast(_6996.ClutchHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def component_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6998
            
            return self._parent._cast(_6998.ComponentAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6999
            
            return self._parent._cast(_6999.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7001
            
            return self._parent._cast(_7001.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7002
            
            return self._parent._cast(_7002.ConceptGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7004
            
            return self._parent._cast(_7004.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7005
            
            return self._parent._cast(_7005.ConicalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7007
            
            return self._parent._cast(_7007.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7009
            
            return self._parent._cast(_7009.ConnectorAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7010
            
            return self._parent._cast(_7010.CouplingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7012
            
            return self._parent._cast(_7012.CouplingHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7013
            
            return self._parent._cast(_7013.CVTAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7015
            
            return self._parent._cast(_7015.CVTPulleyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7016
            
            return self._parent._cast(_7016.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7017
            
            return self._parent._cast(_7017.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7020
            
            return self._parent._cast(_7020.CylindricalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7022
            
            return self._parent._cast(_7022.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7023
            
            return self._parent._cast(_7023.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def datum_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7024
            
            return self._parent._cast(_7024.DatumAdvancedTimeSteppingAnalysisForModulation)

        @property
        def external_cad_model_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7025
            
            return self._parent._cast(_7025.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7026
            
            return self._parent._cast(_7026.FaceGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7028
            
            return self._parent._cast(_7028.FaceGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def fe_part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7029
            
            return self._parent._cast(_7029.FEPartAdvancedTimeSteppingAnalysisForModulation)

        @property
        def flexible_pin_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7030
            
            return self._parent._cast(_7030.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7031
            
            return self._parent._cast(_7031.GearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7033
            
            return self._parent._cast(_7033.GearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def guide_dxf_model_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7034
            
            return self._parent._cast(_7034.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7036
            
            return self._parent._cast(_7036.HypoidGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7038
            
            return self._parent._cast(_7038.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7040
            
            return self._parent._cast(_7040.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7042
            
            return self._parent._cast(_7042.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7043
            
            return self._parent._cast(_7043.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7045
            
            return self._parent._cast(_7045.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7046
            
            return self._parent._cast(_7046.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7048
            
            return self._parent._cast(_7048.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def mass_disc_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7049
            
            return self._parent._cast(_7049.MassDiscAdvancedTimeSteppingAnalysisForModulation)

        @property
        def measurement_component_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7050
            
            return self._parent._cast(_7050.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation)

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7051
            
            return self._parent._cast(_7051.MountableComponentAdvancedTimeSteppingAnalysisForModulation)

        @property
        def oil_seal_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7052
            
            return self._parent._cast(_7052.OilSealAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7053
            
            return self._parent._cast(_7053.PartAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7054
            
            return self._parent._cast(_7054.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7056
            
            return self._parent._cast(_7056.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7058
            
            return self._parent._cast(_7058.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planet_carrier_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7059
            
            return self._parent._cast(_7059.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation)

        @property
        def point_load_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7060
            
            return self._parent._cast(_7060.PointLoadAdvancedTimeSteppingAnalysisForModulation)

        @property
        def power_load_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7061
            
            return self._parent._cast(_7061.PowerLoadAdvancedTimeSteppingAnalysisForModulation)

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7062
            
            return self._parent._cast(_7062.PulleyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def ring_pins_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7063
            
            return self._parent._cast(_7063.RingPinsAdvancedTimeSteppingAnalysisForModulation)

        @property
        def rolling_ring_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7065
            
            return self._parent._cast(_7065.RollingRingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7066
            
            return self._parent._cast(_7066.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def root_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7068
            
            return self._parent._cast(_7068.RootAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def shaft_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7069
            
            return self._parent._cast(_7069.ShaftAdvancedTimeSteppingAnalysisForModulation)

        @property
        def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7070
            
            return self._parent._cast(_7070.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7072
            
            return self._parent._cast(_7072.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7073
            
            return self._parent._cast(_7073.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7075
            
            return self._parent._cast(_7075.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7076
            
            return self._parent._cast(_7076.SpringDamperAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spring_damper_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7078
            
            return self._parent._cast(_7078.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7079
            
            return self._parent._cast(_7079.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7081
            
            return self._parent._cast(_7081.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7082
            
            return self._parent._cast(_7082.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7084
            
            return self._parent._cast(_7084.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7085
            
            return self._parent._cast(_7085.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7086
            
            return self._parent._cast(_7086.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7087
            
            return self._parent._cast(_7087.SynchroniserAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_half_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7088
            
            return self._parent._cast(_7088.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7089
            
            return self._parent._cast(_7089.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation)

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7090
            
            return self._parent._cast(_7090.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7091
            
            return self._parent._cast(_7091.TorqueConverterAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_pump_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7093
            
            return self._parent._cast(_7093.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_turbine_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7094
            
            return self._parent._cast(_7094.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation)

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7095
            
            return self._parent._cast(_7095.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation)

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7096
            
            return self._parent._cast(_7096.VirtualComponentAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7097
            
            return self._parent._cast(_7097.WormGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7099
            
            return self._parent._cast(_7099.WormGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7100
            
            return self._parent._cast(_7100.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7102
            
            return self._parent._cast(_7102.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7232
            
            return self._parent._cast(_7232.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def abstract_shaft_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7233
            
            return self._parent._cast(_7233.AbstractShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7234
            
            return self._parent._cast(_7234.AbstractShaftOrHousingAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7239
            
            return self._parent._cast(_7239.AGMAGleasonConicalGearAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7241
            
            return self._parent._cast(_7241.AGMAGleasonConicalGearSetAdvancedSystemDeflection)

        @property
        def assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7242
            
            return self._parent._cast(_7242.AssemblyAdvancedSystemDeflection)

        @property
        def bearing_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7243
            
            return self._parent._cast(_7243.BearingAdvancedSystemDeflection)

        @property
        def belt_drive_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7245
            
            return self._parent._cast(_7245.BeltDriveAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7246
            
            return self._parent._cast(_7246.BevelDifferentialGearAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7248
            
            return self._parent._cast(_7248.BevelDifferentialGearSetAdvancedSystemDeflection)

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7249
            
            return self._parent._cast(_7249.BevelDifferentialPlanetGearAdvancedSystemDeflection)

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7250
            
            return self._parent._cast(_7250.BevelDifferentialSunGearAdvancedSystemDeflection)

        @property
        def bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7251
            
            return self._parent._cast(_7251.BevelGearAdvancedSystemDeflection)

        @property
        def bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7253
            
            return self._parent._cast(_7253.BevelGearSetAdvancedSystemDeflection)

        @property
        def bolt_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7254
            
            return self._parent._cast(_7254.BoltAdvancedSystemDeflection)

        @property
        def bolted_joint_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7255
            
            return self._parent._cast(_7255.BoltedJointAdvancedSystemDeflection)

        @property
        def clutch_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7256
            
            return self._parent._cast(_7256.ClutchAdvancedSystemDeflection)

        @property
        def clutch_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7258
            
            return self._parent._cast(_7258.ClutchHalfAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7260
            
            return self._parent._cast(_7260.ComponentAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7261
            
            return self._parent._cast(_7261.ConceptCouplingAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7263
            
            return self._parent._cast(_7263.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7264
            
            return self._parent._cast(_7264.ConceptGearAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7266
            
            return self._parent._cast(_7266.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7267
            
            return self._parent._cast(_7267.ConicalGearAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7269
            
            return self._parent._cast(_7269.ConicalGearSetAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7271
            
            return self._parent._cast(_7271.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7273
            
            return self._parent._cast(_7273.CouplingAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7275
            
            return self._parent._cast(_7275.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7276
            
            return self._parent._cast(_7276.CVTAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7278
            
            return self._parent._cast(_7278.CVTPulleyAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7279
            
            return self._parent._cast(_7279.CycloidalAssemblyAdvancedSystemDeflection)

        @property
        def cycloidal_disc_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7280
            
            return self._parent._cast(_7280.CycloidalDiscAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7283
            
            return self._parent._cast(_7283.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7285
            
            return self._parent._cast(_7285.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7287
            
            return self._parent._cast(_7287.CylindricalPlanetGearAdvancedSystemDeflection)

        @property
        def datum_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7288
            
            return self._parent._cast(_7288.DatumAdvancedSystemDeflection)

        @property
        def external_cad_model_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7289
            
            return self._parent._cast(_7289.ExternalCADModelAdvancedSystemDeflection)

        @property
        def face_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7290
            
            return self._parent._cast(_7290.FaceGearAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7292
            
            return self._parent._cast(_7292.FaceGearSetAdvancedSystemDeflection)

        @property
        def fe_part_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7293
            
            return self._parent._cast(_7293.FEPartAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7294
            
            return self._parent._cast(_7294.FlexiblePinAssemblyAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7295
            
            return self._parent._cast(_7295.GearAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7297
            
            return self._parent._cast(_7297.GearSetAdvancedSystemDeflection)

        @property
        def guide_dxf_model_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7298
            
            return self._parent._cast(_7298.GuideDxfModelAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7299
            
            return self._parent._cast(_7299.HypoidGearAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7301
            
            return self._parent._cast(_7301.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7303
            
            return self._parent._cast(_7303.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7305
            
            return self._parent._cast(_7305.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7306
            
            return self._parent._cast(_7306.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7308
            
            return self._parent._cast(_7308.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7309
            
            return self._parent._cast(_7309.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7311
            
            return self._parent._cast(_7311.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def mass_disc_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7313
            
            return self._parent._cast(_7313.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7314
            
            return self._parent._cast(_7314.MeasurementComponentAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7315
            
            return self._parent._cast(_7315.MountableComponentAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7316
            
            return self._parent._cast(_7316.OilSealAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7317
            
            return self._parent._cast(_7317.PartAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7318
            
            return self._parent._cast(_7318.PartToPartShearCouplingAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7320
            
            return self._parent._cast(_7320.PartToPartShearCouplingHalfAdvancedSystemDeflection)

        @property
        def planetary_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7322
            
            return self._parent._cast(_7322.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def planet_carrier_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7323
            
            return self._parent._cast(_7323.PlanetCarrierAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7324
            
            return self._parent._cast(_7324.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7325
            
            return self._parent._cast(_7325.PowerLoadAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7326
            
            return self._parent._cast(_7326.PulleyAdvancedSystemDeflection)

        @property
        def ring_pins_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7327
            
            return self._parent._cast(_7327.RingPinsAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7329
            
            return self._parent._cast(_7329.RollingRingAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7330
            
            return self._parent._cast(_7330.RollingRingAssemblyAdvancedSystemDeflection)

        @property
        def root_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7332
            
            return self._parent._cast(_7332.RootAssemblyAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7333
            
            return self._parent._cast(_7333.ShaftAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7334
            
            return self._parent._cast(_7334.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7336
            
            return self._parent._cast(_7336.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7337
            
            return self._parent._cast(_7337.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7339
            
            return self._parent._cast(_7339.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def spring_damper_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7340
            
            return self._parent._cast(_7340.SpringDamperAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7342
            
            return self._parent._cast(_7342.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7343
            
            return self._parent._cast(_7343.StraightBevelDiffGearAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7345
            
            return self._parent._cast(_7345.StraightBevelDiffGearSetAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7346
            
            return self._parent._cast(_7346.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7348
            
            return self._parent._cast(_7348.StraightBevelGearSetAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7349
            
            return self._parent._cast(_7349.StraightBevelPlanetGearAdvancedSystemDeflection)

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7350
            
            return self._parent._cast(_7350.StraightBevelSunGearAdvancedSystemDeflection)

        @property
        def synchroniser_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7351
            
            return self._parent._cast(_7351.SynchroniserAdvancedSystemDeflection)

        @property
        def synchroniser_half_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7352
            
            return self._parent._cast(_7352.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7353
            
            return self._parent._cast(_7353.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7354
            
            return self._parent._cast(_7354.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7355
            
            return self._parent._cast(_7355.TorqueConverterAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7357
            
            return self._parent._cast(_7357.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7358
            
            return self._parent._cast(_7358.TorqueConverterTurbineAdvancedSystemDeflection)

        @property
        def unbalanced_mass_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7360
            
            return self._parent._cast(_7360.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7361
            
            return self._parent._cast(_7361.VirtualComponentAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7362
            
            return self._parent._cast(_7362.WormGearAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7364
            
            return self._parent._cast(_7364.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7365
            
            return self._parent._cast(_7365.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7367
            
            return self._parent._cast(_7367.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis(self) -> 'PartAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PartAnalysis._Cast_PartAnalysis':
        return self._Cast_PartAnalysis(self)
