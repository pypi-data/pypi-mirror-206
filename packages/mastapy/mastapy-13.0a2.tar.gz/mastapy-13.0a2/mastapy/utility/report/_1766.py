"""_1766.py

CustomReportText
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.html import _300
from mastapy.utility.report import _1749
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_TEXT = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportText')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportText',)


class CustomReportText(_1749.CustomReportDefinitionItem):
    """CustomReportText

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_TEXT

    class _Cast_CustomReportText:
        """Special nested class for casting CustomReportText to subclasses."""

        def __init__(self, parent: 'CustomReportText'):
            self._parent = parent

        @property
        def custom_report_definition_item(self):
            return self._parent._cast(_1749.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(self):
            from mastapy.utility.report import _1760
            
            return self._parent._cast(_1760.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def custom_report_text(self) -> 'CustomReportText':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportText.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bold(self) -> 'bool':
        """bool: 'Bold' is the original name of this property."""

        temp = self.wrapped.Bold

        if temp is None:
            return False

        return temp

    @bold.setter
    def bold(self, value: 'bool'):
        self.wrapped.Bold = bool(value) if value else False

    @property
    def cad_text_size(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CADTextSize' is the original name of this property."""

        temp = self.wrapped.CADTextSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @cad_text_size.setter
    def cad_text_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CADTextSize = value

    @property
    def heading_type(self) -> '_300.HeadingType':
        """HeadingType: 'HeadingType' is the original name of this property."""

        temp = self.wrapped.HeadingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _300.HeadingType)
        return constructor.new_from_mastapy_type(_300.HeadingType)(value) if value is not None else None

    @heading_type.setter
    def heading_type(self, value: '_300.HeadingType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _300.HeadingType.type_())
        self.wrapped.HeadingType = value

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
    def show_symbol(self) -> 'bool':
        """bool: 'ShowSymbol' is the original name of this property."""

        temp = self.wrapped.ShowSymbol

        if temp is None:
            return False

        return temp

    @show_symbol.setter
    def show_symbol(self, value: 'bool'):
        self.wrapped.ShowSymbol = bool(value) if value else False

    @property
    def show_unit(self) -> 'bool':
        """bool: 'ShowUnit' is the original name of this property."""

        temp = self.wrapped.ShowUnit

        if temp is None:
            return False

        return temp

    @show_unit.setter
    def show_unit(self, value: 'bool'):
        self.wrapped.ShowUnit = bool(value) if value else False

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
    def cast_to(self) -> 'CustomReportText._Cast_CustomReportText':
        return self._Cast_CustomReportText(self)
