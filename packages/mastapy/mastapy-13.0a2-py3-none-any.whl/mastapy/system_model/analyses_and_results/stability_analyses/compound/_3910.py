"""_3910.py

ConnectorCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3778
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3951
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'ConnectorCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorCompoundStabilityAnalysis',)


class ConnectorCompoundStabilityAnalysis(_3951.MountableComponentCompoundStabilityAnalysis):
    """ConnectorCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_STABILITY_ANALYSIS

    class _Cast_ConnectorCompoundStabilityAnalysis:
        """Special nested class for casting ConnectorCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectorCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_stability_analysis(self):
            return self._parent._cast(_3951.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3899
            
            return self._parent._cast(_3899.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3953
            
            return self._parent._cast(_3953.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def bearing_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3882
            
            return self._parent._cast(_3882.BearingCompoundStabilityAnalysis)

        @property
        def oil_seal_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3952
            
            return self._parent._cast(_3952.OilSealCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3970
            
            return self._parent._cast(_3970.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(self) -> 'ConnectorCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectorCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3778.ConnectorStabilityAnalysis]':
        """List[ConnectorStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3778.ConnectorStabilityAnalysis]':
        """List[ConnectorStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectorCompoundStabilityAnalysis._Cast_ConnectorCompoundStabilityAnalysis':
        return self._Cast_ConnectorCompoundStabilityAnalysis(self)
