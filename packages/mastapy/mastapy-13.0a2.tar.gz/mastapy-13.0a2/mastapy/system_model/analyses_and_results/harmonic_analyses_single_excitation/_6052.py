"""_6052.py

MeasurementComponentHarmonicAnalysisOfSingleExcitation
"""
from mastapy.system_model.part_model import _2443
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6886
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6098
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'MeasurementComponentHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentHarmonicAnalysisOfSingleExcitation',)


class MeasurementComponentHarmonicAnalysisOfSingleExcitation(_6098.VirtualComponentHarmonicAnalysisOfSingleExcitation):
    """MeasurementComponentHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting MeasurementComponentHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'MeasurementComponentHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6098.VirtualComponentHarmonicAnalysisOfSingleExcitation)

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
        def measurement_component_harmonic_analysis_of_single_excitation(self) -> 'MeasurementComponentHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeasurementComponentHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2443.MeasurementComponent':
        """MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6886.MeasurementComponentLoadCase':
        """MeasurementComponentLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MeasurementComponentHarmonicAnalysisOfSingleExcitation._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation':
        return self._Cast_MeasurementComponentHarmonicAnalysisOfSingleExcitation(self)
