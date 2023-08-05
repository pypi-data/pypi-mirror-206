"""_6176.py

KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.part_model.gears import _2518
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6047
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6174, _6175, _6173
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation',)


class KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation(_6173.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6173.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6139
            
            return self._parent._cast(_6139.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6165
            
            return self._parent._cast(_6165.GearSetCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6203
            
            return self._parent._cast(_6203.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6105
            
            return self._parent._cast(_6105.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def part_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6184
            
            return self._parent._cast(_6184.PartCompoundHarmonicAnalysisOfSingleExcitation)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(self) -> 'KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2518.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2518.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6047.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation]':
        """List[KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_harmonic_analysis_of_single_excitation(self) -> 'List[_6174.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation]':
        """List[KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation]: 'KlingelnbergCycloPalloidHypoidGearsCompoundHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_harmonic_analysis_of_single_excitation(self) -> 'List[_6175.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation]: 'KlingelnbergCycloPalloidHypoidMeshesCompoundHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6047.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation]':
        """List[KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation(self)
