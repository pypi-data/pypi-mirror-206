"""_4383.py

RootAssemblyParametricStudyTool
"""
from typing import List

from mastapy.system_model.part_model import _2454
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4363, _4365, _4278
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2882
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'RootAssemblyParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyParametricStudyTool',)


class RootAssemblyParametricStudyTool(_4278.AssemblyParametricStudyTool):
    """RootAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_PARAMETRIC_STUDY_TOOL

    class _Cast_RootAssemblyParametricStudyTool:
        """Special nested class for casting RootAssemblyParametricStudyTool to subclasses."""

        def __init__(self, parent: 'RootAssemblyParametricStudyTool'):
            self._parent = parent

        @property
        def assembly_parametric_study_tool(self):
            return self._parent._cast(_4278.AssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4271
            
            return self._parent._cast(_4271.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4368
            
            return self._parent._cast(_4368.PartParametricStudyTool)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def root_assembly_parametric_study_tool(self) -> 'RootAssemblyParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2454.RootAssembly':
        """RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def parametric_study_tool_inputs(self) -> '_4363.ParametricStudyTool':
        """ParametricStudyTool: 'ParametricStudyToolInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParametricStudyToolInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results_for_reporting(self) -> '_4365.ParametricStudyToolResultsForReporting':
        """ParametricStudyToolResultsForReporting: 'ResultsForReporting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsForReporting

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def root_assembly_duty_cycle_results(self) -> 'List[_2882.DutyCycleEfficiencyResults]':
        """List[DutyCycleEfficiencyResults]: 'RootAssemblyDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootAssemblyDutyCycleResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RootAssemblyParametricStudyTool._Cast_RootAssemblyParametricStudyTool':
        return self._Cast_RootAssemblyParametricStudyTool(self)
