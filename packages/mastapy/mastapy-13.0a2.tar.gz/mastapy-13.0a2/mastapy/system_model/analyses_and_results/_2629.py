"""_2629.py

Context
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.utility import _1572
from mastapy.system_model import _2185
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONTEXT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'Context')


__docformat__ = 'restructuredtext en'
__all__ = ('Context',)


class Context(_0.APIBase):
    """Context

    This is a mastapy class.
    """

    TYPE = _CONTEXT

    class _Cast_Context:
        """Special nested class for casting Context to subclasses."""

        def __init__(self, parent: 'Context'):
            self._parent = parent

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
        def parametric_study_static_load(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4362
            
            return self._parent._cast(_4362.ParametricStudyStaticLoad)

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
        def harmonic_analysis_with_varying_stiffness_static_load_case(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5737
            
            return self._parent._cast(_5737.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase)

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
        def load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6768
            
            return self._parent._cast(_6768.LoadCase)

        @property
        def static_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6769
            
            return self._parent._cast(_6769.StaticLoadCase)

        @property
        def time_series_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6770
            
            return self._parent._cast(_6770.TimeSeriesLoadCase)

        @property
        def advanced_time_stepping_analysis_for_modulation_static_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6776
            
            return self._parent._cast(_6776.AdvancedTimeSteppingAnalysisForModulationStaticLoadCase)

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
        def analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7497
            
            return self._parent._cast(_7497.AnalysisCase)

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
        def context(self) -> 'Context':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Context.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self) -> 'str':
        """str: 'Comment' is the original name of this property."""

        temp = self.wrapped.Comment

        if temp is None:
            return ''

        return temp

    @comment.setter
    def comment(self, value: 'str'):
        self.wrapped.Comment = str(value) if value else ''

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def save_history_information(self) -> '_1572.FileHistoryItem':
        """FileHistoryItem: 'SaveHistoryInformation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SaveHistoryInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_properties(self) -> '_2185.Design':
        """Design: 'DesignProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'Context._Cast_Context':
        return self._Cast_Context(self)
