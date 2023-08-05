"""_1290.py

StatorCutOutSpecification
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATOR_CUT_OUT_SPECIFICATION = python_net_import('SMT.MastaAPI.ElectricMachines', 'StatorCutOutSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('StatorCutOutSpecification',)


class StatorCutOutSpecification(_0.APIBase):
    """StatorCutOutSpecification

    This is a mastapy class.
    """

    TYPE = _STATOR_CUT_OUT_SPECIFICATION

    class _Cast_StatorCutOutSpecification:
        """Special nested class for casting StatorCutOutSpecification to subclasses."""

        def __init__(self, parent: 'StatorCutOutSpecification'):
            self._parent = parent

        @property
        def stator_cut_out_specification(self) -> 'StatorCutOutSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StatorCutOutSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_to_first_cut_out(self) -> 'float':
        """float: 'AngleToFirstCutOut' is the original name of this property."""

        temp = self.wrapped.AngleToFirstCutOut

        if temp is None:
            return 0.0

        return temp

    @angle_to_first_cut_out.setter
    def angle_to_first_cut_out(self, value: 'float'):
        self.wrapped.AngleToFirstCutOut = float(value) if value else 0.0

    @property
    def corner_radius(self) -> 'float':
        """float: 'CornerRadius' is the original name of this property."""

        temp = self.wrapped.CornerRadius

        if temp is None:
            return 0.0

        return temp

    @corner_radius.setter
    def corner_radius(self, value: 'float'):
        self.wrapped.CornerRadius = float(value) if value else 0.0

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

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
    def number_of_cut_outs(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfCutOuts' is the original name of this property."""

        temp = self.wrapped.NumberOfCutOuts

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else 0

    @number_of_cut_outs.setter
    def number_of_cut_outs(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfCutOuts = value

    @property
    def radial_position(self) -> 'float':
        """float: 'RadialPosition' is the original name of this property."""

        temp = self.wrapped.RadialPosition

        if temp is None:
            return 0.0

        return temp

    @radial_position.setter
    def radial_position(self, value: 'float'):
        self.wrapped.RadialPosition = float(value) if value else 0.0

    @property
    def rotation(self) -> 'float':
        """float: 'Rotation' is the original name of this property."""

        temp = self.wrapped.Rotation

        if temp is None:
            return 0.0

        return temp

    @rotation.setter
    def rotation(self, value: 'float'):
        self.wrapped.Rotation = float(value) if value else 0.0

    @property
    def width(self) -> 'float':
        """float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value else 0.0

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
    def cast_to(self) -> 'StatorCutOutSpecification._Cast_StatorCutOutSpecification':
        return self._Cast_StatorCutOutSpecification(self)
