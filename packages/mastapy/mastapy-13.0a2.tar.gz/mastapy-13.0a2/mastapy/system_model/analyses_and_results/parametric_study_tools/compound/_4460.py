"""_4460.py

CVTPulleyCompoundParametricStudyTool
"""
from typing import List

from mastapy.system_model.analyses_and_results.parametric_study_tools import _4313
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4506
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'CVTPulleyCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleyCompoundParametricStudyTool',)


class CVTPulleyCompoundParametricStudyTool(_4506.PulleyCompoundParametricStudyTool):
    """CVTPulleyCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_CVTPulleyCompoundParametricStudyTool:
        """Special nested class for casting CVTPulleyCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'CVTPulleyCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def pulley_compound_parametric_study_tool(self):
            return self._parent._cast(_4506.PulleyCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4457
            
            return self._parent._cast(_4457.CouplingHalfCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4495
            
            return self._parent._cast(_4495.MountableComponentCompoundParametricStudyTool)

        @property
        def component_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4443
            
            return self._parent._cast(_4443.ComponentCompoundParametricStudyTool)

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
        def cvt_pulley_compound_parametric_study_tool(self) -> 'CVTPulleyCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTPulleyCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_4313.CVTPulleyParametricStudyTool]':
        """List[CVTPulleyParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4313.CVTPulleyParametricStudyTool]':
        """List[CVTPulleyParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTPulleyCompoundParametricStudyTool._Cast_CVTPulleyCompoundParametricStudyTool':
        return self._Cast_CVTPulleyCompoundParametricStudyTool(self)
