"""_5018.py

GearCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4890
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5037
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'GearCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundModalAnalysisAtAStiffness',)


class GearCompoundModalAnalysisAtAStiffness(_5037.MountableComponentCompoundModalAnalysisAtAStiffness):
    """GearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_GearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting GearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'GearCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_5037.MountableComponentCompoundModalAnalysisAtAStiffness)

        @property
        def component_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4985
            
            return self._parent._cast(_4985.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5039
            
            return self._parent._cast(_5039.PartCompoundModalAnalysisAtAStiffness)

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
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4964
            
            return self._parent._cast(_4964.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4971
            
            return self._parent._cast(_4971.BevelDifferentialGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4974
            
            return self._parent._cast(_4974.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4975
            
            return self._parent._cast(_4975.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4976
            
            return self._parent._cast(_4976.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4989
            
            return self._parent._cast(_4989.ConceptGearCompoundModalAnalysisAtAStiffness)

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4992
            
            return self._parent._cast(_4992.ConicalGearCompoundModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5007
            
            return self._parent._cast(_5007.CylindricalGearCompoundModalAnalysisAtAStiffness)

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5010
            
            return self._parent._cast(_5010.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness)

        @property
        def face_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5013
            
            return self._parent._cast(_5013.FaceGearCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5022
            
            return self._parent._cast(_5022.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5026
            
            return self._parent._cast(_5026.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5029
            
            return self._parent._cast(_5029.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5032
            
            return self._parent._cast(_5032.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5059
            
            return self._parent._cast(_5059.SpiralBevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5065
            
            return self._parent._cast(_5065.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5068
            
            return self._parent._cast(_5068.StraightBevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5071
            
            return self._parent._cast(_5071.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5072
            
            return self._parent._cast(_5072.StraightBevelSunGearCompoundModalAnalysisAtAStiffness)

        @property
        def worm_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5083
            
            return self._parent._cast(_5083.WormGearCompoundModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5086
            
            return self._parent._cast(_5086.ZerolBevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def gear_compound_modal_analysis_at_a_stiffness(self) -> 'GearCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4890.GearModalAnalysisAtAStiffness]':
        """List[GearModalAnalysisAtAStiffness]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4890.GearModalAnalysisAtAStiffness]':
        """List[GearModalAnalysisAtAStiffness]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness':
        return self._Cast_GearCompoundModalAnalysisAtAStiffness(self)
