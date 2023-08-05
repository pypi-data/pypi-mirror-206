"""_5882.py

ConnectorCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5686
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5923
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'ConnectorCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorCompoundHarmonicAnalysis',)


class ConnectorCompoundHarmonicAnalysis(_5923.MountableComponentCompoundHarmonicAnalysis):
    """ConnectorCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_ConnectorCompoundHarmonicAnalysis:
        """Special nested class for casting ConnectorCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectorCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis(self):
            return self._parent._cast(_5923.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5871
            
            return self._parent._cast(_5871.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5925
            
            return self._parent._cast(_5925.PartCompoundHarmonicAnalysis)

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
        def bearing_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5854
            
            return self._parent._cast(_5854.BearingCompoundHarmonicAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5924
            
            return self._parent._cast(_5924.OilSealCompoundHarmonicAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5942
            
            return self._parent._cast(_5942.ShaftHubConnectionCompoundHarmonicAnalysis)

        @property
        def connector_compound_harmonic_analysis(self) -> 'ConnectorCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectorCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5686.ConnectorHarmonicAnalysis]':
        """List[ConnectorHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5686.ConnectorHarmonicAnalysis]':
        """List[ConnectorHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis':
        return self._Cast_ConnectorCompoundHarmonicAnalysis(self)
