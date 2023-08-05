"""_1731.py

AdHocCustomTable
"""
from mastapy.utility.report import _1749
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AD_HOC_CUSTOM_TABLE = python_net_import('SMT.MastaAPI.Utility.Report', 'AdHocCustomTable')


__docformat__ = 'restructuredtext en'
__all__ = ('AdHocCustomTable',)


class AdHocCustomTable(_1749.CustomReportDefinitionItem):
    """AdHocCustomTable

    This is a mastapy class.
    """

    TYPE = _AD_HOC_CUSTOM_TABLE

    class _Cast_AdHocCustomTable:
        """Special nested class for casting AdHocCustomTable to subclasses."""

        def __init__(self, parent: 'AdHocCustomTable'):
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
        def ad_hoc_custom_table(self) -> 'AdHocCustomTable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AdHocCustomTable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AdHocCustomTable._Cast_AdHocCustomTable':
        return self._Cast_AdHocCustomTable(self)
