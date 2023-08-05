"""_5797.py

SynchroniserSleeveHarmonicAnalysis
"""
from mastapy.system_model.part_model.couplings import _2585
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6934
from mastapy.system_model.analyses_and_results.system_deflections import _2802
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5796
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'SynchroniserSleeveHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserSleeveHarmonicAnalysis',)


class SynchroniserSleeveHarmonicAnalysis(_5796.SynchroniserPartHarmonicAnalysis):
    """SynchroniserSleeveHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_HARMONIC_ANALYSIS

    class _Cast_SynchroniserSleeveHarmonicAnalysis:
        """Special nested class for casting SynchroniserSleeveHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'SynchroniserSleeveHarmonicAnalysis'):
            self._parent = parent

        @property
        def synchroniser_part_harmonic_analysis(self):
            return self._parent._cast(_5796.SynchroniserPartHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5688
            
            return self._parent._cast(_5688.CouplingHalfHarmonicAnalysis)

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
        def synchroniser_sleeve_harmonic_analysis(self) -> 'SynchroniserSleeveHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserSleeveHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2585.SynchroniserSleeve':
        """SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6934.SynchroniserSleeveLoadCase':
        """SynchroniserSleeveLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2802.SynchroniserSleeveSystemDeflection':
        """SynchroniserSleeveSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SynchroniserSleeveHarmonicAnalysis._Cast_SynchroniserSleeveHarmonicAnalysis':
        return self._Cast_SynchroniserSleeveHarmonicAnalysis(self)
