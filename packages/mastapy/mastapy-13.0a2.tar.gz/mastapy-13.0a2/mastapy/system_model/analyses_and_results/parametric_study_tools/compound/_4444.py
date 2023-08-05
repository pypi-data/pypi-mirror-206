"""_4444.py

ConceptCouplingCompoundParametricStudyTool
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2560
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4299
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4455
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'ConceptCouplingCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingCompoundParametricStudyTool',)


class ConceptCouplingCompoundParametricStudyTool(_4455.CouplingCompoundParametricStudyTool):
    """ConceptCouplingCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_ConceptCouplingCompoundParametricStudyTool:
        """Special nested class for casting ConceptCouplingCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'ConceptCouplingCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def coupling_compound_parametric_study_tool(self):
            return self._parent._cast(_4455.CouplingCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4516
            
            return self._parent._cast(_4516.SpecialisedAssemblyCompoundParametricStudyTool)

        @property
        def abstract_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4418
            
            return self._parent._cast(_4418.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4497
            
            return self._parent._cast(_4497.PartCompoundParametricStudyTool)

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
        def concept_coupling_compound_parametric_study_tool(self) -> 'ConceptCouplingCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2560.ConceptCoupling':
        """ConceptCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2560.ConceptCoupling':
        """ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4299.ConceptCouplingParametricStudyTool]':
        """List[ConceptCouplingParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4299.ConceptCouplingParametricStudyTool]':
        """List[ConceptCouplingParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptCouplingCompoundParametricStudyTool._Cast_ConceptCouplingCompoundParametricStudyTool':
        return self._Cast_ConceptCouplingCompoundParametricStudyTool(self)
