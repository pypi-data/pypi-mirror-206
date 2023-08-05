"""_6409.py

ConnectorCompoundDynamicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6450
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'ConnectorCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorCompoundDynamicAnalysis',)


class ConnectorCompoundDynamicAnalysis(_6450.MountableComponentCompoundDynamicAnalysis):
    """ConnectorCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_ConnectorCompoundDynamicAnalysis:
        """Special nested class for casting ConnectorCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectorCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_dynamic_analysis(self):
            return self._parent._cast(_6450.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6398
            
            return self._parent._cast(_6398.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6452
            
            return self._parent._cast(_6452.PartCompoundDynamicAnalysis)

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
        def bearing_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6381
            
            return self._parent._cast(_6381.BearingCompoundDynamicAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6451
            
            return self._parent._cast(_6451.OilSealCompoundDynamicAnalysis)

        @property
        def shaft_hub_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6469
            
            return self._parent._cast(_6469.ShaftHubConnectionCompoundDynamicAnalysis)

        @property
        def connector_compound_dynamic_analysis(self) -> 'ConnectorCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectorCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6279.ConnectorDynamicAnalysis]':
        """List[ConnectorDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6279.ConnectorDynamicAnalysis]':
        """List[ConnectorDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis':
        return self._Cast_ConnectorCompoundDynamicAnalysis(self)
