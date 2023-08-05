"""_6017.py

CVTPulleyHarmonicAnalysisOfSingleExcitation
"""
from mastapy.system_model.part_model.couplings import _2566
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6064
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'CVTPulleyHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleyHarmonicAnalysisOfSingleExcitation',)


class CVTPulleyHarmonicAnalysisOfSingleExcitation(_6064.PulleyHarmonicAnalysisOfSingleExcitation):
    """CVTPulleyHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CVTPulleyHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'CVTPulleyHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def pulley_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6064.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6013
            
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
        def cvt_pulley_harmonic_analysis_of_single_excitation(self) -> 'CVTPulleyHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTPulleyHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2566.CVTPulley':
        """CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CVTPulleyHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation':
        return self._Cast_CVTPulleyHarmonicAnalysisOfSingleExcitation(self)
