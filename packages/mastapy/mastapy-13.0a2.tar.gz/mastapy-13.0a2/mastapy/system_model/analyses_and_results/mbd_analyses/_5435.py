"""_5435.py

MountableComponentMultibodyDynamicsAnalysis
"""
from mastapy.system_model.part_model import _2444
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5375
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'MountableComponentMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentMultibodyDynamicsAnalysis',)


class MountableComponentMultibodyDynamicsAnalysis(_5375.ComponentMultibodyDynamicsAnalysis):
    """MountableComponentMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_MountableComponentMultibodyDynamicsAnalysis:
        """Special nested class for casting MountableComponentMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'MountableComponentMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def component_multibody_dynamics_analysis(self):
            return self._parent._cast(_5375.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437
            
            return self._parent._cast(_5437.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartTimeSeriesLoadAnalysisCase)

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
        def agma_gleason_conical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5352
            
            return self._parent._cast(_5352.AGMAGleasonConicalGearMultibodyDynamicsAnalysis)

        @property
        def bearing_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5356
            
            return self._parent._cast(_5356.BearingMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5361
            
            return self._parent._cast(_5361.BevelDifferentialGearMultibodyDynamicsAnalysis)

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
        def clutch_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5371
            
            return self._parent._cast(_5371.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5377
            
            return self._parent._cast(_5377.ConceptCouplingHalfMultibodyDynamicsAnalysis)

        @property
        def concept_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5380
            
            return self._parent._cast(_5380.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5383
            
            return self._parent._cast(_5383.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5386
            
            return self._parent._cast(_5386.ConnectorMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5388
            
            return self._parent._cast(_5388.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392
            
            return self._parent._cast(_5392.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398
            
            return self._parent._cast(_5398.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400
            
            return self._parent._cast(_5400.CylindricalPlanetGearMultibodyDynamicsAnalysis)

        @property
        def face_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404
            
            return self._parent._cast(_5404.FaceGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410
            
            return self._parent._cast(_5410.GearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414
            
            return self._parent._cast(_5414.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422
            
            return self._parent._cast(_5422.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425
            
            return self._parent._cast(_5425.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428
            
            return self._parent._cast(_5428.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def mass_disc_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430
            
            return self._parent._cast(_5430.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5434
            
            return self._parent._cast(_5434.MeasurementComponentMultibodyDynamicsAnalysis)

        @property
        def oil_seal_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436
            
            return self._parent._cast(_5436.OilSealMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439
            
            return self._parent._cast(_5439.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis)

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
        def rolling_ring_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451
            
            return self._parent._cast(_5451.RollingRingMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455
            
            return self._parent._cast(_5455.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461
            
            return self._parent._cast(_5461.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464
            
            return self._parent._cast(_5464.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467
            
            return self._parent._cast(_5467.StraightBevelDiffGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470
            
            return self._parent._cast(_5470.StraightBevelGearMultibodyDynamicsAnalysis)

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
        def synchroniser_part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476
            
            return self._parent._cast(_5476.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477
            
            return self._parent._cast(_5477.SynchroniserSleeveMultibodyDynamicsAnalysis)

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
        def zerol_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491
            
            return self._parent._cast(_5491.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(self) -> 'MountableComponentMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2444.MountableComponent':
        """MountableComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis':
        return self._Cast_MountableComponentMultibodyDynamicsAnalysis(self)
