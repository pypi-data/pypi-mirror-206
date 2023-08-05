"""_2747.py

KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
"""
from mastapy.system_model.connections_and_sockets.gears import _2299
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4076
from mastapy.system_model.analyses_and_results.system_deflections import _2703
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'KlingelnbergCycloPalloidConicalGearMeshSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearMeshSystemDeflection',)


class KlingelnbergCycloPalloidConicalGearMeshSystemDeflection(_2703.ConicalGearMeshSystemDeflection):
    """KlingelnbergCycloPalloidConicalGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_SYSTEM_DEFLECTION

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshSystemDeflection to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearMeshSystemDeflection'):
            self._parent = parent

        @property
        def conical_gear_mesh_system_deflection(self):
            return self._parent._cast(_2703.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2738
            
            return self._parent._cast(_2738.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2746
            
            return self._parent._cast(_2746.InterMountableComponentConnectionSystemDeflection)

        @property
        def connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2706
            
            return self._parent._cast(_2706.ConnectionSystemDeflection)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2750
            
            return self._parent._cast(_2750.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2753
            
            return self._parent._cast(_2753.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(self) -> 'KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearMeshSystemDeflection.TYPE'):
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
    def power_flow_results(self) -> '_4076.KlingelnbergCycloPalloidConicalGearMeshPowerFlow':
        """KlingelnbergCycloPalloidConicalGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshSystemDeflection(self)
