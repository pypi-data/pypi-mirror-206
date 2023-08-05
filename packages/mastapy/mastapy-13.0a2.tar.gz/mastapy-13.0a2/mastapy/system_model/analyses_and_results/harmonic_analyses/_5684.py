"""_5684.py

ConicalGearSetHarmonicAnalysis
"""
from mastapy.system_model.part_model.gears import _2503
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2704
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5727
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ConicalGearSetHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetHarmonicAnalysis',)


class ConicalGearSetHarmonicAnalysis(_5727.GearSetHarmonicAnalysis):
    """ConicalGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_HARMONIC_ANALYSIS

    class _Cast_ConicalGearSetHarmonicAnalysis:
        """Special nested class for casting ConicalGearSetHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearSetHarmonicAnalysis'):
            self._parent = parent

        @property
        def gear_set_harmonic_analysis(self):
            return self._parent._cast(_5727.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5777
            
            return self._parent._cast(_5777.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5648
            
            return self._parent._cast(_5648.AbstractAssemblyHarmonicAnalysis)

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
        def agma_gleason_conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5655
            
            return self._parent._cast(_5655.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5662
            
            return self._parent._cast(_5662.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5667
            
            return self._parent._cast(_5667.BevelGearSetHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5740
            
            return self._parent._cast(_5740.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5744
            
            return self._parent._cast(_5744.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5747
            
            return self._parent._cast(_5747.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5750
            
            return self._parent._cast(_5750.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5781
            
            return self._parent._cast(_5781.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5788
            
            return self._parent._cast(_5788.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5791
            
            return self._parent._cast(_5791.StraightBevelGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5810
            
            return self._parent._cast(_5810.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(self) -> 'ConicalGearSetHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSetHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2503.ConicalGearSet':
        """ConicalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2704.ConicalGearSetSystemDeflection':
        """ConicalGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis':
        return self._Cast_ConicalGearSetHarmonicAnalysis(self)
