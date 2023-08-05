"""_3968.py

RootAssemblyCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3837
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3881
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'RootAssemblyCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundStabilityAnalysis',)


class RootAssemblyCompoundStabilityAnalysis(_3881.AssemblyCompoundStabilityAnalysis):
    """RootAssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS

    class _Cast_RootAssemblyCompoundStabilityAnalysis:
        """Special nested class for casting RootAssemblyCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'RootAssemblyCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def assembly_compound_stability_analysis(self):
            return self._parent._cast(_3881.AssemblyCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3874
            
            return self._parent._cast(_3874.AbstractAssemblyCompoundStabilityAnalysis)

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
        def root_assembly_compound_stability_analysis(self) -> 'RootAssemblyCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3837.RootAssemblyStabilityAnalysis]':
        """List[RootAssemblyStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3837.RootAssemblyStabilityAnalysis]':
        """List[RootAssemblyStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RootAssemblyCompoundStabilityAnalysis._Cast_RootAssemblyCompoundStabilityAnalysis':
        return self._Cast_RootAssemblyCompoundStabilityAnalysis(self)
