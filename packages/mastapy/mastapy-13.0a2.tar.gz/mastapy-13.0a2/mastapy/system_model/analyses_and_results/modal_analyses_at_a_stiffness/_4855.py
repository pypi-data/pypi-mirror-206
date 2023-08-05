"""_4855.py

ComponentModalAnalysisAtAStiffness
"""
from mastapy.system_model.part_model import _2424
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4910
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'ComponentModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentModalAnalysisAtAStiffness',)


class ComponentModalAnalysisAtAStiffness(_4910.PartModalAnalysisAtAStiffness):
    """ComponentModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COMPONENT_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_ComponentModalAnalysisAtAStiffness:
        """Special nested class for casting ComponentModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'ComponentModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def part_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4910.PartModalAnalysisAtAStiffness)

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
        def bearing_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4838
            
            return self._parent._cast(_4838.BearingModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4842
            
            return self._parent._cast(_4842.BevelDifferentialGearModalAnalysisAtAStiffness)

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
        def bolt_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4850
            
            return self._parent._cast(_4850.BoltModalAnalysisAtAStiffness)

        @property
        def clutch_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4852
            
            return self._parent._cast(_4852.ClutchHalfModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4857
            
            return self._parent._cast(_4857.ConceptCouplingHalfModalAnalysisAtAStiffness)

        @property
        def concept_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4860
            
            return self._parent._cast(_4860.ConceptGearModalAnalysisAtAStiffness)

        @property
        def conical_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4863
            
            return self._parent._cast(_4863.ConicalGearModalAnalysisAtAStiffness)

        @property
        def connector_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4866
            
            return self._parent._cast(_4866.ConnectorModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4868
            
            return self._parent._cast(_4868.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4872
            
            return self._parent._cast(_4872.CVTPulleyModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4875
            
            return self._parent._cast(_4875.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4878
            
            return self._parent._cast(_4878.CylindricalGearModalAnalysisAtAStiffness)

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
        def fe_part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4887
            
            return self._parent._cast(_4887.FEPartModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4890
            
            return self._parent._cast(_4890.GearModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4892
            
            return self._parent._cast(_4892.GuideDxfModelModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4894
            
            return self._parent._cast(_4894.HypoidGearModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4898
            
            return self._parent._cast(_4898.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4901
            
            return self._parent._cast(_4901.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4904
            
            return self._parent._cast(_4904.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness)

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
        def part_to_part_shear_coupling_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4912
            
            return self._parent._cast(_4912.PartToPartShearCouplingHalfModalAnalysisAtAStiffness)

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
        def rolling_ring_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4924
            
            return self._parent._cast(_4924.RollingRingModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4926
            
            return self._parent._cast(_4926.ShaftHubConnectionModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4927
            
            return self._parent._cast(_4927.ShaftModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4931
            
            return self._parent._cast(_4931.SpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def spring_damper_half_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4934
            
            return self._parent._cast(_4934.SpringDamperHalfModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4937
            
            return self._parent._cast(_4937.StraightBevelDiffGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4940
            
            return self._parent._cast(_4940.StraightBevelGearModalAnalysisAtAStiffness)

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
        def synchroniser_part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4946
            
            return self._parent._cast(_4946.SynchroniserPartModalAnalysisAtAStiffness)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4947
            
            return self._parent._cast(_4947.SynchroniserSleeveModalAnalysisAtAStiffness)

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
        def zerol_bevel_gear_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4958
            
            return self._parent._cast(_4958.ZerolBevelGearModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(self) -> 'ComponentModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentModalAnalysisAtAStiffness.TYPE'):
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
    def cast_to(self) -> 'ComponentModalAnalysisAtAStiffness._Cast_ComponentModalAnalysisAtAStiffness':
        return self._Cast_ComponentModalAnalysisAtAStiffness(self)
