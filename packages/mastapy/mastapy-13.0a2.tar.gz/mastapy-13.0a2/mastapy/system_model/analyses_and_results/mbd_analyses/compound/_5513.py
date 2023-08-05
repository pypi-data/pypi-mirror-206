"""_5513.py

BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5363
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5510
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis',)


class BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis(_5510.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis):
    """BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5510.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5515
            
            return self._parent._cast(_5515.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5503
            
            return self._parent._cast(_5503.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5531
            
            return self._parent._cast(_5531.ConicalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5557
            
            return self._parent._cast(_5557.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5576
            
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
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(self) -> 'BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_5363.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis]':
        """List[BevelDifferentialPlanetGearMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5363.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis]':
        """List[BevelDifferentialPlanetGearMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis':
        return self._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis(self)
