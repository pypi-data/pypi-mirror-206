"""_5985.py

BeltDriveHarmonicAnalysisOfSingleExcitation
"""
from mastapy.system_model.part_model.couplings import _2555
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6786
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6074
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'BeltDriveHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveHarmonicAnalysisOfSingleExcitation',)


class BeltDriveHarmonicAnalysisOfSingleExcitation(_6074.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation):
    """BeltDriveHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_BeltDriveHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BeltDriveHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'BeltDriveHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(self):
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
        def cvt_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6016
            
            return self._parent._cast(_6016.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(self) -> 'BeltDriveHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltDriveHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2555.BeltDrive':
        """BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6786.BeltDriveLoadCase':
        """BeltDriveLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BeltDriveHarmonicAnalysisOfSingleExcitation._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation':
        return self._Cast_BeltDriveHarmonicAnalysisOfSingleExcitation(self)
