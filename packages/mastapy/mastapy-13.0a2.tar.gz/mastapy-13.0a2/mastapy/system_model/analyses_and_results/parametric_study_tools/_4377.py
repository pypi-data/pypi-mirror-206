"""_4377.py

PulleyParametricStudyTool
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2569
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6904
from mastapy.system_model.analyses_and_results.system_deflections import _2772
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4309
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'PulleyParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyParametricStudyTool',)


class PulleyParametricStudyTool(_4309.CouplingHalfParametricStudyTool):
    """PulleyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PULLEY_PARAMETRIC_STUDY_TOOL

    class _Cast_PulleyParametricStudyTool:
        """Special nested class for casting PulleyParametricStudyTool to subclasses."""

        def __init__(self, parent: 'PulleyParametricStudyTool'):
            self._parent = parent

        @property
        def coupling_half_parametric_study_tool(self):
            return self._parent._cast(_4309.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4356
            
            return self._parent._cast(_4356.MountableComponentParametricStudyTool)

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
        def cvt_pulley_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4313
            
            return self._parent._cast(_4313.CVTPulleyParametricStudyTool)

        @property
        def pulley_parametric_study_tool(self) -> 'PulleyParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PulleyParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2569.Pulley':
        """Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6904.PulleyLoadCase':
        """PulleyLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2772.PulleySystemDeflection]':
        """List[PulleySystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PulleyParametricStudyTool._Cast_PulleyParametricStudyTool':
        return self._Cast_PulleyParametricStudyTool(self)
