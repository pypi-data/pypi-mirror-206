"""_5593.py

RootAssemblyCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5452
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5506
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'RootAssemblyCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundMultibodyDynamicsAnalysis',)


class RootAssemblyCompoundMultibodyDynamicsAnalysis(_5506.AssemblyCompoundMultibodyDynamicsAnalysis):
    """RootAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting RootAssemblyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'RootAssemblyCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def assembly_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5506.AssemblyCompoundMultibodyDynamicsAnalysis)

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
        def root_assembly_compound_multibody_dynamics_analysis(self) -> 'RootAssemblyCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5452.RootAssemblyMultibodyDynamicsAnalysis]':
        """List[RootAssemblyMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5452.RootAssemblyMultibodyDynamicsAnalysis]':
        """List[RootAssemblyMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RootAssemblyCompoundMultibodyDynamicsAnalysis._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis':
        return self._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis(self)
