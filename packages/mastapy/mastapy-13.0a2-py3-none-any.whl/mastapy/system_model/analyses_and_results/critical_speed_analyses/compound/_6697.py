"""_6697.py

GearCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6568
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6716
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'GearCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundCriticalSpeedAnalysis',)


class GearCompoundCriticalSpeedAnalysis(_6716.MountableComponentCompoundCriticalSpeedAnalysis):
    """GearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_GearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting GearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'GearCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_critical_speed_analysis(self):
            return self._parent._cast(_6716.MountableComponentCompoundCriticalSpeedAnalysis)

        @property
        def component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6664
            
            return self._parent._cast(_6664.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6718
            
            return self._parent._cast(_6718.PartCompoundCriticalSpeedAnalysis)

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
        def agma_gleason_conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6643
            
            return self._parent._cast(_6643.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6650
            
            return self._parent._cast(_6650.BevelDifferentialGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6653
            
            return self._parent._cast(_6653.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6654
            
            return self._parent._cast(_6654.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6655
            
            return self._parent._cast(_6655.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6668
            
            return self._parent._cast(_6668.ConceptGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6671
            
            return self._parent._cast(_6671.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6686
            
            return self._parent._cast(_6686.CylindricalGearCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6689
            
            return self._parent._cast(_6689.CylindricalPlanetGearCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6692
            
            return self._parent._cast(_6692.FaceGearCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6701
            
            return self._parent._cast(_6701.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6705
            
            return self._parent._cast(_6705.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6708
            
            return self._parent._cast(_6708.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6711
            
            return self._parent._cast(_6711.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6738
            
            return self._parent._cast(_6738.SpiralBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6744
            
            return self._parent._cast(_6744.StraightBevelDiffGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6747
            
            return self._parent._cast(_6747.StraightBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6750
            
            return self._parent._cast(_6750.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6751
            
            return self._parent._cast(_6751.StraightBevelSunGearCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6762
            
            return self._parent._cast(_6762.WormGearCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6765
            
            return self._parent._cast(_6765.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(self) -> 'GearCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6568.GearCriticalSpeedAnalysis]':
        """List[GearCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6568.GearCriticalSpeedAnalysis]':
        """List[GearCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis':
        return self._Cast_GearCompoundCriticalSpeedAnalysis(self)
