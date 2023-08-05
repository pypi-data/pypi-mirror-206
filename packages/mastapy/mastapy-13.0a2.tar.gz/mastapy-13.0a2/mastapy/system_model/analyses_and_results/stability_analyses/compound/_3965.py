"""_3965.py

RollingRingAssemblyCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2576
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3834
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3972
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'RollingRingAssemblyCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingAssemblyCompoundStabilityAnalysis',)


class RollingRingAssemblyCompoundStabilityAnalysis(_3972.SpecialisedAssemblyCompoundStabilityAnalysis):
    """RollingRingAssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS

    class _Cast_RollingRingAssemblyCompoundStabilityAnalysis:
        """Special nested class for casting RollingRingAssemblyCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'RollingRingAssemblyCompoundStabilityAnalysis'):
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
        def rolling_ring_assembly_compound_stability_analysis(self) -> 'RollingRingAssemblyCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingRingAssemblyCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2576.RollingRingAssembly':
        """RollingRingAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2576.RollingRingAssembly':
        """RollingRingAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3834.RollingRingAssemblyStabilityAnalysis]':
        """List[RollingRingAssemblyStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3834.RollingRingAssemblyStabilityAnalysis]':
        """List[RollingRingAssemblyStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RollingRingAssemblyCompoundStabilityAnalysis._Cast_RollingRingAssemblyCompoundStabilityAnalysis':
        return self._Cast_RollingRingAssemblyCompoundStabilityAnalysis(self)
