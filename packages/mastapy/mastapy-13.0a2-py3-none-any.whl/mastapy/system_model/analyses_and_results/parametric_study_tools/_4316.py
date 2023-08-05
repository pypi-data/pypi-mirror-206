"""_4316.py

CycloidalDiscParametricStudyTool
"""
from typing import List

from mastapy.system_model.part_model.cycloidal import _2548
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6823
from mastapy.system_model.analyses_and_results.system_deflections import _2717
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4273
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'CycloidalDiscParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscParametricStudyTool',)


class CycloidalDiscParametricStudyTool(_4273.AbstractShaftParametricStudyTool):
    """CycloidalDiscParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PARAMETRIC_STUDY_TOOL

    class _Cast_CycloidalDiscParametricStudyTool:
        """Special nested class for casting CycloidalDiscParametricStudyTool to subclasses."""

        def __init__(self, parent: 'CycloidalDiscParametricStudyTool'):
            self._parent = parent

        @property
        def abstract_shaft_parametric_study_tool(self):
            return self._parent._cast(_4273.AbstractShaftParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4272
            
            return self._parent._cast(_4272.AbstractShaftOrHousingParametricStudyTool)

        @property
        def component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4296
            
            return self._parent._cast(_4296.ComponentParametricStudyTool)

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
        def cycloidal_disc_parametric_study_tool(self) -> 'CycloidalDiscParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2548.CycloidalDisc':
        """CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6823.CycloidalDiscLoadCase':
        """CycloidalDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2717.CycloidalDiscSystemDeflection]':
        """List[CycloidalDiscSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscParametricStudyTool._Cast_CycloidalDiscParametricStudyTool':
        return self._Cast_CycloidalDiscParametricStudyTool(self)
