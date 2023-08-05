"""_171.py

MechanicalContactSpecification
"""
from typing import List

from mastapy.nodal_analysis.elmer import _166
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MECHANICAL_CONTACT_SPECIFICATION = python_net_import('SMT.MastaAPI.NodalAnalysis.Elmer', 'MechanicalContactSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('MechanicalContactSpecification',)


class MechanicalContactSpecification(_0.APIBase):
    """MechanicalContactSpecification

    This is a mastapy class.
    """

    TYPE = _MECHANICAL_CONTACT_SPECIFICATION

    class _Cast_MechanicalContactSpecification:
        """Special nested class for casting MechanicalContactSpecification to subclasses."""

        def __init__(self, parent: 'MechanicalContactSpecification'):
            self._parent = parent

        @property
        def mechanical_contact_specification(self) -> 'MechanicalContactSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MechanicalContactSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_type(self) -> '_166.ContactType':
        """ContactType: 'ContactType' is the original name of this property."""

        temp = self.wrapped.ContactType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _166.ContactType)
        return constructor.new_from_mastapy_type(_166.ContactType)(value) if value is not None else None

    @contact_type.setter
    def contact_type(self, value: '_166.ContactType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _166.ContactType.type_())
        self.wrapped.ContactType = value

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
    def cast_to(self) -> 'MechanicalContactSpecification._Cast_MechanicalContactSpecification':
        return self._Cast_MechanicalContactSpecification(self)
