"""_4403.py

SynchroniserParametricStudyTool
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2581
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6932
from mastapy.system_model.analyses_and_results.system_deflections import _2803
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4387
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'SynchroniserParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserParametricStudyTool',)


class SynchroniserParametricStudyTool(_4387.SpecialisedAssemblyParametricStudyTool):
    """SynchroniserParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PARAMETRIC_STUDY_TOOL

    class _Cast_SynchroniserParametricStudyTool:
        """Special nested class for casting SynchroniserParametricStudyTool to subclasses."""

        def __init__(self, parent: 'SynchroniserParametricStudyTool'):
            self._parent = parent

        @property
        def specialised_assembly_parametric_study_tool(self):
            return self._parent._cast(_4387.SpecialisedAssemblyParametricStudyTool)

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
        def synchroniser_parametric_study_tool(self) -> 'SynchroniserParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2581.Synchroniser':
        """Synchroniser: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6932.SynchroniserLoadCase':
        """SynchroniserLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2803.SynchroniserSystemDeflection]':
        """List[SynchroniserSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SynchroniserParametricStudyTool._Cast_SynchroniserParametricStudyTool':
        return self._Cast_SynchroniserParametricStudyTool(self)
