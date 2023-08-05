"""_5054.py

RootAssemblyCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4925
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4967
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'RootAssemblyCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundModalAnalysisAtAStiffness',)


class RootAssemblyCompoundModalAnalysisAtAStiffness(_4967.AssemblyCompoundModalAnalysisAtAStiffness):
    """RootAssemblyCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_RootAssemblyCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting RootAssemblyCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'RootAssemblyCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def assembly_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4967.AssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4960
            
            return self._parent._cast(_4960.AbstractAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5039
            
            return self._parent._cast(_5039.PartCompoundModalAnalysisAtAStiffness)

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
        def root_assembly_compound_modal_analysis_at_a_stiffness(self) -> 'RootAssemblyCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4925.RootAssemblyModalAnalysisAtAStiffness]':
        """List[RootAssemblyModalAnalysisAtAStiffness]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4925.RootAssemblyModalAnalysisAtAStiffness]':
        """List[RootAssemblyModalAnalysisAtAStiffness]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RootAssemblyCompoundModalAnalysisAtAStiffness._Cast_RootAssemblyCompoundModalAnalysisAtAStiffness':
        return self._Cast_RootAssemblyCompoundModalAnalysisAtAStiffness(self)
