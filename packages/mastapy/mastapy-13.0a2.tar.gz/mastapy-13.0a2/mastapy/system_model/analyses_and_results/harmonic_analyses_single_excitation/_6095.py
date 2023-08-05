"""_6095.py

TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
"""
from mastapy.system_model.part_model.couplings import _2587
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6938
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6013
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'TorqueConverterPumpHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpHarmonicAnalysisOfSingleExcitation',)


class TorqueConverterPumpHarmonicAnalysisOfSingleExcitation(_6013.CouplingHalfHarmonicAnalysisOfSingleExcitation):
    """TorqueConverterPumpHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting TorqueConverterPumpHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'TorqueConverterPumpHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(self):
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
        def torque_converter_pump_harmonic_analysis_of_single_excitation(self) -> 'TorqueConverterPumpHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2587.TorqueConverterPump':
        """TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6938.TorqueConverterPumpLoadCase':
        """TorqueConverterPumpLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation':
        return self._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation(self)
