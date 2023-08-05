"""_6238.py

FlexiblePinAnalysisGearAndBearingRating
"""
from typing import List

from mastapy.system_model.analyses_and_results.system_deflections.compound import _2879, _2838
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS_GEAR_AND_BEARING_RATING = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses', 'FlexiblePinAnalysisGearAndBearingRating')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAnalysisGearAndBearingRating',)


class FlexiblePinAnalysisGearAndBearingRating(_6235.FlexiblePinAnalysis):
    """FlexiblePinAnalysisGearAndBearingRating

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS_GEAR_AND_BEARING_RATING

    class _Cast_FlexiblePinAnalysisGearAndBearingRating:
        """Special nested class for casting FlexiblePinAnalysisGearAndBearingRating to subclasses."""

        def __init__(self, parent: 'FlexiblePinAnalysisGearAndBearingRating'):
            self._parent = parent

        @property
        def flexible_pin_analysis(self):
            return self._parent._cast(_6235.FlexiblePinAnalysis)

        @property
        def combination_analysis(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6234
            
            return self._parent._cast(_6234.CombinationAnalysis)

        @property
        def flexible_pin_analysis_gear_and_bearing_rating(self) -> 'FlexiblePinAnalysisGearAndBearingRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlexiblePinAnalysisGearAndBearingRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_analysis(self) -> '_2879.CylindricalGearSetCompoundSystemDeflection':
        """CylindricalGearSetCompoundSystemDeflection: 'GearSetAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_analyses(self) -> 'List[_2838.BearingCompoundSystemDeflection]':
        """List[BearingCompoundSystemDeflection]: 'BearingAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FlexiblePinAnalysisGearAndBearingRating._Cast_FlexiblePinAnalysisGearAndBearingRating':
        return self._Cast_FlexiblePinAnalysisGearAndBearingRating(self)
