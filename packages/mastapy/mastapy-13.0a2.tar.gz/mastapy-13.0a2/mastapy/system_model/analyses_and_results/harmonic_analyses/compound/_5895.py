"""_5895.py

CylindricalGearSetCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.part_model.gears import _2505
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5699
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5893, _5894, _5906
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'CylindricalGearSetCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetCompoundHarmonicAnalysis',)


class CylindricalGearSetCompoundHarmonicAnalysis(_5906.GearSetCompoundHarmonicAnalysis):
    """CylindricalGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_CylindricalGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting CylindricalGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def gear_set_compound_harmonic_analysis(self):
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
        def planetary_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5930
            
            return self._parent._cast(_5930.PlanetaryGearSetCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(self) -> 'CylindricalGearSetCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2505.CylindricalGearSet':
        """CylindricalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2505.CylindricalGearSet':
        """CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5699.CylindricalGearSetHarmonicAnalysis]':
        """List[CylindricalGearSetHarmonicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gears_compound_harmonic_analysis(self) -> 'List[_5893.CylindricalGearCompoundHarmonicAnalysis]':
        """List[CylindricalGearCompoundHarmonicAnalysis]: 'CylindricalGearsCompoundHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearsCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_meshes_compound_harmonic_analysis(self) -> 'List[_5894.CylindricalGearMeshCompoundHarmonicAnalysis]':
        """List[CylindricalGearMeshCompoundHarmonicAnalysis]: 'CylindricalMeshesCompoundHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshesCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5699.CylindricalGearSetHarmonicAnalysis]':
        """List[CylindricalGearSetHarmonicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearSetCompoundHarmonicAnalysis._Cast_CylindricalGearSetCompoundHarmonicAnalysis':
        return self._Cast_CylindricalGearSetCompoundHarmonicAnalysis(self)
