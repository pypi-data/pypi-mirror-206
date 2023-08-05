﻿"""_1762.py

CustomReportPropertyItem
"""
from mastapy.utility.report import _1772, _1773
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.utility.reporting_property_framework import _1777
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_PROPERTY_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportPropertyItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportPropertyItem',)


class CustomReportPropertyItem(_0.APIBase):
    """CustomReportPropertyItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_PROPERTY_ITEM

    class _Cast_CustomReportPropertyItem:
        """Special nested class for casting CustomReportPropertyItem to subclasses."""

        def __init__(self, parent: 'CustomReportPropertyItem'):
            self._parent = parent

        @property
        def blank_row(self):
            from mastapy.utility.report import _1733
            
            return self._parent._cast(_1733.BlankRow)

        @property
        def custom_report_chart_item(self):
            from mastapy.utility.report import _1746
            
            return self._parent._cast(_1746.CustomReportChartItem)

        @property
        def custom_row(self):
            from mastapy.utility.report import _1767
            
            return self._parent._cast(_1767.CustomRow)

        @property
        def user_text_row(self):
            from mastapy.utility.report import _1776
            
            return self._parent._cast(_1776.UserTextRow)

        @property
        def custom_report_property_item(self) -> 'CustomReportPropertyItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportPropertyItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def font_style(self) -> '_1772.FontStyle':
        """FontStyle: 'FontStyle' is the original name of this property."""

        temp = self.wrapped.FontStyle

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1772.FontStyle)
        return constructor.new_from_mastapy_type(_1772.FontStyle)(value) if value is not None else None

    @font_style.setter
    def font_style(self, value: '_1772.FontStyle'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1772.FontStyle.type_())
        self.wrapped.FontStyle = value

    @property
    def font_weight(self) -> '_1773.FontWeight':
        """FontWeight: 'FontWeight' is the original name of this property."""

        temp = self.wrapped.FontWeight

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1773.FontWeight)
        return constructor.new_from_mastapy_type(_1773.FontWeight)(value) if value is not None else None

    @font_weight.setter
    def font_weight(self, value: '_1773.FontWeight'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1773.FontWeight.type_())
        self.wrapped.FontWeight = value

    @property
    def horizontal_position(self) -> '_1777.CellValuePosition':
        """CellValuePosition: 'HorizontalPosition' is the original name of this property."""

        temp = self.wrapped.HorizontalPosition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1777.CellValuePosition)
        return constructor.new_from_mastapy_type(_1777.CellValuePosition)(value) if value is not None else None

    @horizontal_position.setter
    def horizontal_position(self, value: '_1777.CellValuePosition'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1777.CellValuePosition.type_())
        self.wrapped.HorizontalPosition = value

    @property
    def show_property_name(self) -> 'bool':
        """bool: 'ShowPropertyName' is the original name of this property."""

        temp = self.wrapped.ShowPropertyName

        if temp is None:
            return False

        return temp

    @show_property_name.setter
    def show_property_name(self, value: 'bool'):
        self.wrapped.ShowPropertyName = bool(value) if value else False

    def add_condition(self):
        """ 'AddCondition' is the original name of this method."""

        self.wrapped.AddCondition()

    @property
    def cast_to(self) -> 'CustomReportPropertyItem._Cast_CustomReportPropertyItem':
        return self._Cast_CustomReportPropertyItem(self)
