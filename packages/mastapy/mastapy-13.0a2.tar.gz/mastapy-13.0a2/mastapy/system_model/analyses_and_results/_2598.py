"""_2598.py

CompoundAnalysis
"""
from typing import Iterable

from mastapy._internal import constructor, conversion
from mastapy import _7521, _7515
from mastapy.system_model import _2188
from mastapy.system_model.analyses_and_results.analysis_cases import _7505
from mastapy._internal.python_net import python_net_import
from mastapy._internal.cast_exception import CastException

_TASK_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'TaskProgress')
_COMPOUND_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundAnalysis',)


class CompoundAnalysis(_7515.MarshalByRefObjectPermanent):
    """CompoundAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_ANALYSIS

    class _Cast_CompoundAnalysis:
        """Special nested class for casting CompoundAnalysis to subclasses."""

        def __init__(self, parent: 'CompoundAnalysis'):
            self._parent = parent

        @property
        def marshal_by_ref_object_permanent(self):
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def compound_advanced_system_deflection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2637
            
            return self._parent._cast(_2637.CompoundAdvancedSystemDeflectionAnalysis)

        @property
        def compound_advanced_system_deflection_sub_analysis(self):
            from mastapy.system_model.analyses_and_results import _2638
            
            return self._parent._cast(_2638.CompoundAdvancedSystemDeflectionSubAnalysis)

        @property
        def compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results import _2639
            
            return self._parent._cast(_2639.CompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results import _2640
            
            return self._parent._cast(_2640.CompoundCriticalSpeedAnalysis)

        @property
        def compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results import _2641
            
            return self._parent._cast(_2641.CompoundDynamicAnalysis)

        @property
        def compound_dynamic_model_at_a_stiffness_analysis(self):
            from mastapy.system_model.analyses_and_results import _2642
            
            return self._parent._cast(_2642.CompoundDynamicModelAtAStiffnessAnalysis)

        @property
        def compound_dynamic_model_for_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results import _2643
            
            return self._parent._cast(_2643.CompoundDynamicModelForHarmonicAnalysis)

        @property
        def compound_dynamic_model_for_modal_analysis(self):
            from mastapy.system_model.analyses_and_results import _2644
            
            return self._parent._cast(_2644.CompoundDynamicModelForModalAnalysis)

        @property
        def compound_dynamic_model_for_stability_analysis(self):
            from mastapy.system_model.analyses_and_results import _2645
            
            return self._parent._cast(_2645.CompoundDynamicModelForStabilityAnalysis)

        @property
        def compound_dynamic_model_for_steady_state_synchronous_response_analysis(self):
            from mastapy.system_model.analyses_and_results import _2646
            
            return self._parent._cast(_2646.CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis)

        @property
        def compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results import _2647
            
            return self._parent._cast(_2647.CompoundHarmonicAnalysis)

        @property
        def compound_harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results import _2648
            
            return self._parent._cast(_2648.CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation)

        @property
        def compound_harmonic_analysis_of_single_excitation_analysis(self):
            from mastapy.system_model.analyses_and_results import _2649
            
            return self._parent._cast(_2649.CompoundHarmonicAnalysisOfSingleExcitationAnalysis)

        @property
        def compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results import _2650
            
            return self._parent._cast(_2650.CompoundModalAnalysis)

        @property
        def compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results import _2651
            
            return self._parent._cast(_2651.CompoundModalAnalysisAtASpeed)

        @property
        def compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results import _2652
            
            return self._parent._cast(_2652.CompoundModalAnalysisAtAStiffness)

        @property
        def compound_modal_analysis_for_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results import _2653
            
            return self._parent._cast(_2653.CompoundModalAnalysisForHarmonicAnalysis)

        @property
        def compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results import _2654
            
            return self._parent._cast(_2654.CompoundMultibodyDynamicsAnalysis)

        @property
        def compound_power_flow_analysis(self):
            from mastapy.system_model.analyses_and_results import _2655
            
            return self._parent._cast(_2655.CompoundPowerFlowAnalysis)

        @property
        def compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results import _2656
            
            return self._parent._cast(_2656.CompoundStabilityAnalysis)

        @property
        def compound_steady_state_synchronous_response_analysis(self):
            from mastapy.system_model.analyses_and_results import _2657
            
            return self._parent._cast(_2657.CompoundSteadyStateSynchronousResponseAnalysis)

        @property
        def compound_steady_state_synchronous_response_at_a_speed_analysis(self):
            from mastapy.system_model.analyses_and_results import _2658
            
            return self._parent._cast(_2658.CompoundSteadyStateSynchronousResponseAtASpeedAnalysis)

        @property
        def compound_steady_state_synchronous_response_on_a_shaft_analysis(self):
            from mastapy.system_model.analyses_and_results import _2659
            
            return self._parent._cast(_2659.CompoundSteadyStateSynchronousResponseOnAShaftAnalysis)

        @property
        def compound_system_deflection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2660
            
            return self._parent._cast(_2660.CompoundSystemDeflectionAnalysis)

        @property
        def compound_torsional_system_deflection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2661
            
            return self._parent._cast(_2661.CompoundTorsionalSystemDeflectionAnalysis)

        @property
        def compound_analysis(self) -> 'CompoundAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CompoundAnalysis.TYPE'):
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

    def perform_analysis_with_progress(self, progress: '_7521.TaskProgress'):
        """ 'PerformAnalysis' is the original name of this method.

        Args:
            progress (mastapy.TaskProgress)
        """

        self.wrapped.PerformAnalysis.Overloads[_TASK_PROGRESS](progress.wrapped if progress else None)

    def results_for(self, design_entity: '_2188.DesignEntity') -> 'Iterable[_7505.DesignEntityCompoundAnalysis]':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.DesignEntity)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.analysis_cases.DesignEntityCompoundAnalysis]
        """

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None))

    @property
    def cast_to(self) -> 'CompoundAnalysis._Cast_CompoundAnalysis':
        return self._Cast_CompoundAnalysis(self)
