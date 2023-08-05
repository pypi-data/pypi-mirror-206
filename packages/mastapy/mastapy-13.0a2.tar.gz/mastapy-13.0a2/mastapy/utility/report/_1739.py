"""_1739.py

CustomChart
"""
from mastapy._internal import constructor
from mastapy.utility.report import _1741
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_CHART = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomChart')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomChart',)


class CustomChart(_1741.CustomGraphic):
    """CustomChart

    This is a mastapy class.
    """

    TYPE = _CUSTOM_CHART

    class _Cast_CustomChart:
        """Special nested class for casting CustomChart to subclasses."""

        def __init__(self, parent: 'CustomChart'):
            self._parent = parent

        @property
        def custom_graphic(self):
            return self._parent._cast(_1741.CustomGraphic)

        @property
        def custom_report_definition_item(self):
            from mastapy.utility.report import _1749
            
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
        def custom_chart(self) -> 'CustomChart':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomChart.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def line_thickness_factor(self) -> 'int':
        """int: 'LineThicknessFactor' is the original name of this property."""

        temp = self.wrapped.LineThicknessFactor

        if temp is None:
            return 0

        return temp

    @line_thickness_factor.setter
    def line_thickness_factor(self, value: 'int'):
        self.wrapped.LineThicknessFactor = int(value) if value else 0

    @property
    def show_header(self) -> 'bool':
        """bool: 'ShowHeader' is the original name of this property."""

        temp = self.wrapped.ShowHeader

        if temp is None:
            return False

        return temp

    @show_header.setter
    def show_header(self, value: 'bool'):
        self.wrapped.ShowHeader = bool(value) if value else False

    @property
    def text_is_uppercase(self) -> 'bool':
        """bool: 'TextIsUppercase' is the original name of this property."""

        temp = self.wrapped.TextIsUppercase

        if temp is None:
            return False

        return temp

    @text_is_uppercase.setter
    def text_is_uppercase(self, value: 'bool'):
        self.wrapped.TextIsUppercase = bool(value) if value else False

    @property
    def cast_to(self) -> 'CustomChart._Cast_CustomChart':
        return self._Cast_CustomChart(self)
