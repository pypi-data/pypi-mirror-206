"""_4635.py

PartModalAnalysis
"""
from typing import List

from mastapy.system_model.part_model import _2448
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _2614
from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4699, _4697, _4700
from mastapy.system_model.analyses_and_results.system_deflections import _2764
from mastapy.system_model.drawing import _2232
from mastapy.system_model.analyses_and_results.analysis_cases import _7510
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'PartModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartModalAnalysis',)


class PartModalAnalysis(_7510.PartStaticLoadAnalysisCase):
    """PartModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_MODAL_ANALYSIS

    class _Cast_PartModalAnalysis:
        """Special nested class for casting PartModalAnalysis to subclasses."""

        def __init__(self, parent: 'PartModalAnalysis'):
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
        def part_modal_analysis(self) -> 'PartModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartModalAnalysis.TYPE'):
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
    def modal_analysis(self) -> '_2614.ModalAnalysis':
        """ModalAnalysis: 'ModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excited_modes_summary(self) -> 'List[_4699.SingleExcitationResultsModalAnalysis]':
        """List[SingleExcitationResultsModalAnalysis]: 'ExcitedModesSummary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcitedModesSummary

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_mesh_excitation_details(self) -> 'List[_4697.RigidlyConnectedDesignEntityGroupModalAnalysis]':
        """List[RigidlyConnectedDesignEntityGroupModalAnalysis]: 'GearMeshExcitationDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshExcitationDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def results_for_modes(self) -> 'List[_4700.SingleModeResults]':
        """List[SingleModeResults]: 'ResultsForModes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsForModes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_excitation_details(self) -> 'List[_4697.RigidlyConnectedDesignEntityGroupModalAnalysis]':
        """List[RigidlyConnectedDesignEntityGroupModalAnalysis]: 'ShaftExcitationDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftExcitationDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def system_deflection_results(self) -> '_2764.PartSystemDeflection':
        """PartSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def create_viewable(self) -> '_2232.ModalAnalysisViewable':
        """ 'CreateViewable' is the original name of this method.

        Returns:
            mastapy.system_model.drawing.ModalAnalysisViewable
        """

        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'PartModalAnalysis._Cast_PartModalAnalysis':
        return self._Cast_PartModalAnalysis(self)
