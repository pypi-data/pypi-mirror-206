"""_7497.py

AnalysisCase
"""
from mastapy._internal import constructor
from mastapy.utility import _1567
from mastapy.system_model import _2188
from mastapy.system_model.analyses_and_results import _2630, _2629
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'AnalysisCase')


__docformat__ = 'restructuredtext en'
__all__ = ('AnalysisCase',)


class AnalysisCase(_2629.Context):
    """AnalysisCase

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_CASE

    class _Cast_AnalysisCase:
        """Special nested class for casting AnalysisCase to subclasses."""

        def __init__(self, parent: 'AnalysisCase'):
            self._parent = parent

        @property
        def context(self):
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
        def parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4363
            
            return self._parent._cast(_4363.ParametricStudyTool)

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
        def multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _2618
            
            return self._parent._cast(_2618.MultibodyDynamicsAnalysis)

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
        def static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
            return self._parent._cast(_7512.StaticLoadAnalysisCase)

        @property
        def time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7513
            
            return self._parent._cast(_7513.TimeSeriesLoadAnalysisCase)

        @property
        def analysis_case(self) -> 'AnalysisCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AnalysisCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_setup_time(self) -> 'float':
        """float: 'AnalysisSetupTime' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisSetupTime

        if temp is None:
            return 0.0

        return temp

    @property
    def load_case_name(self) -> 'str':
        """str: 'LoadCaseName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCaseName

        if temp is None:
            return ''

        return temp

    @property
    def analysis_run_information(self) -> '_1567.AnalysisRunInformation':
        """AnalysisRunInformation: 'AnalysisRunInformation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisRunInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results_ready(self) -> 'bool':
        """bool: 'ResultsReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsReady

        if temp is None:
            return False

        return temp

    def results_for(self, design_entity: '_2188.DesignEntity') -> '_2630.DesignEntityAnalysis':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.DesignEntity)

        Returns:
            mastapy.system_model.analyses_and_results.DesignEntityAnalysis
        """

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def perform_analysis(self):
        """ 'PerformAnalysis' is the original name of this method."""

        self.wrapped.PerformAnalysis()

    @property
    def cast_to(self) -> 'AnalysisCase._Cast_AnalysisCase':
        return self._Cast_AnalysisCase(self)
