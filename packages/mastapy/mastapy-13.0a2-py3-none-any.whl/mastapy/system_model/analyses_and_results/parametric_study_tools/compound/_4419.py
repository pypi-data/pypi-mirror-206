"""_4419.py

AbstractShaftCompoundParametricStudyTool
"""
from typing import List

from mastapy.system_model.analyses_and_results.parametric_study_tools import _4273
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4420
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'AbstractShaftCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftCompoundParametricStudyTool',)


class AbstractShaftCompoundParametricStudyTool(_4420.AbstractShaftOrHousingCompoundParametricStudyTool):
    """AbstractShaftCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_AbstractShaftCompoundParametricStudyTool:
        """Special nested class for casting AbstractShaftCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'AbstractShaftCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(self):
            return self._parent._cast(_4420.AbstractShaftOrHousingCompoundParametricStudyTool)

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
        def cycloidal_disc_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4463
            
            return self._parent._cast(_4463.CycloidalDiscCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4513
            
            return self._parent._cast(_4513.ShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_compound_parametric_study_tool(self) -> 'AbstractShaftCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4273.AbstractShaftParametricStudyTool]':
        """List[AbstractShaftParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4273.AbstractShaftParametricStudyTool]':
        """List[AbstractShaftParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftCompoundParametricStudyTool._Cast_AbstractShaftCompoundParametricStudyTool':
        return self._Cast_AbstractShaftCompoundParametricStudyTool(self)
