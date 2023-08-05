"""_3822.py

PartStabilityAnalysis
"""
from mastapy.system_model.part_model import _2448
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _2621
from mastapy.system_model.drawing import _2238
from mastapy.system_model.analyses_and_results.analysis_cases import _7510
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'PartStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartStabilityAnalysis',)


class PartStabilityAnalysis(_7510.PartStaticLoadAnalysisCase):
    """PartStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_STABILITY_ANALYSIS

    class _Cast_PartStabilityAnalysis:
        """Special nested class for casting PartStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'PartStabilityAnalysis'):
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
        def part_stability_analysis(self) -> 'PartStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2448.Part':
        """Part: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stability_analysis(self) -> '_2621.StabilityAnalysis':
        """StabilityAnalysis: 'StabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StabilityAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def create_viewable(self) -> '_2238.StabilityAnalysisViewable':
        """ 'CreateViewable' is the original name of this method.

        Returns:
            mastapy.system_model.drawing.StabilityAnalysisViewable
        """

        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'PartStabilityAnalysis._Cast_PartStabilityAnalysis':
        return self._Cast_PartStabilityAnalysis(self)
