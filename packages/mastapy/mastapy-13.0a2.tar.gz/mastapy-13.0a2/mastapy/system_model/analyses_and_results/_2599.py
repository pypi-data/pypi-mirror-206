"""_2599.py

SingleAnalysis
"""
from mastapy._internal import constructor
from mastapy import _7521, _7515
from mastapy.system_model import _2188
from mastapy.system_model.analyses_and_results import _2630
from mastapy._internal.python_net import python_net_import
from mastapy._internal.cast_exception import CastException

_TASK_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'TaskProgress')
_DESIGN_ENTITY = python_net_import('SMT.MastaAPI.SystemModel', 'DesignEntity')
_DESIGN_ENTITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'DesignEntityAnalysis')
_SINGLE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'SingleAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SingleAnalysis',)


class SingleAnalysis(_7515.MarshalByRefObjectPermanent):
    """SingleAnalysis

    This is a mastapy class.
    """

    TYPE = _SINGLE_ANALYSIS

    class _Cast_SingleAnalysis:
        """Special nested class for casting SingleAnalysis to subclasses."""

        def __init__(self, parent: 'SingleAnalysis'):
            self._parent = parent

        @property
        def marshal_by_ref_object_permanent(self):
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def advanced_system_deflection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2600
            
            return self._parent._cast(_2600.AdvancedSystemDeflectionAnalysis)

        @property
        def advanced_system_deflection_sub_analysis(self):
            from mastapy.system_model.analyses_and_results import _2601
            
            return self._parent._cast(_2601.AdvancedSystemDeflectionSubAnalysis)

        @property
        def advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results import _2602
            
            return self._parent._cast(_2602.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def compound_parametric_study_tool_analysis(self):
            from mastapy.system_model.analyses_and_results import _2603
            
            return self._parent._cast(_2603.CompoundParametricStudyToolAnalysis)

        @property
        def critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results import _2604
            
            return self._parent._cast(_2604.CriticalSpeedAnalysis)

        @property
        def dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results import _2605
            
            return self._parent._cast(_2605.DynamicAnalysis)

        @property
        def dynamic_model_at_a_stiffness_analysis(self):
            from mastapy.system_model.analyses_and_results import _2606
            
            return self._parent._cast(_2606.DynamicModelAtAStiffnessAnalysis)

        @property
        def dynamic_model_for_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results import _2607
            
            return self._parent._cast(_2607.DynamicModelForHarmonicAnalysis)

        @property
        def dynamic_model_for_modal_analysis(self):
            from mastapy.system_model.analyses_and_results import _2608
            
            return self._parent._cast(_2608.DynamicModelForModalAnalysis)

        @property
        def dynamic_model_for_stability_analysis(self):
            from mastapy.system_model.analyses_and_results import _2609
            
            return self._parent._cast(_2609.DynamicModelForStabilityAnalysis)

        @property
        def dynamic_model_for_steady_state_synchronous_response_analysis(self):
            from mastapy.system_model.analyses_and_results import _2610
            
            return self._parent._cast(_2610.DynamicModelForSteadyStateSynchronousResponseAnalysis)

        @property
        def harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results import _2611
            
            return self._parent._cast(_2611.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results import _2612
            
            return self._parent._cast(_2612.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation)

        @property
        def harmonic_analysis_of_single_excitation_analysis(self):
            from mastapy.system_model.analyses_and_results import _2613
            
            return self._parent._cast(_2613.HarmonicAnalysisOfSingleExcitationAnalysis)

        @property
        def modal_analysis(self):
            from mastapy.system_model.analyses_and_results import _2614
            
            return self._parent._cast(_2614.ModalAnalysis)

        @property
        def modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results import _2615
            
            return self._parent._cast(_2615.ModalAnalysisAtASpeed)

        @property
        def modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results import _2616
            
            return self._parent._cast(_2616.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_for_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results import _2617
            
            return self._parent._cast(_2617.ModalAnalysisForHarmonicAnalysis)

        @property
        def multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results import _2618
            
            return self._parent._cast(_2618.MultibodyDynamicsAnalysis)

        @property
        def parametric_study_tool_analysis(self):
            from mastapy.system_model.analyses_and_results import _2619
            
            return self._parent._cast(_2619.ParametricStudyToolAnalysis)

        @property
        def power_flow_analysis(self):
            from mastapy.system_model.analyses_and_results import _2620
            
            return self._parent._cast(_2620.PowerFlowAnalysis)

        @property
        def stability_analysis(self):
            from mastapy.system_model.analyses_and_results import _2621
            
            return self._parent._cast(_2621.StabilityAnalysis)

        @property
        def steady_state_synchronous_response_analysis(self):
            from mastapy.system_model.analyses_and_results import _2622
            
            return self._parent._cast(_2622.SteadyStateSynchronousResponseAnalysis)

        @property
        def steady_state_synchronous_response_at_a_speed_analysis(self):
            from mastapy.system_model.analyses_and_results import _2623
            
            return self._parent._cast(_2623.SteadyStateSynchronousResponseAtASpeedAnalysis)

        @property
        def steady_state_synchronous_response_on_a_shaft_analysis(self):
            from mastapy.system_model.analyses_and_results import _2624
            
            return self._parent._cast(_2624.SteadyStateSynchronousResponseOnAShaftAnalysis)

        @property
        def system_deflection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2625
            
            return self._parent._cast(_2625.SystemDeflectionAnalysis)

        @property
        def torsional_system_deflection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2626
            
            return self._parent._cast(_2626.TorsionalSystemDeflectionAnalysis)

        @property
        def single_analysis(self) -> 'SingleAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SingleAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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

    def perform_analysis(self):
        """ 'PerformAnalysis' is the original name of this method."""

        self.wrapped.PerformAnalysis()

    def perform_analysis_with_progress(self, task_progress: '_7521.TaskProgress'):
        """ 'PerformAnalysis' is the original name of this method.

        Args:
            task_progress (mastapy.TaskProgress)
        """

        self.wrapped.PerformAnalysis.Overloads[_TASK_PROGRESS](task_progress.wrapped if task_progress else None)

    def results_for(self, design_entity: '_2188.DesignEntity') -> '_2630.DesignEntityAnalysis':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.DesignEntity)

        Returns:
            mastapy.system_model.analyses_and_results.DesignEntityAnalysis
        """

        method_result = self.wrapped.ResultsFor.Overloads[_DESIGN_ENTITY](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def results_for_design_entity_analysis(self, design_entity_analysis: '_2630.DesignEntityAnalysis') -> '_2630.DesignEntityAnalysis':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.DesignEntityAnalysis)

        Returns:
            mastapy.system_model.analyses_and_results.DesignEntityAnalysis
        """

        method_result = self.wrapped.ResultsFor.Overloads[_DESIGN_ENTITY_ANALYSIS](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'SingleAnalysis._Cast_SingleAnalysis':
        return self._Cast_SingleAnalysis(self)
