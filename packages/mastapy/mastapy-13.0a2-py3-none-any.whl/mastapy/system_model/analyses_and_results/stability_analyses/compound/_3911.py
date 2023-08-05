"""_3911.py

CouplingCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3781
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3972
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'CouplingCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingCompoundStabilityAnalysis',)


class CouplingCompoundStabilityAnalysis(_3972.SpecialisedAssemblyCompoundStabilityAnalysis):
    """CouplingCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_STABILITY_ANALYSIS

    class _Cast_CouplingCompoundStabilityAnalysis:
        """Special nested class for casting CouplingCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_compound_stability_analysis(self):
            return self._parent._cast(_3972.SpecialisedAssemblyCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3874
            
            return self._parent._cast(_3874.AbstractAssemblyCompoundStabilityAnalysis)

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
        def clutch_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3895
            
            return self._parent._cast(_3895.ClutchCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3900
            
            return self._parent._cast(_3900.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3954
            
            return self._parent._cast(_3954.PartToPartShearCouplingCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3976
            
            return self._parent._cast(_3976.SpringDamperCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3991
            
            return self._parent._cast(_3991.TorqueConverterCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(self) -> 'CouplingCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_3781.CouplingStabilityAnalysis]':
        """List[CouplingStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3781.CouplingStabilityAnalysis]':
        """List[CouplingStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis':
        return self._Cast_CouplingCompoundStabilityAnalysis(self)
