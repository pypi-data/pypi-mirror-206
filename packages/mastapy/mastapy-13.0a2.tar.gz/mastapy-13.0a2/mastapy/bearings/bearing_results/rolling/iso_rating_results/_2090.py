"""_2090.py

ISOResults
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.IsoRatingResults', 'ISOResults')


__docformat__ = 'restructuredtext en'
__all__ = ('ISOResults',)


class ISOResults(_0.APIBase):
    """ISOResults

    This is a mastapy class.
    """

    TYPE = _ISO_RESULTS

    class _Cast_ISOResults:
        """Special nested class for casting ISOResults to subclasses."""

        def __init__(self, parent: 'ISOResults'):
            self._parent = parent

        @property
        def ball_iso2812007_results(self):
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2086
            
            return self._parent._cast(_2086.BallISO2812007Results)

        @property
        def ball_isots162812008_results(self):
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2087
            
            return self._parent._cast(_2087.BallISOTS162812008Results)

        @property
        def iso2812007_results(self):
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2088
            
            return self._parent._cast(_2088.ISO2812007Results)

        @property
        def isots162812008_results(self):
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2091
            
            return self._parent._cast(_2091.ISOTS162812008Results)

        @property
        def roller_iso2812007_results(self):
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2092
            
            return self._parent._cast(_2092.RollerISO2812007Results)

        @property
        def roller_isots162812008_results(self):
            from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2093
            
            return self._parent._cast(_2093.RollerISOTS162812008Results)

        @property
        def ansiabma112014_results(self):
            from mastapy.bearings.bearing_results.rolling.abma import _2100
            
            return self._parent._cast(_2100.ANSIABMA112014Results)

        @property
        def ansiabma92015_results(self):
            from mastapy.bearings.bearing_results.rolling.abma import _2101
            
            return self._parent._cast(_2101.ANSIABMA92015Results)

        @property
        def ansiabma_results(self):
            from mastapy.bearings.bearing_results.rolling.abma import _2102
            
            return self._parent._cast(_2102.ANSIABMAResults)

        @property
        def iso_results(self) -> 'ISOResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISOResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def life_modification_factor_for_reliability(self) -> 'float':
        """float: 'LifeModificationFactorForReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeModificationFactorForReliability

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(self) -> 'ISOResults._Cast_ISOResults':
        return self._Cast_ISOResults(self)
