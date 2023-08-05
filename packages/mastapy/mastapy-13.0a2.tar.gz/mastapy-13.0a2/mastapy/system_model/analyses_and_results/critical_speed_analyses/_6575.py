"""_6575.py

InterMountableComponentConnectionCriticalSpeedAnalysis
"""
from mastapy.system_model.connections_and_sockets import _2262
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'InterMountableComponentConnectionCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionCriticalSpeedAnalysis',)


class InterMountableComponentConnectionCriticalSpeedAnalysis(_6543.ConnectionCriticalSpeedAnalysis):
    """InterMountableComponentConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_CRITICAL_SPEED_ANALYSIS

    class _Cast_InterMountableComponentConnectionCriticalSpeedAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def connection_critical_speed_analysis(self):
            return self._parent._cast(_6543.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7503
            
            return self._parent._cast(_7503.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7500
            
            return self._parent._cast(_7500.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2628
            
            return self._parent._cast(_2628.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6513
            
            return self._parent._cast(_6513.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis)

        @property
        def belt_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6517
            
            return self._parent._cast(_6517.BeltConnectionCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6520
            
            return self._parent._cast(_6520.BevelDifferentialGearMeshCriticalSpeedAnalysis)

        @property
        def bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6525
            
            return self._parent._cast(_6525.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def clutch_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6529
            
            return self._parent._cast(_6529.ClutchConnectionCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6534
            
            return self._parent._cast(_6534.ConceptCouplingConnectionCriticalSpeedAnalysis)

        @property
        def concept_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6538
            
            return self._parent._cast(_6538.ConceptGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6541
            
            return self._parent._cast(_6541.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def coupling_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6545
            
            return self._parent._cast(_6545.CouplingConnectionCriticalSpeedAnalysis)

        @property
        def cvt_belt_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6550
            
            return self._parent._cast(_6550.CVTBeltConnectionCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6558
            
            return self._parent._cast(_6558.CylindricalGearMeshCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6564
            
            return self._parent._cast(_6564.FaceGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6569
            
            return self._parent._cast(_6569.GearMeshCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6573
            
            return self._parent._cast(_6573.HypoidGearMeshCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6577
            
            return self._parent._cast(_6577.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6580
            
            return self._parent._cast(_6580.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6583
            
            return self._parent._cast(_6583.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6590
            
            return self._parent._cast(_6590.PartToPartShearCouplingConnectionCriticalSpeedAnalysis)

        @property
        def ring_pins_to_disc_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6600
            
            return self._parent._cast(_6600.RingPinsToDiscConnectionCriticalSpeedAnalysis)

        @property
        def rolling_ring_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6602
            
            return self._parent._cast(_6602.RollingRingConnectionCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6610
            
            return self._parent._cast(_6610.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6612
            
            return self._parent._cast(_6612.SpringDamperConnectionCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6616
            
            return self._parent._cast(_6616.StraightBevelDiffGearMeshCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6619
            
            return self._parent._cast(_6619.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6627
            
            return self._parent._cast(_6627.TorqueConverterConnectionCriticalSpeedAnalysis)

        @property
        def worm_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6634
            
            return self._parent._cast(_6634.WormGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6637
            
            return self._parent._cast(_6637.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(self) -> 'InterMountableComponentConnectionCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2262.InterMountableComponentConnection':
        """InterMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'InterMountableComponentConnectionCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCriticalSpeedAnalysis':
        return self._Cast_InterMountableComponentConnectionCriticalSpeedAnalysis(self)
