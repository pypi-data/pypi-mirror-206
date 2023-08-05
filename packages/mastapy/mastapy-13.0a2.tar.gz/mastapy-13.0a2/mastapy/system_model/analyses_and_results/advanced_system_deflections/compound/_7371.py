"""_7371.py

AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7235
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7403
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection',)


class AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection(_7403.ConnectionCompoundAdvancedSystemDeflection):
    """AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def connection_compound_advanced_system_deflection(self):
            return self._parent._cast(_7403.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7392
            
            return self._parent._cast(_7392.CoaxialConnectionCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7412
            
            return self._parent._cast(_7412.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7414
            
            return self._parent._cast(_7414.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection)

        @property
        def planetary_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7451
            
            return self._parent._cast(_7451.PlanetaryConnectionCompoundAdvancedSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7465
            
            return self._parent._cast(_7465.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(self) -> 'AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_7235.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection]':
        """List[AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_7235.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection]':
        """List[AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection':
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection(self)
