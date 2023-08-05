"""_6237.py

FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass
"""
from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS_DETAIL_LEVEL_AND_PIN_FATIGUE_ONE_TOOTH_PASS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses', 'FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass',)


class FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass(_6235.FlexiblePinAnalysis):
    """FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS_DETAIL_LEVEL_AND_PIN_FATIGUE_ONE_TOOTH_PASS

    class _Cast_FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass:
        """Special nested class for casting FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass to subclasses."""

        def __init__(self, parent: 'FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass'):
            self._parent = parent

        @property
        def flexible_pin_analysis(self):
            return self._parent._cast(_6235.FlexiblePinAnalysis)

        @property
        def combination_analysis(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6234
            
            return self._parent._cast(_6234.CombinationAnalysis)

        @property
        def flexible_pin_analysis_detail_level_and_pin_fatigue_one_tooth_pass(self) -> 'FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass._Cast_FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass':
        return self._Cast_FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass(self)
