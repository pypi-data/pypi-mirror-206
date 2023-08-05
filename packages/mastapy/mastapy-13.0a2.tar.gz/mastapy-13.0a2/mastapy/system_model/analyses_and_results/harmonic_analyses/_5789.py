"""_5789.py

StraightBevelGearHarmonicAnalysis
"""
from mastapy.system_model.part_model.gears import _2526
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6926
from mastapy.system_model.analyses_and_results.system_deflections import _2797
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5665
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'StraightBevelGearHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearHarmonicAnalysis',)


class StraightBevelGearHarmonicAnalysis(_5665.BevelGearHarmonicAnalysis):
    """StraightBevelGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_HARMONIC_ANALYSIS

    class _Cast_StraightBevelGearHarmonicAnalysis:
        """Special nested class for casting StraightBevelGearHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'StraightBevelGearHarmonicAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_harmonic_analysis(self):
            return self._parent._cast(_5665.BevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5653
            
            return self._parent._cast(_5653.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5682
            
            return self._parent._cast(_5682.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5722
            
            return self._parent._cast(_5722.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5753
            
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
        def straight_bevel_gear_harmonic_analysis(self) -> 'StraightBevelGearHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2526.StraightBevelGear':
        """StraightBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6926.StraightBevelGearLoadCase':
        """StraightBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2797.StraightBevelGearSystemDeflection':
        """StraightBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis':
        return self._Cast_StraightBevelGearHarmonicAnalysis(self)
