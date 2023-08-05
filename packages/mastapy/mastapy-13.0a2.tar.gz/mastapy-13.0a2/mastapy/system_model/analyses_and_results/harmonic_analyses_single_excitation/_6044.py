"""_6044.py

KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
"""
from mastapy.system_model.part_model.gears import _2516
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6009
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation',)


class KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation(_6009.ConicalGearSetHarmonicAnalysisOfSingleExcitation):
    """KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6009.ConicalGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6035
            
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
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6047
            
            return self._parent._cast(_6047.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6050
            
            return self._parent._cast(_6050.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(self) -> 'KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2516.KlingelnbergCycloPalloidConicalGearSet':
        """KlingelnbergCycloPalloidConicalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation':
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation(self)
