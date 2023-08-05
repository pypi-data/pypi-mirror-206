"""_6642.py

AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6511
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6674
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis',)


class AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis(_6674.ConnectionCompoundCriticalSpeedAnalysis):
    """AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def connection_compound_critical_speed_analysis(self):
            return self._parent._cast(_6674.ConnectionCompoundCriticalSpeedAnalysis)

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
        def coaxial_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6663
            
            return self._parent._cast(_6663.CoaxialConnectionCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6683
            
            return self._parent._cast(_6683.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6685
            
            return self._parent._cast(_6685.CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def planetary_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6722
            
            return self._parent._cast(_6722.PlanetaryConnectionCompoundCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6736
            
            return self._parent._cast(_6736.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_critical_speed_analysis(self) -> 'AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6511.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis]':
        """List[AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6511.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis]':
        """List[AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis':
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis(self)
