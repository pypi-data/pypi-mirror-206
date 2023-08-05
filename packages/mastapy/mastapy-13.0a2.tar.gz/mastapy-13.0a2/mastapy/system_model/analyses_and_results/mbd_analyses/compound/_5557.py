"""_5557.py

GearCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5410
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5576
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'GearCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundMultibodyDynamicsAnalysis',)


class GearCompoundMultibodyDynamicsAnalysis(_5576.MountableComponentCompoundMultibodyDynamicsAnalysis):
    """GearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_GearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting GearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'GearCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5576.MountableComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5524
            
            return self._parent._cast(_5524.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5578
            
            return self._parent._cast(_5578.PartCompoundMultibodyDynamicsAnalysis)

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
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5503
            
            return self._parent._cast(_5503.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5510
            
            return self._parent._cast(_5510.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5513
            
            return self._parent._cast(_5513.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5514
            
            return self._parent._cast(_5514.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5515
            
            return self._parent._cast(_5515.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5528
            
            return self._parent._cast(_5528.ConceptGearCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5531
            
            return self._parent._cast(_5531.ConicalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5546
            
            return self._parent._cast(_5546.CylindricalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5549
            
            return self._parent._cast(_5549.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5552
            
            return self._parent._cast(_5552.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5561
            
            return self._parent._cast(_5561.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5565
            
            return self._parent._cast(_5565.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5568
            
            return self._parent._cast(_5568.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5571
            
            return self._parent._cast(_5571.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5598
            
            return self._parent._cast(_5598.SpiralBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5604
            
            return self._parent._cast(_5604.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5607
            
            return self._parent._cast(_5607.StraightBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5610
            
            return self._parent._cast(_5610.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5611
            
            return self._parent._cast(_5611.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5622
            
            return self._parent._cast(_5622.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5625
            
            return self._parent._cast(_5625.ZerolBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_compound_multibody_dynamics_analysis(self) -> 'GearCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5410.GearMultibodyDynamicsAnalysis]':
        """List[GearMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5410.GearMultibodyDynamicsAnalysis]':
        """List[GearMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis':
        return self._Cast_GearCompoundMultibodyDynamicsAnalysis(self)
