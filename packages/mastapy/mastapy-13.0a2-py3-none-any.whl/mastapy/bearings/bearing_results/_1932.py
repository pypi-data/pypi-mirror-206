"""_1932.py

LoadedBearingChartReporter
"""
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility.report import _1742
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_CHART_REPORTER = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedBearingChartReporter')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBearingChartReporter',)


class LoadedBearingChartReporter(_1742.CustomImage):
    """LoadedBearingChartReporter

    This is a mastapy class.
    """

    TYPE = _LOADED_BEARING_CHART_REPORTER

    class _Cast_LoadedBearingChartReporter:
        """Special nested class for casting LoadedBearingChartReporter to subclasses."""

        def __init__(self, parent: 'LoadedBearingChartReporter'):
            self._parent = parent

        @property
        def custom_image(self):
            return self._parent._cast(_1742.CustomImage)

        @property
        def custom_graphic(self):
            from mastapy.utility.report import _1741
            
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
        def loaded_bearing_chart_reporter(self) -> 'LoadedBearingChartReporter':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedBearingChartReporter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def property_(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'Property' is the original name of this property."""

        temp = self.wrapped.Property

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @property_.setter
    def property_(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.Property = value

    @property
    def cast_to(self) -> 'LoadedBearingChartReporter._Cast_LoadedBearingChartReporter':
        return self._Cast_LoadedBearingChartReporter(self)
