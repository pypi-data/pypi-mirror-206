"""_4436.py

BevelGearSetCompoundParametricStudyTool
"""
from typing import List

from mastapy.system_model.analyses_and_results.parametric_study_tools import _4289
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'BevelGearSetCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearSetCompoundParametricStudyTool',)


class BevelGearSetCompoundParametricStudyTool(_4424.AGMAGleasonConicalGearSetCompoundParametricStudyTool):
    """BevelGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_BevelGearSetCompoundParametricStudyTool:
        """Special nested class for casting BevelGearSetCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'BevelGearSetCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(self):
            return self._parent._cast(_4424.AGMAGleasonConicalGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4452
            
            return self._parent._cast(_4452.ConicalGearSetCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4478
            
            return self._parent._cast(_4478.GearSetCompoundParametricStudyTool)

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
        def bevel_differential_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4431
            
            return self._parent._cast(_4431.BevelDifferentialGearSetCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4519
            
            return self._parent._cast(_4519.SpiralBevelGearSetCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4525
            
            return self._parent._cast(_4525.StraightBevelDiffGearSetCompoundParametricStudyTool)

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4528
            
            return self._parent._cast(_4528.StraightBevelGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4546
            
            return self._parent._cast(_4546.ZerolBevelGearSetCompoundParametricStudyTool)

        @property
        def bevel_gear_set_compound_parametric_study_tool(self) -> 'BevelGearSetCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearSetCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_4289.BevelGearSetParametricStudyTool]':
        """List[BevelGearSetParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4289.BevelGearSetParametricStudyTool]':
        """List[BevelGearSetParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelGearSetCompoundParametricStudyTool._Cast_BevelGearSetCompoundParametricStudyTool':
        return self._Cast_BevelGearSetCompoundParametricStudyTool(self)
