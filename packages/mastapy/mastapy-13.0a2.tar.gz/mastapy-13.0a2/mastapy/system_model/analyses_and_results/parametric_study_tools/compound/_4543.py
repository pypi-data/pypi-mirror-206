"""_4543.py

WormGearSetCompoundParametricStudyTool
"""
from typing import List

from mastapy.system_model.part_model.gears import _2531
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4414
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4541, _4542, _4478
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'WormGearSetCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetCompoundParametricStudyTool',)


class WormGearSetCompoundParametricStudyTool(_4478.GearSetCompoundParametricStudyTool):
    """WormGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_WormGearSetCompoundParametricStudyTool:
        """Special nested class for casting WormGearSetCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'WormGearSetCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def gear_set_compound_parametric_study_tool(self):
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
        def worm_gear_set_compound_parametric_study_tool(self) -> 'WormGearSetCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearSetCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2531.WormGearSet':
        """WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2531.WormGearSet':
        """WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4414.WormGearSetParametricStudyTool]':
        """List[WormGearSetParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gears_compound_parametric_study_tool(self) -> 'List[_4541.WormGearCompoundParametricStudyTool]':
        """List[WormGearCompoundParametricStudyTool]: 'WormGearsCompoundParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsCompoundParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_compound_parametric_study_tool(self) -> 'List[_4542.WormGearMeshCompoundParametricStudyTool]':
        """List[WormGearMeshCompoundParametricStudyTool]: 'WormMeshesCompoundParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesCompoundParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4414.WormGearSetParametricStudyTool]':
        """List[WormGearSetParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'WormGearSetCompoundParametricStudyTool._Cast_WormGearSetCompoundParametricStudyTool':
        return self._Cast_WormGearSetCompoundParametricStudyTool(self)
