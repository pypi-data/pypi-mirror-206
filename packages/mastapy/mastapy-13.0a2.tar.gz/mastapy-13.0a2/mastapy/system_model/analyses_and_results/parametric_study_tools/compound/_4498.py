"""_4498.py

PartToPartShearCouplingCompoundParametricStudyTool
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2567
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4371
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4455
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'PartToPartShearCouplingCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingCompoundParametricStudyTool',)


class PartToPartShearCouplingCompoundParametricStudyTool(_4455.CouplingCompoundParametricStudyTool):
    """PartToPartShearCouplingCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_PartToPartShearCouplingCompoundParametricStudyTool:
        """Special nested class for casting PartToPartShearCouplingCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'PartToPartShearCouplingCompoundParametricStudyTool'):
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
        def part_to_part_shear_coupling_compound_parametric_study_tool(self) -> 'PartToPartShearCouplingCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2567.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2567.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4371.PartToPartShearCouplingParametricStudyTool]':
        """List[PartToPartShearCouplingParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4371.PartToPartShearCouplingParametricStudyTool]':
        """List[PartToPartShearCouplingParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartToPartShearCouplingCompoundParametricStudyTool._Cast_PartToPartShearCouplingCompoundParametricStudyTool':
        return self._Cast_PartToPartShearCouplingCompoundParametricStudyTool(self)
