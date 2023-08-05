"""_1776.py

UserTextRow
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility.report import _1774, _1767
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_USER_TEXT_ROW = python_net_import('SMT.MastaAPI.Utility.Report', 'UserTextRow')


__docformat__ = 'restructuredtext en'
__all__ = ('UserTextRow',)


class UserTextRow(_1767.CustomRow):
    """UserTextRow

    This is a mastapy class.
    """

    TYPE = _USER_TEXT_ROW

    class _Cast_UserTextRow:
        """Special nested class for casting UserTextRow to subclasses."""

        def __init__(self, parent: 'UserTextRow'):
            self._parent = parent

        @property
        def custom_row(self):
            return self._parent._cast(_1767.CustomRow)

        @property
        def custom_report_property_item(self):
            from mastapy.utility.report import _1762
            
            return self._parent._cast(_1762.CustomReportPropertyItem)

        @property
        def user_text_row(self) -> 'UserTextRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'UserTextRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_text(self) -> 'str':
        """str: 'AdditionalText' is the original name of this property."""

        temp = self.wrapped.AdditionalText

        if temp is None:
            return ''

        return temp

    @additional_text.setter
    def additional_text(self, value: 'str'):
        self.wrapped.AdditionalText = str(value) if value else ''

    @property
    def heading_size(self) -> '_1774.HeadingSize':
        """HeadingSize: 'HeadingSize' is the original name of this property."""

        temp = self.wrapped.HeadingSize

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1774.HeadingSize)
        return constructor.new_from_mastapy_type(_1774.HeadingSize)(value) if value is not None else None

    @heading_size.setter
    def heading_size(self, value: '_1774.HeadingSize'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1774.HeadingSize.type_())
        self.wrapped.HeadingSize = value

    @property
    def is_heading(self) -> 'bool':
        """bool: 'IsHeading' is the original name of this property."""

        temp = self.wrapped.IsHeading

        if temp is None:
            return False

        return temp

    @is_heading.setter
    def is_heading(self, value: 'bool'):
        self.wrapped.IsHeading = bool(value) if value else False

    @property
    def show_additional_text(self) -> 'bool':
        """bool: 'ShowAdditionalText' is the original name of this property."""

        temp = self.wrapped.ShowAdditionalText

        if temp is None:
            return False

        return temp

    @show_additional_text.setter
    def show_additional_text(self, value: 'bool'):
        self.wrapped.ShowAdditionalText = bool(value) if value else False

    @property
    def text(self) -> 'str':
        """str: 'Text' is the original name of this property."""

        temp = self.wrapped.Text

        if temp is None:
            return ''

        return temp

    @text.setter
    def text(self, value: 'str'):
        self.wrapped.Text = str(value) if value else ''

    @property
    def cast_to(self) -> 'UserTextRow._Cast_UserTextRow':
        return self._Cast_UserTextRow(self)
