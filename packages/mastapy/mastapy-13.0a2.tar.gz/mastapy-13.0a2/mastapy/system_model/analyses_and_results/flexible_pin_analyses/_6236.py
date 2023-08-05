"""_6236.py

FlexiblePinAnalysisConceptLevel
"""
from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2737, _2677
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS_CONCEPT_LEVEL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses', 'FlexiblePinAnalysisConceptLevel')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAnalysisConceptLevel',)


class FlexiblePinAnalysisConceptLevel(_6235.FlexiblePinAnalysis):
    """FlexiblePinAnalysisConceptLevel

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS_CONCEPT_LEVEL

    class _Cast_FlexiblePinAnalysisConceptLevel:
        """Special nested class for casting FlexiblePinAnalysisConceptLevel to subclasses."""

        def __init__(self, parent: 'FlexiblePinAnalysisConceptLevel'):
            self._parent = parent

        @property
        def flexible_pin_analysis(self):
            return self._parent._cast(_6235.FlexiblePinAnalysis)

        @property
        def combination_analysis(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6234
            
            return self._parent._cast(_6234.CombinationAnalysis)

        @property
        def flexible_pin_analysis_concept_level(self) -> 'FlexiblePinAnalysisConceptLevel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlexiblePinAnalysisConceptLevel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flexible_pin_extreme_load_case(self) -> '_2737.FlexiblePinAssemblySystemDeflection':
        """FlexiblePinAssemblySystemDeflection: 'FlexiblePinExtremeLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinExtremeLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def flexible_pin_nominal_load_case(self) -> '_2737.FlexiblePinAssemblySystemDeflection':
        """FlexiblePinAssemblySystemDeflection: 'FlexiblePinNominalLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinNominalLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planet_bearings_in_nominal_load(self) -> 'List[_2677.BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'PlanetBearingsInNominalLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetBearingsInNominalLoad

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FlexiblePinAnalysisConceptLevel._Cast_FlexiblePinAnalysisConceptLevel':
        return self._Cast_FlexiblePinAnalysisConceptLevel(self)
