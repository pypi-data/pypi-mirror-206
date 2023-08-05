"""_6533.py

ComponentCriticalSpeedAnalysis
"""
from mastapy.system_model.part_model import _2424
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6589
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'ComponentCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentCriticalSpeedAnalysis',)


class ComponentCriticalSpeedAnalysis(_6589.PartCriticalSpeedAnalysis):
    """ComponentCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_CRITICAL_SPEED_ANALYSIS

    class _Cast_ComponentCriticalSpeedAnalysis:
        """Special nested class for casting ComponentCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'ComponentCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def part_critical_speed_analysis(self):
            return self._parent._cast(_6589.PartCriticalSpeedAnalysis)

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
        def bearing_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6516
            
            return self._parent._cast(_6516.BearingCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6519
            
            return self._parent._cast(_6519.BevelDifferentialGearCriticalSpeedAnalysis)

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
        def bolt_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6527
            
            return self._parent._cast(_6527.BoltCriticalSpeedAnalysis)

        @property
        def clutch_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6531
            
            return self._parent._cast(_6531.ClutchHalfCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6536
            
            return self._parent._cast(_6536.ConceptCouplingHalfCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6537
            
            return self._parent._cast(_6537.ConceptGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6540
            
            return self._parent._cast(_6540.ConicalGearCriticalSpeedAnalysis)

        @property
        def connector_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6544
            
            return self._parent._cast(_6544.ConnectorCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6547
            
            return self._parent._cast(_6547.CouplingHalfCriticalSpeedAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6552
            
            return self._parent._cast(_6552.CVTPulleyCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6555
            
            return self._parent._cast(_6555.CycloidalDiscCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6557
            
            return self._parent._cast(_6557.CylindricalGearCriticalSpeedAnalysis)

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
        def fe_part_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6566
            
            return self._parent._cast(_6566.FEPartCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6568
            
            return self._parent._cast(_6568.GearCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6571
            
            return self._parent._cast(_6571.GuideDxfModelCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6572
            
            return self._parent._cast(_6572.HypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6576
            
            return self._parent._cast(_6576.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6579
            
            return self._parent._cast(_6579.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6582
            
            return self._parent._cast(_6582.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis)

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
        def part_to_part_shear_coupling_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6592
            
            return self._parent._cast(_6592.PartToPartShearCouplingHalfCriticalSpeedAnalysis)

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
        def rolling_ring_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6603
            
            return self._parent._cast(_6603.RollingRingCriticalSpeedAnalysis)

        @property
        def shaft_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6605
            
            return self._parent._cast(_6605.ShaftCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6606
            
            return self._parent._cast(_6606.ShaftHubConnectionCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6609
            
            return self._parent._cast(_6609.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def spring_damper_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6614
            
            return self._parent._cast(_6614.SpringDamperHalfCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6615
            
            return self._parent._cast(_6615.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6618
            
            return self._parent._cast(_6618.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6621
            
            return self._parent._cast(_6621.StraightBevelPlanetGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6622
            
            return self._parent._cast(_6622.StraightBevelSunGearCriticalSpeedAnalysis)

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
        def zerol_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6636
            
            return self._parent._cast(_6636.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(self) -> 'ComponentCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentCriticalSpeedAnalysis.TYPE'):
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
    def cast_to(self) -> 'ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis':
        return self._Cast_ComponentCriticalSpeedAnalysis(self)
