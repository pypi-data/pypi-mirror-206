"""_6239.py

FlexiblePinAnalysisManufactureLevel
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4318
from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS_MANUFACTURE_LEVEL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses', 'FlexiblePinAnalysisManufactureLevel')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAnalysisManufactureLevel',)


class FlexiblePinAnalysisManufactureLevel(_6235.FlexiblePinAnalysis):
    """FlexiblePinAnalysisManufactureLevel

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS_MANUFACTURE_LEVEL

    class _Cast_FlexiblePinAnalysisManufactureLevel:
        """Special nested class for casting FlexiblePinAnalysisManufactureLevel to subclasses."""

        def __init__(self, parent: 'FlexiblePinAnalysisManufactureLevel'):
            self._parent = parent

        @property
        def flexible_pin_analysis(self):
            return self._parent._cast(_6235.FlexiblePinAnalysis)

        @property
        def combination_analysis(self):
            from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6234
            
            return self._parent._cast(_6234.CombinationAnalysis)

        @property
        def flexible_pin_analysis_manufacture_level(self) -> 'FlexiblePinAnalysisManufactureLevel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlexiblePinAnalysisManufactureLevel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_sharing_factors(self) -> 'List[float]':
        """List[float]: 'LoadSharingFactors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadSharingFactors

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def planetary_mesh_analysis(self) -> '_4318.CylindricalGearMeshParametricStudyTool':
        """CylindricalGearMeshParametricStudyTool: 'PlanetaryMeshAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetaryMeshAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'FlexiblePinAnalysisManufactureLevel._Cast_FlexiblePinAnalysisManufactureLevel':
        return self._Cast_FlexiblePinAnalysisManufactureLevel(self)
