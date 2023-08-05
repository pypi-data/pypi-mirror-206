"""_5722.py

GearHarmonicAnalysis
"""
from mastapy.system_model.part_model.gears import _2509
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2740
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5753
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'GearHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearHarmonicAnalysis',)


class GearHarmonicAnalysis(_5753.MountableComponentHarmonicAnalysis):
    """GearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_HARMONIC_ANALYSIS

    class _Cast_GearHarmonicAnalysis:
        """Special nested class for casting GearHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'GearHarmonicAnalysis'):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(self):
            return self._parent._cast(_5753.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5675
            
            return self._parent._cast(_5675.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5755
            
            return self._parent._cast(_5755.PartHarmonicAnalysis)

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
        def agma_gleason_conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5653
            
            return self._parent._cast(_5653.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5660
            
            return self._parent._cast(_5660.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5663
            
            return self._parent._cast(_5663.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5664
            
            return self._parent._cast(_5664.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5665
            
            return self._parent._cast(_5665.BevelGearHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5679
            
            return self._parent._cast(_5679.ConceptGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5682
            
            return self._parent._cast(_5682.ConicalGearHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5697
            
            return self._parent._cast(_5697.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5700
            
            return self._parent._cast(_5700.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5716
            
            return self._parent._cast(_5716.FaceGearHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5738
            
            return self._parent._cast(_5738.HypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5742
            
            return self._parent._cast(_5742.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5745
            
            return self._parent._cast(_5745.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5748
            
            return self._parent._cast(_5748.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5779
            
            return self._parent._cast(_5779.SpiralBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5786
            
            return self._parent._cast(_5786.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5789
            
            return self._parent._cast(_5789.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5792
            
            return self._parent._cast(_5792.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5793
            
            return self._parent._cast(_5793.StraightBevelSunGearHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5805
            
            return self._parent._cast(_5805.WormGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5808
            
            return self._parent._cast(_5808.ZerolBevelGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(self) -> 'GearHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearHarmonicAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2740.GearSystemDeflection':
        """GearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearHarmonicAnalysis._Cast_GearHarmonicAnalysis':
        return self._Cast_GearHarmonicAnalysis(self)
