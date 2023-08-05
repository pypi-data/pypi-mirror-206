"""_1750.py

CustomReportHorizontalLine
"""
from mastapy.utility.report import _1752
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_HORIZONTAL_LINE = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportHorizontalLine')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportHorizontalLine',)


class CustomReportHorizontalLine(_1752.CustomReportItem):
    """CustomReportHorizontalLine

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_HORIZONTAL_LINE

    class _Cast_CustomReportHorizontalLine:
        """Special nested class for casting CustomReportHorizontalLine to subclasses."""

        def __init__(self, parent: 'CustomReportHorizontalLine'):
            self._parent = parent

        @property
        def custom_report_item(self):
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def custom_report_horizontal_line(self) -> 'CustomReportHorizontalLine':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportHorizontalLine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomReportHorizontalLine._Cast_CustomReportHorizontalLine':
        return self._Cast_CustomReportHorizontalLine(self)
