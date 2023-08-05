"""_3932.py

GearCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3803
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3951
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'GearCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundStabilityAnalysis',)


class GearCompoundStabilityAnalysis(_3951.MountableComponentCompoundStabilityAnalysis):
    """GearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_STABILITY_ANALYSIS

    class _Cast_GearCompoundStabilityAnalysis:
        """Special nested class for casting GearCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'GearCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_stability_analysis(self):
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
        def agma_gleason_conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3878
            
            return self._parent._cast(_3878.AGMAGleasonConicalGearCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3885
            
            return self._parent._cast(_3885.BevelDifferentialGearCompoundStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3888
            
            return self._parent._cast(_3888.BevelDifferentialPlanetGearCompoundStabilityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3889
            
            return self._parent._cast(_3889.BevelDifferentialSunGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3890
            
            return self._parent._cast(_3890.BevelGearCompoundStabilityAnalysis)

        @property
        def concept_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3903
            
            return self._parent._cast(_3903.ConceptGearCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3906
            
            return self._parent._cast(_3906.ConicalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3921
            
            return self._parent._cast(_3921.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3924
            
            return self._parent._cast(_3924.CylindricalPlanetGearCompoundStabilityAnalysis)

        @property
        def face_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3927
            
            return self._parent._cast(_3927.FaceGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3936
            
            return self._parent._cast(_3936.HypoidGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3940
            
            return self._parent._cast(_3940.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3943
            
            return self._parent._cast(_3943.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3946
            
            return self._parent._cast(_3946.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3973
            
            return self._parent._cast(_3973.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3979
            
            return self._parent._cast(_3979.StraightBevelDiffGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3982
            
            return self._parent._cast(_3982.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3985
            
            return self._parent._cast(_3985.StraightBevelPlanetGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3986
            
            return self._parent._cast(_3986.StraightBevelSunGearCompoundStabilityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3997
            
            return self._parent._cast(_3997.WormGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4000
            
            return self._parent._cast(_4000.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(self) -> 'GearCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3803.GearStabilityAnalysis]':
        """List[GearStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3803.GearStabilityAnalysis]':
        """List[GearStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis':
        return self._Cast_GearCompoundStabilityAnalysis(self)
