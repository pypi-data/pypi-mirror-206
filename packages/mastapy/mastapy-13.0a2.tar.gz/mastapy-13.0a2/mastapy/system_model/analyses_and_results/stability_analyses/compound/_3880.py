"""_3880.py

AGMAGleasonConicalGearSetCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3747
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3908
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'AGMAGleasonConicalGearSetCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearSetCompoundStabilityAnalysis',)


class AGMAGleasonConicalGearSetCompoundStabilityAnalysis(_3908.ConicalGearSetCompoundStabilityAnalysis):
    """AGMAGleasonConicalGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS

    class _Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearSetCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def conical_gear_set_compound_stability_analysis(self):
            return self._parent._cast(_3908.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3934
            
            return self._parent._cast(_3934.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3972
            
            return self._parent._cast(_3972.SpecialisedAssemblyCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3874
            
            return self._parent._cast(_3874.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3953
            
            return self._parent._cast(_3953.PartCompoundStabilityAnalysis)

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
        def bevel_differential_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3887
            
            return self._parent._cast(_3887.BevelDifferentialGearSetCompoundStabilityAnalysis)

        @property
        def bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3892
            
            return self._parent._cast(_3892.BevelGearSetCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3938
            
            return self._parent._cast(_3938.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3975
            
            return self._parent._cast(_3975.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3981
            
            return self._parent._cast(_3981.StraightBevelDiffGearSetCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3984
            
            return self._parent._cast(_3984.StraightBevelGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4002
            
            return self._parent._cast(_4002.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(self) -> 'AGMAGleasonConicalGearSetCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearSetCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_3747.AGMAGleasonConicalGearSetStabilityAnalysis]':
        """List[AGMAGleasonConicalGearSetStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3747.AGMAGleasonConicalGearSetStabilityAnalysis]':
        """List[AGMAGleasonConicalGearSetStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis':
        return self._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis(self)
