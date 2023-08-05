"""_4759.py

GearCompoundModalAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses import _4610
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4778
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'GearCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundModalAnalysis',)


class GearCompoundModalAnalysis(_4778.MountableComponentCompoundModalAnalysis):
    """GearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_MODAL_ANALYSIS

    class _Cast_GearCompoundModalAnalysis:
        """Special nested class for casting GearCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'GearCompoundModalAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis(self):
            return self._parent._cast(_4778.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4726
            
            return self._parent._cast(_4726.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4780
            
            return self._parent._cast(_4780.PartCompoundModalAnalysis)

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
        def agma_gleason_conical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4705
            
            return self._parent._cast(_4705.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4712
            
            return self._parent._cast(_4712.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4715
            
            return self._parent._cast(_4715.BevelDifferentialPlanetGearCompoundModalAnalysis)

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4716
            
            return self._parent._cast(_4716.BevelDifferentialSunGearCompoundModalAnalysis)

        @property
        def bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4717
            
            return self._parent._cast(_4717.BevelGearCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4730
            
            return self._parent._cast(_4730.ConceptGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4733
            
            return self._parent._cast(_4733.ConicalGearCompoundModalAnalysis)

        @property
        def cylindrical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4748
            
            return self._parent._cast(_4748.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4751
            
            return self._parent._cast(_4751.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4754
            
            return self._parent._cast(_4754.FaceGearCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4763
            
            return self._parent._cast(_4763.HypoidGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4767
            
            return self._parent._cast(_4767.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4770
            
            return self._parent._cast(_4770.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4773
            
            return self._parent._cast(_4773.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4800
            
            return self._parent._cast(_4800.SpiralBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4806
            
            return self._parent._cast(_4806.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4809
            
            return self._parent._cast(_4809.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4812
            
            return self._parent._cast(_4812.StraightBevelPlanetGearCompoundModalAnalysis)

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4813
            
            return self._parent._cast(_4813.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4824
            
            return self._parent._cast(_4824.WormGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4827
            
            return self._parent._cast(_4827.ZerolBevelGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(self) -> 'GearCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4610.GearModalAnalysis]':
        """List[GearModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4610.GearModalAnalysis]':
        """List[GearModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearCompoundModalAnalysis._Cast_GearCompoundModalAnalysis':
        return self._Cast_GearCompoundModalAnalysis(self)
