"""_6016.py

CVTHarmonicAnalysisOfSingleExcitation
"""
from mastapy.system_model.part_model.couplings import _2565
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5985
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'CVTHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTHarmonicAnalysisOfSingleExcitation',)


class CVTHarmonicAnalysisOfSingleExcitation(_5985.BeltDriveHarmonicAnalysisOfSingleExcitation):
    """CVTHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CVT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_CVTHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CVTHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'CVTHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_5985.BeltDriveHarmonicAnalysisOfSingleExcitation)

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
        def cvt_harmonic_analysis_of_single_excitation(self) -> 'CVTHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2565.CVT':
        """CVT: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation':
        return self._Cast_CVTHarmonicAnalysisOfSingleExcitation(self)
