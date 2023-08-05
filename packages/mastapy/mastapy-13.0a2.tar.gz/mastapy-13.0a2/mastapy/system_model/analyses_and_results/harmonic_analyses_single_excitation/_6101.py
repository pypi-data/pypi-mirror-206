"""_6101.py

WormGearSetHarmonicAnalysisOfSingleExcitation
"""
from typing import List

from mastapy.system_model.part_model.gears import _2531
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6948
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6099, _6100, _6035
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'WormGearSetHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetHarmonicAnalysisOfSingleExcitation',)


class WormGearSetHarmonicAnalysisOfSingleExcitation(_6035.GearSetHarmonicAnalysisOfSingleExcitation):
    """WormGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_WormGearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting WormGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'WormGearSetHarmonicAnalysisOfSingleExcitation'):
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
        def worm_gear_set_harmonic_analysis_of_single_excitation(self) -> 'WormGearSetHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearSetHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2531.WormGearSet':
        """WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6948.WormGearSetLoadCase':
        """WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_gears_harmonic_analysis_of_single_excitation(self) -> 'List[_6099.WormGearHarmonicAnalysisOfSingleExcitation]':
        """List[WormGearHarmonicAnalysisOfSingleExcitation]: 'WormGearsHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_harmonic_analysis_of_single_excitation(self) -> 'List[_6100.WormGearMeshHarmonicAnalysisOfSingleExcitation]':
        """List[WormGearMeshHarmonicAnalysisOfSingleExcitation]: 'WormMeshesHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'WormGearSetHarmonicAnalysisOfSingleExcitation._Cast_WormGearSetHarmonicAnalysisOfSingleExcitation':
        return self._Cast_WormGearSetHarmonicAnalysisOfSingleExcitation(self)
