"""_7200.py

ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from typing import List

from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7071
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7106
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation',)


class ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(_7106.AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation):
    """ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7106.AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7138
            
            return self._parent._cast(_7138.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

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
        def coaxial_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7127
            
            return self._parent._cast(_7127.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7147
            
            return self._parent._cast(_7147.CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planetary_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7186
            
            return self._parent._cast(_7186.PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_7071.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation]':
        """List[ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_7071.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation]':
        """List[ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(self)
