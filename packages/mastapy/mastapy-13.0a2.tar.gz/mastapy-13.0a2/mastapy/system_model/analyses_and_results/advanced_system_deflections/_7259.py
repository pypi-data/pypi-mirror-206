"""_7259.py

CoaxialConnectionAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.connections_and_sockets import _2250
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6800
from mastapy.system_model.analyses_and_results.system_deflections import _2693
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7335
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'CoaxialConnectionAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionAdvancedSystemDeflection',)


class CoaxialConnectionAdvancedSystemDeflection(_7335.ShaftToMountableComponentConnectionAdvancedSystemDeflection):
    """CoaxialConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_CoaxialConnectionAdvancedSystemDeflection:
        """Special nested class for casting CoaxialConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'CoaxialConnectionAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(self):
            return self._parent._cast(_7335.ShaftToMountableComponentConnectionAdvancedSystemDeflection)

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7235
            
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
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7281
            
            return self._parent._cast(_7281.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection)

        @property
        def coaxial_connection_advanced_system_deflection(self) -> 'CoaxialConnectionAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2250.CoaxialConnection':
        """CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6800.CoaxialConnectionLoadCase':
        """CoaxialConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2693.CoaxialConnectionSystemDeflection]':
        """List[CoaxialConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection':
        return self._Cast_CoaxialConnectionAdvancedSystemDeflection(self)
