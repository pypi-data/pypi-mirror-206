"""_7506.py

FEAnalysis
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'FEAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FEAnalysis',)


class FEAnalysis(_7512.StaticLoadAnalysisCase):
    """FEAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_ANALYSIS

    class _Cast_FEAnalysis:
        """Special nested class for casting FEAnalysis to subclasses."""

        def __init__(self, parent: 'FEAnalysis'):
            self._parent = parent

        @property
        def static_load_analysis_case(self):
            return self._parent._cast(_7512.StaticLoadAnalysisCase)

        @property
        def analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7497
            
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
        def dynamic_model_for_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _2609
            
            return self._parent._cast(_2609.DynamicModelForStabilityAnalysis)

        @property
        def dynamic_model_for_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _2608
            
            return self._parent._cast(_2608.DynamicModelForModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4882
            
            return self._parent._cast(_4882.DynamicModelAtAStiffness)

        @property
        def dynamic_model_for_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _2607
            
            return self._parent._cast(_2607.DynamicModelForHarmonicAnalysis)

        @property
        def dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _2605
            
            return self._parent._cast(_2605.DynamicAnalysis)

        @property
        def advanced_system_deflection_sub_analysis(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7238
            
            return self._parent._cast(_7238.AdvancedSystemDeflectionSubAnalysis)

        @property
        def fe_analysis(self) -> 'FEAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stiffness_with_respect_to_input_power_load(self) -> 'float':
        """float: 'StiffnessWithRespectToInputPowerLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessWithRespectToInputPowerLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_at_zero_displacement_for_input_power_load(self) -> 'float':
        """float: 'TorqueAtZeroDisplacementForInputPowerLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueAtZeroDisplacementForInputPowerLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ratio_to_output(self) -> 'float':
        """float: 'TorqueRatioToOutput' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueRatioToOutput

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'FEAnalysis._Cast_FEAnalysis':
        return self._Cast_FEAnalysis(self)
