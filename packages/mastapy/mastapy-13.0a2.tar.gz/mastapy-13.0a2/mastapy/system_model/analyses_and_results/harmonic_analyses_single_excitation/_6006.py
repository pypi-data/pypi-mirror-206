"""_6006.py

ConceptGearSetHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.part_model.gears import _2501
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6807
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6004, _6005, _6035
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'ConceptGearSetHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetHarmonicAnalysisOfSingleExcitation',)


class ConceptGearSetHarmonicAnalysisOfSingleExcitation(_6035.GearSetHarmonicAnalysisOfSingleExcitation):
    """ConceptGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_ConceptGearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConceptGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'ConceptGearSetHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def gear_set_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6035.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6074
            
            return self._parent._cast(_6074.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5975
            
            return self._parent._cast(_5975.AbstractAssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6055
            
            return self._parent._cast(_6055.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(self) -> 'ConceptGearSetHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearSetHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2501.ConceptGearSet':
        """ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6807.ConceptGearSetLoadCase':
        """ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gears_harmonic_analysis_of_single_excitation(self) -> 'List[_6004.ConceptGearHarmonicAnalysisOfSingleExcitation]':
        """List[ConceptGearHarmonicAnalysisOfSingleExcitation]: 'ConceptGearsHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_harmonic_analysis_of_single_excitation(self) -> 'List[_6005.ConceptGearMeshHarmonicAnalysisOfSingleExcitation]':
        """List[ConceptGearMeshHarmonicAnalysisOfSingleExcitation]: 'ConceptMeshesHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearSetHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearSetHarmonicAnalysisOfSingleExcitation':
        return self._Cast_ConceptGearSetHarmonicAnalysisOfSingleExcitation(self)
