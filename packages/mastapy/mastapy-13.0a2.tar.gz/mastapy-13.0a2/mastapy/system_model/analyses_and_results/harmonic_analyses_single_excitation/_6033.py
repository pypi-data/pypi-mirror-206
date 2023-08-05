"""_6033.py

GearHarmonicAnalysisOfSingleExcitation
"""
from mastapy.system_model.part_model.gears import _2509
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6053
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'GearHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('GearHarmonicAnalysisOfSingleExcitation',)


class GearHarmonicAnalysisOfSingleExcitation(_6053.MountableComponentHarmonicAnalysisOfSingleExcitation):
    """GearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_GearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'GearHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(self):
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
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5979
            
            return self._parent._cast(_5979.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5986
            
            return self._parent._cast(_5986.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5989
            
            return self._parent._cast(_5989.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5990
            
            return self._parent._cast(_5990.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5991
            
            return self._parent._cast(_5991.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6004
            
            return self._parent._cast(_6004.ConceptGearHarmonicAnalysisOfSingleExcitation)

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6007
            
            return self._parent._cast(_6007.ConicalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6022
            
            return self._parent._cast(_6022.CylindricalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6025
            
            return self._parent._cast(_6025.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6028
            
            return self._parent._cast(_6028.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6038
            
            return self._parent._cast(_6038.HypoidGearHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6042
            
            return self._parent._cast(_6042.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6045
            
            return self._parent._cast(_6045.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6048
            
            return self._parent._cast(_6048.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6075
            
            return self._parent._cast(_6075.SpiralBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6081
            
            return self._parent._cast(_6081.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6084
            
            return self._parent._cast(_6084.StraightBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6087
            
            return self._parent._cast(_6087.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation)

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6088
            
            return self._parent._cast(_6088.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6099
            
            return self._parent._cast(_6099.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6102
            
            return self._parent._cast(_6102.ZerolBevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_harmonic_analysis_of_single_excitation(self) -> 'GearHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2509.Gear':
        """Gear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation':
        return self._Cast_GearHarmonicAnalysisOfSingleExcitation(self)
