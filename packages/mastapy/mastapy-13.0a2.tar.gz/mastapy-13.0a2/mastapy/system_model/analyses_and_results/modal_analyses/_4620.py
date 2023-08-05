"""_4620.py

KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
"""
from mastapy.system_model.connections_and_sockets.gears import _2300
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6880
from mastapy.system_model.analyses_and_results.system_deflections import _2750
from mastapy.system_model.analyses_and_results.modal_analyses import _4617
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis',)


class KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis(_4617.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis):
    """KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_MODAL_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(self):
            return self._parent._cast(_4617.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4579
            
            return self._parent._cast(_4579.ConicalGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609
            
            return self._parent._cast(_4609.GearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616
            
            return self._parent._cast(_4616.InterMountableComponentConnectionModalAnalysis)

        @property
        def connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582
            
            return self._parent._cast(_4582.ConnectionModalAnalysis)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(self) -> 'KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2300.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6880.KlingelnbergCycloPalloidHypoidGearMeshLoadCase':
        """KlingelnbergCycloPalloidHypoidGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2750.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection':
        """KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis(self)
