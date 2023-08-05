"""_6663.py

CoaxialConnectionCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.connections_and_sockets import _2250
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6532
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6736
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'CoaxialConnectionCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionCompoundCriticalSpeedAnalysis',)


class CoaxialConnectionCompoundCriticalSpeedAnalysis(_6736.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis):
    """CoaxialConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CoaxialConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'CoaxialConnectionCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_critical_speed_analysis(self):
            return self._parent._cast(_6736.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6642
            
            return self._parent._cast(_6642.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6674
            
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
        def cycloidal_disc_central_bearing_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6683
            
            return self._parent._cast(_6683.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def coaxial_connection_compound_critical_speed_analysis(self) -> 'CoaxialConnectionCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2250.CoaxialConnection':
        """CoaxialConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def connection_analysis_cases_ready(self) -> 'List[_6532.CoaxialConnectionCriticalSpeedAnalysis]':
        """List[CoaxialConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6532.CoaxialConnectionCriticalSpeedAnalysis]':
        """List[CoaxialConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CoaxialConnectionCompoundCriticalSpeedAnalysis._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis':
        return self._Cast_CoaxialConnectionCompoundCriticalSpeedAnalysis(self)
