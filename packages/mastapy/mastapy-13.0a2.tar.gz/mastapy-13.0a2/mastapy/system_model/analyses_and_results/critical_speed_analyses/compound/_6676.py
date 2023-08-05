"""_6676.py

CouplingCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6546
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6737
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'CouplingCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingCompoundCriticalSpeedAnalysis',)


class CouplingCompoundCriticalSpeedAnalysis(_6737.SpecialisedAssemblyCompoundCriticalSpeedAnalysis):
    """CouplingCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_CouplingCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CouplingCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_compound_critical_speed_analysis(self):
            return self._parent._cast(_6737.SpecialisedAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def abstract_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6639
            
            return self._parent._cast(_6639.AbstractAssemblyCompoundCriticalSpeedAnalysis)

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
        def clutch_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6660
            
            return self._parent._cast(_6660.ClutchCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6665
            
            return self._parent._cast(_6665.ConceptCouplingCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6719
            
            return self._parent._cast(_6719.PartToPartShearCouplingCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6741
            
            return self._parent._cast(_6741.SpringDamperCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6756
            
            return self._parent._cast(_6756.TorqueConverterCompoundCriticalSpeedAnalysis)

        @property
        def coupling_compound_critical_speed_analysis(self) -> 'CouplingCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_6546.CouplingCriticalSpeedAnalysis]':
        """List[CouplingCriticalSpeedAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6546.CouplingCriticalSpeedAnalysis]':
        """List[CouplingCriticalSpeedAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis':
        return self._Cast_CouplingCompoundCriticalSpeedAnalysis(self)
