"""_3979.py

StraightBevelDiffGearCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.part_model.gears import _2524
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3852
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3890
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'StraightBevelDiffGearCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearCompoundStabilityAnalysis',)


class StraightBevelDiffGearCompoundStabilityAnalysis(_3890.BevelGearCompoundStabilityAnalysis):
    """StraightBevelDiffGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_STABILITY_ANALYSIS

    class _Cast_StraightBevelDiffGearCompoundStabilityAnalysis:
        """Special nested class for casting StraightBevelDiffGearCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_compound_stability_analysis(self):
            return self._parent._cast(_3890.BevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3878
            
            return self._parent._cast(_3878.AGMAGleasonConicalGearCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3906
            
            return self._parent._cast(_3906.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3932
            
            return self._parent._cast(_3932.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3951
            
            return self._parent._cast(_3951.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3899
            
            return self._parent._cast(_3899.ComponentCompoundStabilityAnalysis)

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
        def straight_bevel_planet_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3985
            
            return self._parent._cast(_3985.StraightBevelPlanetGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3986
            
            return self._parent._cast(_3986.StraightBevelSunGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(self) -> 'StraightBevelDiffGearCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2524.StraightBevelDiffGear':
        """StraightBevelDiffGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3852.StraightBevelDiffGearStabilityAnalysis]':
        """List[StraightBevelDiffGearStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3852.StraightBevelDiffGearStabilityAnalysis]':
        """List[StraightBevelDiffGearStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis':
        return self._Cast_StraightBevelDiffGearCompoundStabilityAnalysis(self)
