"""_5385.py

ConnectionMultibodyDynamicsAnalysis
"""
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2253
from mastapy.system_model.analyses_and_results.mbd_analyses import _2618
from mastapy.math_utility.convergence import _1564
from mastapy.system_model.analyses_and_results.analysis_cases import _7504
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'ConnectionMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionMultibodyDynamicsAnalysis',)


class ConnectionMultibodyDynamicsAnalysis(_7504.ConnectionTimeSeriesLoadAnalysisCase):
    """ConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_ConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting ConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectionMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def connection_time_series_load_analysis_case(self):
            return self._parent._cast(_7504.ConnectionTimeSeriesLoadAnalysisCase)

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
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5350
            
            return self._parent._cast(_5350.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5351
            
            return self._parent._cast(_5351.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def belt_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5358
            
            return self._parent._cast(_5358.BeltConnectionMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5360
            
            return self._parent._cast(_5360.BevelDifferentialGearMeshMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5365
            
            return self._parent._cast(_5365.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5370
            
            return self._parent._cast(_5370.ClutchConnectionMultibodyDynamicsAnalysis)

        @property
        def coaxial_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5374
            
            return self._parent._cast(_5374.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5376
            
            return self._parent._cast(_5376.ConceptCouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5379
            
            return self._parent._cast(_5379.ConceptGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382
            
            return self._parent._cast(_5382.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387
            
            return self._parent._cast(_5387.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390
            
            return self._parent._cast(_5390.CVTBeltConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5394
            
            return self._parent._cast(_5394.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396
            
            return self._parent._cast(_5396.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397
            
            return self._parent._cast(_5397.CylindricalGearMeshMultibodyDynamicsAnalysis)

        @property
        def face_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403
            
            return self._parent._cast(_5403.FaceGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408
            
            return self._parent._cast(_5408.GearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413
            
            return self._parent._cast(_5413.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420
            
            return self._parent._cast(_5420.InterMountableComponentConnectionMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421
            
            return self._parent._cast(_5421.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424
            
            return self._parent._cast(_5424.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5427
            
            return self._parent._cast(_5427.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438
            
            return self._parent._cast(_5438.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def planetary_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441
            
            return self._parent._cast(_5441.PlanetaryConnectionMultibodyDynamicsAnalysis)

        @property
        def ring_pins_to_disc_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448
            
            return self._parent._cast(_5448.RingPinsToDiscConnectionMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5450
            
            return self._parent._cast(_5450.RollingRingConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457
            
            return self._parent._cast(_5457.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460
            
            return self._parent._cast(_5460.SpiralBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def spring_damper_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463
            
            return self._parent._cast(_5463.SpringDamperConnectionMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466
            
            return self._parent._cast(_5466.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469
            
            return self._parent._cast(_5469.StraightBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def torque_converter_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478
            
            return self._parent._cast(_5478.TorqueConverterConnectionMultibodyDynamicsAnalysis)

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487
            
            return self._parent._cast(_5487.WormGearMeshMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5490
            
            return self._parent._cast(_5490.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(self) -> 'ConnectionMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def total_degrees_of_freedom(self) -> 'int':
        """int: 'TotalDegreesOfFreedom' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def component_design(self) -> '_2253.Connection':
        """Connection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2253.Connection':
        """Connection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def multibody_dynamics_analysis(self) -> '_2618.MultibodyDynamicsAnalysis':
        """MultibodyDynamicsAnalysis: 'MultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MultibodyDynamicsAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def data_logger(self) -> '_1564.DataLogger':
        """DataLogger: 'DataLogger' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectionMultibodyDynamicsAnalysis._Cast_ConnectionMultibodyDynamicsAnalysis':
        return self._Cast_ConnectionMultibodyDynamicsAnalysis(self)
