"""_7512.py

StaticLoadAnalysisCase
"""
from mastapy.system_model.analyses_and_results.static_loads import _6769
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7497
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATIC_LOAD_ANALYSIS_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'StaticLoadAnalysisCase')


__docformat__ = 'restructuredtext en'
__all__ = ('StaticLoadAnalysisCase',)


class StaticLoadAnalysisCase(_7497.AnalysisCase):
    """StaticLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _STATIC_LOAD_ANALYSIS_CASE

    class _Cast_StaticLoadAnalysisCase:
        """Special nested class for casting StaticLoadAnalysisCase to subclasses."""

        def __init__(self, parent: 'StaticLoadAnalysisCase'):
            self._parent = parent

        @property
        def analysis_case(self):
            return self._parent._cast(_7497.AnalysisCase)

        @property
        def context(self):
            from mastapy.system_model.analyses_and_results import _2629
            
            return self._parent._cast(_2629.Context)

        @property
        def system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2804
            
            return self._parent._cast(_2804.SystemDeflection)

        @property
        def torsional_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2811
            
            return self._parent._cast(_2811.TorsionalSystemDeflection)

        @property
        def dynamic_model_for_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3014
            
            return self._parent._cast(_3014.DynamicModelForSteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3068
            
            return self._parent._cast(_3068.SteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3329
            
            return self._parent._cast(_3329.SteadyStateSynchronousResponseOnAShaft)

        @property
        def steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3588
            
            return self._parent._cast(_3588.SteadyStateSynchronousResponseAtASpeed)

        @property
        def dynamic_model_for_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _2609
            
            return self._parent._cast(_2609.DynamicModelForStabilityAnalysis)

        @property
        def stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _2621
            
            return self._parent._cast(_2621.StabilityAnalysis)

        @property
        def power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4097
            
            return self._parent._cast(_4097.PowerFlow)

        @property
        def dynamic_model_for_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _2608
            
            return self._parent._cast(_2608.DynamicModelForModalAnalysis)

        @property
        def modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _2614
            
            return self._parent._cast(_2614.ModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4882
            
            return self._parent._cast(_4882.DynamicModelAtAStiffness)

        @property
        def modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _2616
            
            return self._parent._cast(_2616.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _2615
            
            return self._parent._cast(_2615.ModalAnalysisAtASpeed)

        @property
        def dynamic_model_for_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _2607
            
            return self._parent._cast(_2607.DynamicModelForHarmonicAnalysis)

        @property
        def harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _2611
            
            return self._parent._cast(_2611.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _2612
            
            return self._parent._cast(_2612.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation)

        @property
        def harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6037
            
            return self._parent._cast(_6037.HarmonicAnalysisOfSingleExcitation)

        @property
        def modal_analysis_for_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _2617
            
            return self._parent._cast(_2617.ModalAnalysisForHarmonicAnalysis)

        @property
        def dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _2605
            
            return self._parent._cast(_2605.DynamicAnalysis)

        @property
        def critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _2604
            
            return self._parent._cast(_2604.CriticalSpeedAnalysis)

        @property
        def advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _2602
            
            return self._parent._cast(_2602.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7236
            
            return self._parent._cast(_7236.AdvancedSystemDeflection)

        @property
        def advanced_system_deflection_sub_analysis(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7238
            
            return self._parent._cast(_7238.AdvancedSystemDeflectionSubAnalysis)

        @property
        def compound_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7499
            
            return self._parent._cast(_7499.CompoundAnalysisCase)

        @property
        def fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7506
            
            return self._parent._cast(_7506.FEAnalysis)

        @property
        def static_load_analysis_case(self) -> 'StaticLoadAnalysisCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StaticLoadAnalysisCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_case(self) -> '_6769.StaticLoadCase':
        """StaticLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase':
        return self._Cast_StaticLoadAnalysisCase(self)
