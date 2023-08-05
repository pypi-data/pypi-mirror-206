"""_3871.py

ZerolBevelGearMeshStabilityAnalysis
"""
from mastapy.system_model.connections_and_sockets.gears import _2312
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6950
from mastapy.system_model.analyses_and_results.stability_analyses import _3758
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ZerolBevelGearMeshStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMeshStabilityAnalysis',)


class ZerolBevelGearMeshStabilityAnalysis(_3758.BevelGearMeshStabilityAnalysis):
    """ZerolBevelGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_STABILITY_ANALYSIS

    class _Cast_ZerolBevelGearMeshStabilityAnalysis:
        """Special nested class for casting ZerolBevelGearMeshStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearMeshStabilityAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_mesh_stability_analysis(self):
            return self._parent._cast(_3758.BevelGearMeshStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3746
            
            return self._parent._cast(_3746.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3774
            
            return self._parent._cast(_3774.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3801
            
            return self._parent._cast(_3801.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3808
            
            return self._parent._cast(_3808.InterMountableComponentConnectionStabilityAnalysis)

        @property
        def connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3777
            
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
        def zerol_bevel_gear_mesh_stability_analysis(self) -> 'ZerolBevelGearMeshStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMeshStabilityAnalysis.TYPE'):
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
    def cast_to(self) -> 'ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis':
        return self._Cast_ZerolBevelGearMeshStabilityAnalysis(self)
