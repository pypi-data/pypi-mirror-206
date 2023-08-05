"""_3777.py

ConnectionStabilityAnalysis
"""
from mastapy.system_model.connections_and_sockets import _2253
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _2621
from mastapy.system_model.analyses_and_results.analysis_cases import _7503
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ConnectionStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionStabilityAnalysis',)


class ConnectionStabilityAnalysis(_7503.ConnectionStaticLoadAnalysisCase):
    """ConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_STABILITY_ANALYSIS

    class _Cast_ConnectionStabilityAnalysis:
        """Special nested class for casting ConnectionStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectionStabilityAnalysis'):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(self):
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
        def abstract_shaft_to_mountable_component_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3745
            
            return self._parent._cast(_3745.AbstractShaftToMountableComponentConnectionStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3746
            
            return self._parent._cast(_3746.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def belt_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3751
            
            return self._parent._cast(_3751.BeltConnectionStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3753
            
            return self._parent._cast(_3753.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3758
            
            return self._parent._cast(_3758.BevelGearMeshStabilityAnalysis)

        @property
        def clutch_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3763
            
            return self._parent._cast(_3763.ClutchConnectionStabilityAnalysis)

        @property
        def coaxial_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3766
            
            return self._parent._cast(_3766.CoaxialConnectionStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3768
            
            return self._parent._cast(_3768.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def concept_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3771
            
            return self._parent._cast(_3771.ConceptGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3774
            
            return self._parent._cast(_3774.ConicalGearMeshStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3779
            
            return self._parent._cast(_3779.CouplingConnectionStabilityAnalysis)

        @property
        def cvt_belt_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3783
            
            return self._parent._cast(_3783.CVTBeltConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3787
            
            return self._parent._cast(_3787.CycloidalDiscCentralBearingConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3788
            
            return self._parent._cast(_3788.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3790
            
            return self._parent._cast(_3790.CylindricalGearMeshStabilityAnalysis)

        @property
        def face_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3796
            
            return self._parent._cast(_3796.FaceGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3801
            
            return self._parent._cast(_3801.GearMeshStabilityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3805
            
            return self._parent._cast(_3805.HypoidGearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3808
            
            return self._parent._cast(_3808.InterMountableComponentConnectionStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3809
            
            return self._parent._cast(_3809.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3812
            
            return self._parent._cast(_3812.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3815
            
            return self._parent._cast(_3815.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3823
            
            return self._parent._cast(_3823.PartToPartShearCouplingConnectionStabilityAnalysis)

        @property
        def planetary_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3826
            
            return self._parent._cast(_3826.PlanetaryConnectionStabilityAnalysis)

        @property
        def ring_pins_to_disc_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3833
            
            return self._parent._cast(_3833.RingPinsToDiscConnectionStabilityAnalysis)

        @property
        def rolling_ring_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3835
            
            return self._parent._cast(_3835.RollingRingConnectionStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3840
            
            return self._parent._cast(_3840.ShaftToMountableComponentConnectionStabilityAnalysis)

        @property
        def spiral_bevel_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3842
            
            return self._parent._cast(_3842.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def spring_damper_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3845
            
            return self._parent._cast(_3845.SpringDamperConnectionStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3850
            
            return self._parent._cast(_3850.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3853
            
            return self._parent._cast(_3853.StraightBevelGearMeshStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3862
            
            return self._parent._cast(_3862.TorqueConverterConnectionStabilityAnalysis)

        @property
        def worm_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3868
            
            return self._parent._cast(_3868.WormGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3871
            
            return self._parent._cast(_3871.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def connection_stability_analysis(self) -> 'ConnectionStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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

    @property
    def cast_to(self) -> 'ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis':
        return self._Cast_ConnectionStabilityAnalysis(self)
