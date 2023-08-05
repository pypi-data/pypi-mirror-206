"""_6241.py

FlexiblePinAnalysisStopStartAnalysis
"""
from mastapy.system_model.analyses_and_results.system_deflections import _2783
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS_STOP_START_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses', 'FlexiblePinAnalysisStopStartAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAnalysisStopStartAnalysis',)


class FlexiblePinAnalysisStopStartAnalysis(_6235.FlexiblePinAnalysis):
    """FlexiblePinAnalysisStopStartAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS_STOP_START_ANALYSIS

    class _Cast_FlexiblePinAnalysisStopStartAnalysis:
        """Special nested class for casting FlexiblePinAnalysisStopStartAnalysis to subclasses."""

        def __init__(self, parent: 'FlexiblePinAnalysisStopStartAnalysis'):
            self._parent = parent

        @property
        def flexible_pin_analysis(self):
            return self._parent._cast(_6235.FlexiblePinAnalysis)

        @property
        def combination_analysis(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6234
            
            return self._parent._cast(_6234.CombinationAnalysis)

        @property
        def flexible_pin_analysis_stop_start_analysis(self) -> 'FlexiblePinAnalysisStopStartAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlexiblePinAnalysisStopStartAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def shaft_extreme_load_case(self) -> '_2783.ShaftSystemDeflection':
        """ShaftSystemDeflection: 'ShaftExtremeLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftExtremeLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_nominal_load_case(self) -> '_2783.ShaftSystemDeflection':
        """ShaftSystemDeflection: 'ShaftNominalLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftNominalLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'FlexiblePinAnalysisStopStartAnalysis._Cast_FlexiblePinAnalysisStopStartAnalysis':
        return self._Cast_FlexiblePinAnalysisStopStartAnalysis(self)
