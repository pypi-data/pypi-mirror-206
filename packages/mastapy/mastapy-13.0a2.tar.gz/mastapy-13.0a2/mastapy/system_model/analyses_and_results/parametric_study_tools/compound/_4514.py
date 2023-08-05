"""_4514.py

ShaftHubConnectionCompoundParametricStudyTool
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2577
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4384
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4454
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'ShaftHubConnectionCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionCompoundParametricStudyTool',)


class ShaftHubConnectionCompoundParametricStudyTool(_4454.ConnectorCompoundParametricStudyTool):
    """ShaftHubConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_ShaftHubConnectionCompoundParametricStudyTool:
        """Special nested class for casting ShaftHubConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'ShaftHubConnectionCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def connector_compound_parametric_study_tool(self):
            return self._parent._cast(_4454.ConnectorCompoundParametricStudyTool)

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
        def shaft_hub_connection_compound_parametric_study_tool(self) -> 'ShaftHubConnectionCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2577.ShaftHubConnection':
        """ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4384.ShaftHubConnectionParametricStudyTool]':
        """List[ShaftHubConnectionParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[ShaftHubConnectionCompoundParametricStudyTool]':
        """List[ShaftHubConnectionCompoundParametricStudyTool]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4384.ShaftHubConnectionParametricStudyTool]':
        """List[ShaftHubConnectionParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftHubConnectionCompoundParametricStudyTool._Cast_ShaftHubConnectionCompoundParametricStudyTool':
        return self._Cast_ShaftHubConnectionCompoundParametricStudyTool(self)
