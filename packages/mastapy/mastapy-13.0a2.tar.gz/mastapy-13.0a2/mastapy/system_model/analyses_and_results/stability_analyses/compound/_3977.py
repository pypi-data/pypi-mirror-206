"""_3977.py

SpringDamperConnectionCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2331
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3845
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3912
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'SpringDamperConnectionCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionCompoundStabilityAnalysis',)


class SpringDamperConnectionCompoundStabilityAnalysis(_3912.CouplingConnectionCompoundStabilityAnalysis):
    """SpringDamperConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_STABILITY_ANALYSIS

    class _Cast_SpringDamperConnectionCompoundStabilityAnalysis:
        """Special nested class for casting SpringDamperConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'SpringDamperConnectionCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def coupling_connection_compound_stability_analysis(self):
            return self._parent._cast(_3912.CouplingConnectionCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3939
            
            return self._parent._cast(_3939.InterMountableComponentConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3909
            
            return self._parent._cast(_3909.ConnectionCompoundStabilityAnalysis)

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
        def spring_damper_connection_compound_stability_analysis(self) -> 'SpringDamperConnectionCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionCompoundStabilityAnalysis.TYPE'):
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
    def connection_analysis_cases_ready(self) -> 'List[_3845.SpringDamperConnectionStabilityAnalysis]':
        """List[SpringDamperConnectionStabilityAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3845.SpringDamperConnectionStabilityAnalysis]':
        """List[SpringDamperConnectionStabilityAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpringDamperConnectionCompoundStabilityAnalysis._Cast_SpringDamperConnectionCompoundStabilityAnalysis':
        return self._Cast_SpringDamperConnectionCompoundStabilityAnalysis(self)
