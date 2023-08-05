"""_6480.py

StraightBevelDiffGearSetCompoundDynamicAnalysis
"""
from typing import List

from mastapy.system_model.part_model.gears import _2525
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6478, _6479, _6391
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'StraightBevelDiffGearSetCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetCompoundDynamicAnalysis',)


class StraightBevelDiffGearSetCompoundDynamicAnalysis(_6391.BevelGearSetCompoundDynamicAnalysis):
    """StraightBevelDiffGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_StraightBevelDiffGearSetCompoundDynamicAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearSetCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_set_compound_dynamic_analysis(self):
            return self._parent._cast(_6391.BevelGearSetCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6379
            
            return self._parent._cast(_6379.AGMAGleasonConicalGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6407
            
            return self._parent._cast(_6407.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6433
            
            return self._parent._cast(_6433.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6471
            
            return self._parent._cast(_6471.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6373
            
            return self._parent._cast(_6373.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6452
            
            return self._parent._cast(_6452.PartCompoundDynamicAnalysis)

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
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(self) -> 'StraightBevelDiffGearSetCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2525.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2525.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6351.StraightBevelDiffGearSetDynamicAnalysis]':
        """List[StraightBevelDiffGearSetDynamicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gears_compound_dynamic_analysis(self) -> 'List[_6478.StraightBevelDiffGearCompoundDynamicAnalysis]':
        """List[StraightBevelDiffGearCompoundDynamicAnalysis]: 'StraightBevelDiffGearsCompoundDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearsCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_meshes_compound_dynamic_analysis(self) -> 'List[_6479.StraightBevelDiffGearMeshCompoundDynamicAnalysis]':
        """List[StraightBevelDiffGearMeshCompoundDynamicAnalysis]: 'StraightBevelDiffMeshesCompoundDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshesCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6351.StraightBevelDiffGearSetDynamicAnalysis]':
        """List[StraightBevelDiffGearSetDynamicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelDiffGearSetCompoundDynamicAnalysis._Cast_StraightBevelDiffGearSetCompoundDynamicAnalysis':
        return self._Cast_StraightBevelDiffGearSetCompoundDynamicAnalysis(self)
