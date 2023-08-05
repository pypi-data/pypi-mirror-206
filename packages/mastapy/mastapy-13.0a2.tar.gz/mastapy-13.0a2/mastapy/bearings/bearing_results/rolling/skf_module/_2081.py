"""_2081.py

SKFCalculationResult
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SKF_CALCULATION_RESULT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'SKFCalculationResult')


__docformat__ = 'restructuredtext en'
__all__ = ('SKFCalculationResult',)


class SKFCalculationResult(_0.APIBase):
    """SKFCalculationResult

    This is a mastapy class.
    """

    TYPE = _SKF_CALCULATION_RESULT

    class _Cast_SKFCalculationResult:
        """Special nested class for casting SKFCalculationResult to subclasses."""

        def __init__(self, parent: 'SKFCalculationResult'):
            self._parent = parent

        @property
        def adjusted_speed(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2061
            
            return self._parent._cast(_2061.AdjustedSpeed)

        @property
        def bearing_loads(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2063
            
            return self._parent._cast(_2063.BearingLoads)

        @property
        def bearing_rating_life(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2064
            
            return self._parent._cast(_2064.BearingRatingLife)

        @property
        def dynamic_axial_load_carrying_capacity(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2065
            
            return self._parent._cast(_2065.DynamicAxialLoadCarryingCapacity)

        @property
        def frequencies(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2066
            
            return self._parent._cast(_2066.Frequencies)

        @property
        def friction(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2068
            
            return self._parent._cast(_2068.Friction)

        @property
        def grease(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2071
            
            return self._parent._cast(_2071.Grease)

        @property
        def grease_life_and_relubrication_interval(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2072
            
            return self._parent._cast(_2072.GreaseLifeAndRelubricationInterval)

        @property
        def grease_quantity(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2073
            
            return self._parent._cast(_2073.GreaseQuantity)

        @property
        def initial_fill(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2074
            
            return self._parent._cast(_2074.InitialFill)

        @property
        def life_model(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2075
            
            return self._parent._cast(_2075.LifeModel)

        @property
        def minimum_load(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2076
            
            return self._parent._cast(_2076.MinimumLoad)

        @property
        def static_safety_factors(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2084
            
            return self._parent._cast(_2084.StaticSafetyFactors)

        @property
        def viscosities(self):
            from mastapy.bearings.bearing_results.rolling.skf_module import _2085
            
            return self._parent._cast(_2085.Viscosities)

        @property
        def skf_calculation_result(self) -> 'SKFCalculationResult':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SKFCalculationResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self) -> 'SKFCalculationResult._Cast_SKFCalculationResult':
        return self._Cast_SKFCalculationResult(self)
