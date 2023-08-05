"""_6742.py

SpringDamperConnectionCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2331
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6612
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6677
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'SpringDamperConnectionCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionCompoundCriticalSpeedAnalysis',)


class SpringDamperConnectionCompoundCriticalSpeedAnalysis(_6677.CouplingConnectionCompoundCriticalSpeedAnalysis):
    """SpringDamperConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting SpringDamperConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'SpringDamperConnectionCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def coupling_connection_compound_critical_speed_analysis(self):
            return self._parent._cast(_6677.CouplingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6704
            
            return self._parent._cast(_6704.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis)

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
        def spring_damper_connection_compound_critical_speed_analysis(self) -> 'SpringDamperConnectionCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2331.SpringDamperConnection':
        """SpringDamperConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2331.SpringDamperConnection':
        """SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6612.SpringDamperConnectionCriticalSpeedAnalysis]':
        """List[SpringDamperConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6612.SpringDamperConnectionCriticalSpeedAnalysis]':
        """List[SpringDamperConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpringDamperConnectionCompoundCriticalSpeedAnalysis._Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis':
        return self._Cast_SpringDamperConnectionCompoundCriticalSpeedAnalysis(self)
