"""_5883.py

CouplingCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5689
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5944
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'CouplingCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingCompoundHarmonicAnalysis',)


class CouplingCompoundHarmonicAnalysis(_5944.SpecialisedAssemblyCompoundHarmonicAnalysis):
    """CouplingCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_CouplingCompoundHarmonicAnalysis:
        """Special nested class for casting CouplingCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_compound_harmonic_analysis(self):
            return self._parent._cast(_5944.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5846
            
            return self._parent._cast(_5846.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5925
            
            return self._parent._cast(_5925.PartCompoundHarmonicAnalysis)

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
        def clutch_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5867
            
            return self._parent._cast(_5867.ClutchCompoundHarmonicAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5872
            
            return self._parent._cast(_5872.ConceptCouplingCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5926
            
            return self._parent._cast(_5926.PartToPartShearCouplingCompoundHarmonicAnalysis)

        @property
        def spring_damper_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5948
            
            return self._parent._cast(_5948.SpringDamperCompoundHarmonicAnalysis)

        @property
        def torque_converter_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5963
            
            return self._parent._cast(_5963.TorqueConverterCompoundHarmonicAnalysis)

        @property
        def coupling_compound_harmonic_analysis(self) -> 'CouplingCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_5689.CouplingHarmonicAnalysis]':
        """List[CouplingHarmonicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5689.CouplingHarmonicAnalysis]':
        """List[CouplingHarmonicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis':
        return self._Cast_CouplingCompoundHarmonicAnalysis(self)
