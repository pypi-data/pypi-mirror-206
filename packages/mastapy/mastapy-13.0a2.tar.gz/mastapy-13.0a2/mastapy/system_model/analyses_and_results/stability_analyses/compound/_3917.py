"""_3917.py

CycloidalAssemblyCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.part_model.cycloidal import _2547
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3786
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3972
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'CycloidalAssemblyCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalAssemblyCompoundStabilityAnalysis',)


class CycloidalAssemblyCompoundStabilityAnalysis(_3972.SpecialisedAssemblyCompoundStabilityAnalysis):
    """CycloidalAssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS

    class _Cast_CycloidalAssemblyCompoundStabilityAnalysis:
        """Special nested class for casting CycloidalAssemblyCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'CycloidalAssemblyCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_compound_stability_analysis(self):
            return self._parent._cast(_3972.SpecialisedAssemblyCompoundStabilityAnalysis)

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
        def cycloidal_assembly_compound_stability_analysis(self) -> 'CycloidalAssemblyCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalAssemblyCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2547.CycloidalAssembly':
        """CycloidalAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2547.CycloidalAssembly':
        """CycloidalAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3786.CycloidalAssemblyStabilityAnalysis]':
        """List[CycloidalAssemblyStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3786.CycloidalAssemblyStabilityAnalysis]':
        """List[CycloidalAssemblyStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalAssemblyCompoundStabilityAnalysis._Cast_CycloidalAssemblyCompoundStabilityAnalysis':
        return self._Cast_CycloidalAssemblyCompoundStabilityAnalysis(self)
