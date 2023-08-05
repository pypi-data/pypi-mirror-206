"""_2017.py

LoadedRollingBearingRaceResults
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLING_BEARING_RACE_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedRollingBearingRaceResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedRollingBearingRaceResults',)


class LoadedRollingBearingRaceResults(_0.APIBase):
    """LoadedRollingBearingRaceResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLING_BEARING_RACE_RESULTS

    class _Cast_LoadedRollingBearingRaceResults:
        """Special nested class for casting LoadedRollingBearingRaceResults to subclasses."""

        def __init__(self, parent: 'LoadedRollingBearingRaceResults'):
            self._parent = parent

        @property
        def loaded_ball_bearing_race_results(self):
            from mastapy.bearings.bearing_results.rolling import _1986
            
            return self._parent._cast(_1986.LoadedBallBearingRaceResults)

        @property
        def loaded_four_point_contact_ball_bearing_race_results(self):
            from mastapy.bearings.bearing_results.rolling import _2001
            
            return self._parent._cast(_2001.LoadedFourPointContactBallBearingRaceResults)

        @property
        def loaded_rolling_bearing_race_results(self) -> 'LoadedRollingBearingRaceResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedRollingBearingRaceResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_radius_in_rolling_direction(self) -> 'float':
        """float: 'ContactRadiusInRollingDirection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactRadiusInRollingDirection

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness(self) -> 'float':
        """float: 'MinimumLubricatingFilmThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

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
    def cast_to(self) -> 'LoadedRollingBearingRaceResults._Cast_LoadedRollingBearingRaceResults':
        return self._Cast_LoadedRollingBearingRaceResults(self)
