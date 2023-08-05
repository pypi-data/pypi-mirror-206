"""_1733.py

BlankRow
"""
from mastapy.utility.report import _1767
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BLANK_ROW = python_net_import('SMT.MastaAPI.Utility.Report', 'BlankRow')


__docformat__ = 'restructuredtext en'
__all__ = ('BlankRow',)


class BlankRow(_1767.CustomRow):
    """BlankRow

    This is a mastapy class.
    """

    TYPE = _BLANK_ROW

    class _Cast_BlankRow:
        """Special nested class for casting BlankRow to subclasses."""

        def __init__(self, parent: 'BlankRow'):
            self._parent = parent

        @property
        def custom_row(self):
            return self._parent._cast(_1767.CustomRow)

        @property
        def custom_report_property_item(self):
            from mastapy.utility.report import _1762
            
            return self._parent._cast(_1762.CustomReportPropertyItem)

        @property
        def blank_row(self) -> 'BlankRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BlankRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BlankRow._Cast_BlankRow':
        return self._Cast_BlankRow(self)
