"""_2929.py

ShaftToMountableComponentConnectionCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2784
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'ShaftToMountableComponentConnectionCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftToMountableComponentConnectionCompoundSystemDeflection',)


class ShaftToMountableComponentConnectionCompoundSystemDeflection(_2833.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection):
    """ShaftToMountableComponentConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'ShaftToMountableComponentConnectionCompoundSystemDeflection'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(self):
            return self._parent._cast(_2833.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection)

        @property
        def connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2865
            
            return self._parent._cast(_2865.ConnectionCompoundSystemDeflection)

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
        def coaxial_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2854
            
            return self._parent._cast(_2854.CoaxialConnectionCompoundSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2874
            
            return self._parent._cast(_2874.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection)

        @property
        def planetary_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2914
            
            return self._parent._cast(_2914.PlanetaryConnectionCompoundSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_compound_system_deflection(self) -> 'ShaftToMountableComponentConnectionCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftToMountableComponentConnectionCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_2784.ShaftToMountableComponentConnectionSystemDeflection]':
        """List[ShaftToMountableComponentConnectionSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2784.ShaftToMountableComponentConnectionSystemDeflection]':
        """List[ShaftToMountableComponentConnectionSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection':
        return self._Cast_ShaftToMountableComponentConnectionCompoundSystemDeflection(self)
