"""_5906.py

GearSetCompoundHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5727
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5944
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'GearSetCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetCompoundHarmonicAnalysis',)


class GearSetCompoundHarmonicAnalysis(_5944.SpecialisedAssemblyCompoundHarmonicAnalysis):
    """GearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_GearSetCompoundHarmonicAnalysis:
        """Special nested class for casting GearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'GearSetCompoundHarmonicAnalysis'):
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
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5852
            
            return self._parent._cast(_5852.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5859
            
            return self._parent._cast(_5859.BevelDifferentialGearSetCompoundHarmonicAnalysis)

        @property
        def bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5864
            
            return self._parent._cast(_5864.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def concept_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5877
            
            return self._parent._cast(_5877.ConceptGearSetCompoundHarmonicAnalysis)

        @property
        def conical_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5880
            
            return self._parent._cast(_5880.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5895
            
            return self._parent._cast(_5895.CylindricalGearSetCompoundHarmonicAnalysis)

        @property
        def face_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5901
            
            return self._parent._cast(_5901.FaceGearSetCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5910
            
            return self._parent._cast(_5910.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5914
            
            return self._parent._cast(_5914.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5917
            
            return self._parent._cast(_5917.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5920
            
            return self._parent._cast(_5920.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def planetary_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5930
            
            return self._parent._cast(_5930.PlanetaryGearSetCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5947
            
            return self._parent._cast(_5947.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5953
            
            return self._parent._cast(_5953.StraightBevelDiffGearSetCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5956
            
            return self._parent._cast(_5956.StraightBevelGearSetCompoundHarmonicAnalysis)

        @property
        def worm_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5971
            
            return self._parent._cast(_5971.WormGearSetCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5974
            
            return self._parent._cast(_5974.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(self) -> 'GearSetCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_5727.GearSetHarmonicAnalysis]':
        """List[GearSetHarmonicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5727.GearSetHarmonicAnalysis]':
        """List[GearSetHarmonicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearSetCompoundHarmonicAnalysis._Cast_GearSetCompoundHarmonicAnalysis':
        return self._Cast_GearSetCompoundHarmonicAnalysis(self)
