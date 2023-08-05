"""_2874.py

CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2715
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'CycloidalDiscCentralBearingConnectionCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionCompoundSystemDeflection',)


class CycloidalDiscCentralBearingConnectionCompoundSystemDeflection(_2854.CoaxialConnectionCompoundSystemDeflection):
    """CycloidalDiscCentralBearingConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionCompoundSystemDeflection'):
            self._parent = parent

        @property
        def coaxial_connection_compound_system_deflection(self):
            return self._parent._cast(_2854.CoaxialConnectionCompoundSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2929
            
            return self._parent._cast(_2929.ShaftToMountableComponentConnectionCompoundSystemDeflection)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2833
            
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
        def cycloidal_disc_central_bearing_connection_compound_system_deflection(self) -> 'CycloidalDiscCentralBearingConnectionCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2715.CycloidalDiscCentralBearingConnectionSystemDeflection]':
        """List[CycloidalDiscCentralBearingConnectionSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_2715.CycloidalDiscCentralBearingConnectionSystemDeflection]':
        """List[CycloidalDiscCentralBearingConnectionSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionCompoundSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection':
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundSystemDeflection(self)
