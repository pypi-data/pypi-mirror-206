"""_3805.py

HypoidGearMeshStabilityAnalysis
"""
from mastapy.system_model.connections_and_sockets.gears import _2296
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6870
from mastapy.system_model.analyses_and_results.stability_analyses import _3746
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'HypoidGearMeshStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMeshStabilityAnalysis',)


class HypoidGearMeshStabilityAnalysis(_3746.AGMAGleasonConicalGearMeshStabilityAnalysis):
    """HypoidGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_STABILITY_ANALYSIS

    class _Cast_HypoidGearMeshStabilityAnalysis:
        """Special nested class for casting HypoidGearMeshStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'HypoidGearMeshStabilityAnalysis'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(self):
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
        def hypoid_gear_mesh_stability_analysis(self) -> 'HypoidGearMeshStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearMeshStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2296.HypoidGearMesh':
        """HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6870.HypoidGearMeshLoadCase':
        """HypoidGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HypoidGearMeshStabilityAnalysis._Cast_HypoidGearMeshStabilityAnalysis':
        return self._Cast_HypoidGearMeshStabilityAnalysis(self)
