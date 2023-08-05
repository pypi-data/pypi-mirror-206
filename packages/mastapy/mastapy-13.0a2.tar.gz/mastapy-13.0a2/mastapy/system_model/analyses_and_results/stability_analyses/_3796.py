"""_3796.py

FaceGearMeshStabilityAnalysis
"""
from mastapy.system_model.connections_and_sockets.gears import _2292
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6849
from mastapy.system_model.analyses_and_results.stability_analyses import _3801
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'FaceGearMeshStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshStabilityAnalysis',)


class FaceGearMeshStabilityAnalysis(_3801.GearMeshStabilityAnalysis):
    """FaceGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_STABILITY_ANALYSIS

    class _Cast_FaceGearMeshStabilityAnalysis:
        """Special nested class for casting FaceGearMeshStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'FaceGearMeshStabilityAnalysis'):
            self._parent = parent

        @property
        def gear_mesh_stability_analysis(self):
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
        def face_gear_mesh_stability_analysis(self) -> 'FaceGearMeshStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearMeshStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2292.FaceGearMesh':
        """FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6849.FaceGearMeshLoadCase':
        """FaceGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'FaceGearMeshStabilityAnalysis._Cast_FaceGearMeshStabilityAnalysis':
        return self._Cast_FaceGearMeshStabilityAnalysis(self)
