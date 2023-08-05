"""_7335.py

ShaftToMountableComponentConnectionAdvancedSystemDeflection
"""
from mastapy.system_model.connections_and_sockets import _2276
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ShaftToMountableComponentConnectionAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftToMountableComponentConnectionAdvancedSystemDeflection',)


class ShaftToMountableComponentConnectionAdvancedSystemDeflection(_7235.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection):
    """ShaftToMountableComponentConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_ShaftToMountableComponentConnectionAdvancedSystemDeflection:
        """Special nested class for casting ShaftToMountableComponentConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'ShaftToMountableComponentConnectionAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(self):
            return self._parent._cast(_7235.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection)

        @property
        def connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7270
            
            return self._parent._cast(_7270.ConnectionAdvancedSystemDeflection)

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
        def coaxial_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7259
            
            return self._parent._cast(_7259.CoaxialConnectionAdvancedSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7281
            
            return self._parent._cast(_7281.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection)

        @property
        def planetary_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7321
            
            return self._parent._cast(_7321.PlanetaryConnectionAdvancedSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(self) -> 'ShaftToMountableComponentConnectionAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftToMountableComponentConnectionAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2276.ShaftToMountableComponentConnection':
        """ShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionAdvancedSystemDeflection':
        return self._Cast_ShaftToMountableComponentConnectionAdvancedSystemDeflection(self)
