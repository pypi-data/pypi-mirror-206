"""_2103.py

LoadedFluidFilmBearingPad
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_FLUID_FILM_BEARING_PAD = python_net_import('SMT.MastaAPI.Bearings.BearingResults.FluidFilm', 'LoadedFluidFilmBearingPad')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedFluidFilmBearingPad',)


class LoadedFluidFilmBearingPad(_0.APIBase):
    """LoadedFluidFilmBearingPad

    This is a mastapy class.
    """

    TYPE = _LOADED_FLUID_FILM_BEARING_PAD

    class _Cast_LoadedFluidFilmBearingPad:
        """Special nested class for casting LoadedFluidFilmBearingPad to subclasses."""

        def __init__(self, parent: 'LoadedFluidFilmBearingPad'):
            self._parent = parent

        @property
        def loaded_tilting_journal_pad(self):
            from mastapy.bearings.bearing_results.fluid_film import _2111
            
            return self._parent._cast(_2111.LoadedTiltingJournalPad)

        @property
        def loaded_tilting_thrust_pad(self):
            from mastapy.bearings.bearing_results.fluid_film import _2114
            
            return self._parent._cast(_2114.LoadedTiltingThrustPad)

        @property
        def loaded_fluid_film_bearing_pad(self) -> 'LoadedFluidFilmBearingPad':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedFluidFilmBearingPad.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def misalignment(self) -> 'float':
        """float: 'Misalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Misalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def pad_id(self) -> 'str':
        """str: 'PadID' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PadID

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
    def cast_to(self) -> 'LoadedFluidFilmBearingPad._Cast_LoadedFluidFilmBearingPad':
        return self._Cast_LoadedFluidFilmBearingPad(self)
