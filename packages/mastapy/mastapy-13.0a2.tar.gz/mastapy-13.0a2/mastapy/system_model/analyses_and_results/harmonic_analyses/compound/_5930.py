"""_5930.py

PlanetaryGearSetCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5761
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5895
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'PlanetaryGearSetCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryGearSetCompoundHarmonicAnalysis',)


class PlanetaryGearSetCompoundHarmonicAnalysis(_5895.CylindricalGearSetCompoundHarmonicAnalysis):
    """PlanetaryGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_PlanetaryGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting PlanetaryGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'PlanetaryGearSetCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(self):
            return self._parent._cast(_5895.CylindricalGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5906
            
            return self._parent._cast(_5906.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5944
            
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
        def planetary_gear_set_compound_harmonic_analysis(self) -> 'PlanetaryGearSetCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryGearSetCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5761.PlanetaryGearSetHarmonicAnalysis]':
        """List[PlanetaryGearSetHarmonicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5761.PlanetaryGearSetHarmonicAnalysis]':
        """List[PlanetaryGearSetHarmonicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis':
        return self._Cast_PlanetaryGearSetCompoundHarmonicAnalysis(self)
