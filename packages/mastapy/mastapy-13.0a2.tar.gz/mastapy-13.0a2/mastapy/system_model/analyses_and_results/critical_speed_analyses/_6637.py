"""_6637.py

ZerolBevelGearMeshCriticalSpeedAnalysis
"""
from mastapy.system_model.connections_and_sockets.gears import _2312
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6950
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6525
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'ZerolBevelGearMeshCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMeshCriticalSpeedAnalysis',)


class ZerolBevelGearMeshCriticalSpeedAnalysis(_6525.BevelGearMeshCriticalSpeedAnalysis):
    """ZerolBevelGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS

    class _Cast_ZerolBevelGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting ZerolBevelGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearMeshCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_mesh_critical_speed_analysis(self):
            return self._parent._cast(_6525.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6513
            
            return self._parent._cast(_6513.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6541
            
            return self._parent._cast(_6541.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6569
            
            return self._parent._cast(_6569.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6575
            
            return self._parent._cast(_6575.InterMountableComponentConnectionCriticalSpeedAnalysis)

        @property
        def connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6543
            
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
        def zerol_bevel_gear_mesh_critical_speed_analysis(self) -> 'ZerolBevelGearMeshCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMeshCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2312.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6950.ZerolBevelGearMeshLoadCase':
        """ZerolBevelGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ZerolBevelGearMeshCriticalSpeedAnalysis._Cast_ZerolBevelGearMeshCriticalSpeedAnalysis':
        return self._Cast_ZerolBevelGearMeshCriticalSpeedAnalysis(self)
