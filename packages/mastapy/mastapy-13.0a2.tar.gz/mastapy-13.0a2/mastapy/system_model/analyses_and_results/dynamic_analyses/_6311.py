"""_6311.py

KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
"""
from mastapy.system_model.connections_and_sockets.gears import _2299
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6276
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis',)


class KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis(_6276.ConicalGearMeshDynamicAnalysis):
    """KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_DYNAMIC_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis'):
            self._parent = parent

        @property
        def conical_gear_mesh_dynamic_analysis(self):
            return self._parent._cast(_6276.ConicalGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303
            
            return self._parent._cast(_6303.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309
            
            return self._parent._cast(_6309.InterMountableComponentConnectionDynamicAnalysis)

        @property
        def connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6278
            
            return self._parent._cast(_6278.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7502
            
            return self._parent._cast(_7502.ConnectionFEAnalysis)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314
            
            return self._parent._cast(_6314.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317
            
            return self._parent._cast(_6317.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(self) -> 'KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2299.KlingelnbergCycloPalloidConicalGearMesh':
        """KlingelnbergCycloPalloidConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis':
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis(self)
