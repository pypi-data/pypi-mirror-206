"""_3953.py

PartCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3822
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'PartCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundStabilityAnalysis',)


class PartCompoundStabilityAnalysis(_7508.PartCompoundAnalysis):
    """PartCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_STABILITY_ANALYSIS

    class _Cast_PartCompoundStabilityAnalysis:
        """Special nested class for casting PartCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'PartCompoundStabilityAnalysis'):
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
        def part_compound_stability_analysis(self) -> 'PartCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3822.PartStabilityAnalysis]':
        """List[PartStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3822.PartStabilityAnalysis]':
        """List[PartStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis':
        return self._Cast_PartCompoundStabilityAnalysis(self)
