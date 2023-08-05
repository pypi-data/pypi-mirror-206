"""_5536.py

CouplingCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5389
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5597
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'CouplingCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingCompoundMultibodyDynamicsAnalysis',)


class CouplingCompoundMultibodyDynamicsAnalysis(_5597.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis):
    """CouplingCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_CouplingCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CouplingCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingCompoundMultibodyDynamicsAnalysis'):
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
        def clutch_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5520
            
            return self._parent._cast(_5520.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5525
            
            return self._parent._cast(_5525.ConceptCouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5579
            
            return self._parent._cast(_5579.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def spring_damper_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5601
            
            return self._parent._cast(_5601.SpringDamperCompoundMultibodyDynamicsAnalysis)

        @property
        def torque_converter_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5616
            
            return self._parent._cast(_5616.TorqueConverterCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_compound_multibody_dynamics_analysis(self) -> 'CouplingCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_5389.CouplingMultibodyDynamicsAnalysis]':
        """List[CouplingMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5389.CouplingMultibodyDynamicsAnalysis]':
        """List[CouplingMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingCompoundMultibodyDynamicsAnalysis._Cast_CouplingCompoundMultibodyDynamicsAnalysis':
        return self._Cast_CouplingCompoundMultibodyDynamicsAnalysis(self)
