"""_6452.py

PartCompoundDynamicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'PartCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundDynamicAnalysis',)


class PartCompoundDynamicAnalysis(_7508.PartCompoundAnalysis):
    """PartCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_PartCompoundDynamicAnalysis:
        """Special nested class for casting PartCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'PartCompoundDynamicAnalysis'):
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
        def part_compound_dynamic_analysis(self) -> 'PartCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6323.PartDynamicAnalysis]':
        """List[PartDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6323.PartDynamicAnalysis]':
        """List[PartDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis':
        return self._Cast_PartCompoundDynamicAnalysis(self)
