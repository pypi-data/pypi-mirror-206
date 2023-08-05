"""_4617.py

KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
"""
from mastapy.system_model.connections_and_sockets.gears import _2299
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2747
from mastapy.system_model.analyses_and_results.modal_analyses import _4579
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'KlingelnbergCycloPalloidConicalGearMeshModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearMeshModalAnalysis',)


class KlingelnbergCycloPalloidConicalGearMeshModalAnalysis(_4579.ConicalGearMeshModalAnalysis):
    """KlingelnbergCycloPalloidConicalGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_MODAL_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshModalAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearMeshModalAnalysis'):
            self._parent = parent

        @property
        def conical_gear_mesh_modal_analysis(self):
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
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620
            
            return self._parent._cast(_4620.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623
            
            return self._parent._cast(_4623.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(self) -> 'KlingelnbergCycloPalloidConicalGearMeshModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearMeshModalAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2747.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
        """KlingelnbergCycloPalloidConicalGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis':
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysis(self)
