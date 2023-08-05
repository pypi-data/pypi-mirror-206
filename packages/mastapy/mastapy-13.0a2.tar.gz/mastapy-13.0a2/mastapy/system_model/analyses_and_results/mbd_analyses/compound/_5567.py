"""_5567.py

KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5423
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5533
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis',)


class KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis(_5533.ConicalGearSetCompoundMultibodyDynamicsAnalysis):
    """KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5533.ConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5559
            
            return self._parent._cast(_5559.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5597
            
            return self._parent._cast(_5597.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5499
            
            return self._parent._cast(_5499.AbstractAssemblyCompoundMultibodyDynamicsAnalysis)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5570
            
            return self._parent._cast(_5570.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5573
            
            return self._parent._cast(_5573.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(self) -> 'KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_5423.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis]':
        """List[KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5423.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis]':
        """List[KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis':
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis(self)
