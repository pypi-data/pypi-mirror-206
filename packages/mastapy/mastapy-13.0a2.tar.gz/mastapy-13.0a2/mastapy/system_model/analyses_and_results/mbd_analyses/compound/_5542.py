"""_5542.py

CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.part_model.cycloidal import _2547
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5393
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5597
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'CycloidalAssemblyCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalAssemblyCompoundMultibodyDynamicsAnalysis',)


class CycloidalAssemblyCompoundMultibodyDynamicsAnalysis(_5597.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis):
    """CycloidalAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_CycloidalAssemblyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CycloidalAssemblyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'CycloidalAssemblyCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(self):
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
        def cycloidal_assembly_compound_multibody_dynamics_analysis(self) -> 'CycloidalAssemblyCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalAssemblyCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2547.CycloidalAssembly':
        """CycloidalAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2547.CycloidalAssembly':
        """CycloidalAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5393.CycloidalAssemblyMultibodyDynamicsAnalysis]':
        """List[CycloidalAssemblyMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5393.CycloidalAssemblyMultibodyDynamicsAnalysis]':
        """List[CycloidalAssemblyMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalAssemblyCompoundMultibodyDynamicsAnalysis._Cast_CycloidalAssemblyCompoundMultibodyDynamicsAnalysis':
        return self._Cast_CycloidalAssemblyCompoundMultibodyDynamicsAnalysis(self)
