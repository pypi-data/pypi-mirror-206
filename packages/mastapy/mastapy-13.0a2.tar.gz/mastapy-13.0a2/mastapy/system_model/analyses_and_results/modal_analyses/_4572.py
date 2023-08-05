"""_4572.py

ComponentModalAnalysis
"""
from mastapy.system_model.part_model import _2424
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2694
from mastapy.system_model.analyses_and_results.modal_analyses import _4635
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ComponentModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentModalAnalysis',)


class ComponentModalAnalysis(_4635.PartModalAnalysis):
    """ComponentModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_MODAL_ANALYSIS

    class _Cast_ComponentModalAnalysis:
        """Special nested class for casting ComponentModalAnalysis to subclasses."""

        def __init__(self, parent: 'ComponentModalAnalysis'):
            self._parent = parent

        @property
        def part_modal_analysis(self):
            return self._parent._cast(_4635.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
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
        def bearing_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4555
            
            return self._parent._cast(_4555.BearingModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4559
            
            return self._parent._cast(_4559.BevelDifferentialGearModalAnalysis)

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
        def bolt_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4567
            
            return self._parent._cast(_4567.BoltModalAnalysis)

        @property
        def clutch_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4569
            
            return self._parent._cast(_4569.ClutchHalfModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574
            
            return self._parent._cast(_4574.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4577
            
            return self._parent._cast(_4577.ConceptGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580
            
            return self._parent._cast(_4580.ConicalGearModalAnalysis)

        @property
        def connector_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4583
            
            return self._parent._cast(_4583.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586
            
            return self._parent._cast(_4586.CouplingHalfModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590
            
            return self._parent._cast(_4590.CVTPulleyModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593
            
            return self._parent._cast(_4593.CycloidalDiscModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596
            
            return self._parent._cast(_4596.CylindricalGearModalAnalysis)

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
        def fe_part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606
            
            return self._parent._cast(_4606.FEPartModalAnalysis)

        @property
        def gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610
            
            return self._parent._cast(_4610.GearModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612
            
            return self._parent._cast(_4612.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614
            
            return self._parent._cast(_4614.HypoidGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618
            
            return self._parent._cast(_4618.KlingelnbergCycloPalloidConicalGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4621
            
            return self._parent._cast(_4621.KlingelnbergCycloPalloidHypoidGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4624
            
            return self._parent._cast(_4624.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis)

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
        def rolling_ring_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649
            
            return self._parent._cast(_4649.RollingRingModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651
            
            return self._parent._cast(_4651.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4652
            
            return self._parent._cast(_4652.ShaftModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657
            
            return self._parent._cast(_4657.SpiralBevelGearModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660
            
            return self._parent._cast(_4660.SpringDamperHalfModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663
            
            return self._parent._cast(_4663.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666
            
            return self._parent._cast(_4666.StraightBevelGearModalAnalysis)

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
        def synchroniser_part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672
            
            return self._parent._cast(_4672.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673
            
            return self._parent._cast(_4673.SynchroniserSleeveModalAnalysis)

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
        def zerol_bevel_gear_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687
            
            return self._parent._cast(_4687.ZerolBevelGearModalAnalysis)

        @property
        def component_modal_analysis(self) -> 'ComponentModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2424.Component':
        """Component: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2694.ComponentSystemDeflection':
        """ComponentSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ComponentModalAnalysis._Cast_ComponentModalAnalysis':
        return self._Cast_ComponentModalAnalysis(self)
