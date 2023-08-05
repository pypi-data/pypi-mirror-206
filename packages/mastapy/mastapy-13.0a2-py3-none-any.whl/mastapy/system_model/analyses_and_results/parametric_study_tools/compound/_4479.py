"""_4479.py

GuideDxfModelCompoundParametricStudyTool
"""
from typing import List

from mastapy.system_model.part_model import _2435
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4339
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4443
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'GuideDxfModelCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelCompoundParametricStudyTool',)


class GuideDxfModelCompoundParametricStudyTool(_4443.ComponentCompoundParametricStudyTool):
    """GuideDxfModelCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_GuideDxfModelCompoundParametricStudyTool:
        """Special nested class for casting GuideDxfModelCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'GuideDxfModelCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def component_compound_parametric_study_tool(self):
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
        def guide_dxf_model_compound_parametric_study_tool(self) -> 'GuideDxfModelCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GuideDxfModelCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2435.GuideDxfModel':
        """GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4339.GuideDxfModelParametricStudyTool]':
        """List[GuideDxfModelParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4339.GuideDxfModelParametricStudyTool]':
        """List[GuideDxfModelParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GuideDxfModelCompoundParametricStudyTool._Cast_GuideDxfModelCompoundParametricStudyTool':
        return self._Cast_GuideDxfModelCompoundParametricStudyTool(self)
