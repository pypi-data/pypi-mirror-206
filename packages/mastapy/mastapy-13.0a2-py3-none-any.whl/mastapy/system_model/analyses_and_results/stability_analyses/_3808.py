"""_3808.py

InterMountableComponentConnectionStabilityAnalysis
"""
from mastapy.system_model.connections_and_sockets import _2262
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3777
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'InterMountableComponentConnectionStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionStabilityAnalysis',)


class InterMountableComponentConnectionStabilityAnalysis(_3777.ConnectionStabilityAnalysis):
    """InterMountableComponentConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_STABILITY_ANALYSIS

    class _Cast_InterMountableComponentConnectionStabilityAnalysis:
        """Special nested class for casting InterMountableComponentConnectionStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionStabilityAnalysis'):
            self._parent = parent

        @property
        def connection_stability_analysis(self):
            return self._parent._cast(_3777.ConnectionStabilityAnalysis)

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
        def ring_pins_to_disc_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3833
            
            return self._parent._cast(_3833.RingPinsToDiscConnectionStabilityAnalysis)

        @property
        def rolling_ring_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3835
            
            return self._parent._cast(_3835.RollingRingConnectionStabilityAnalysis)

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
        def inter_mountable_component_connection_stability_analysis(self) -> 'InterMountableComponentConnectionStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionStabilityAnalysis.TYPE'):
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
    def cast_to(self) -> 'InterMountableComponentConnectionStabilityAnalysis._Cast_InterMountableComponentConnectionStabilityAnalysis':
        return self._Cast_InterMountableComponentConnectionStabilityAnalysis(self)
