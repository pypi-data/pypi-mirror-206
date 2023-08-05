"""_6235.py

FlexiblePinAnalysis
"""
from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6240, _6234
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses', 'FlexiblePinAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAnalysis',)


class FlexiblePinAnalysis(_6234.CombinationAnalysis):
    """FlexiblePinAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS

    class _Cast_FlexiblePinAnalysis:
        """Special nested class for casting FlexiblePinAnalysis to subclasses."""

        def __init__(self, parent: 'FlexiblePinAnalysis'):
            self._parent = parent

        @property
        def combination_analysis(self):
            return self._parent._cast(_6234.CombinationAnalysis)

        @property
        def flexible_pin_analysis_concept_level(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6236
            
            return self._parent._cast(_6236.FlexiblePinAnalysisConceptLevel)

        @property
        def flexible_pin_analysis_detail_level_and_pin_fatigue_one_tooth_pass(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6237
            
            return self._parent._cast(_6237.FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass)

        @property
        def flexible_pin_analysis_gear_and_bearing_rating(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6238
            
            return self._parent._cast(_6238.FlexiblePinAnalysisGearAndBearingRating)

        @property
        def flexible_pin_analysis_manufacture_level(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6239
            
            return self._parent._cast(_6239.FlexiblePinAnalysisManufactureLevel)

        @property
        def flexible_pin_analysis_stop_start_analysis(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6241
            
            return self._parent._cast(_6241.FlexiblePinAnalysisStopStartAnalysis)

        @property
        def flexible_pin_analysis(self) -> 'FlexiblePinAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlexiblePinAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_options(self) -> '_6240.FlexiblePinAnalysisOptions':
        """FlexiblePinAnalysisOptions: 'AnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'FlexiblePinAnalysis._Cast_FlexiblePinAnalysis':
        return self._Cast_FlexiblePinAnalysis(self)
