"""_6091.py

SynchroniserPartHarmonicAnalysisOfSingleExcitation
"""
from mastapy.system_model.part_model.couplings import _2584
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6013
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'SynchroniserPartHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserPartHarmonicAnalysisOfSingleExcitation',)


class SynchroniserPartHarmonicAnalysisOfSingleExcitation(_6013.CouplingHalfHarmonicAnalysisOfSingleExcitation):
    """SynchroniserPartHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SynchroniserPartHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'SynchroniserPartHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6013.CouplingHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6053
            
            return self._parent._cast(_6053.MountableComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def component_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6000
            
            return self._parent._cast(_6000.ComponentHarmonicAnalysisOfSingleExcitation)

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
        def synchroniser_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6089
            
            return self._parent._cast(_6089.SynchroniserHalfHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6092
            
            return self._parent._cast(_6092.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation)

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(self) -> 'SynchroniserPartHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserPartHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2584.SynchroniserPart':
        """SynchroniserPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation':
        return self._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation(self)
