"""_1749.py

CustomReportDefinitionItem
"""
from mastapy.utility.report import _1760
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_DEFINITION_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportDefinitionItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportDefinitionItem',)


class CustomReportDefinitionItem(_1760.CustomReportNameableItem):
    """CustomReportDefinitionItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_DEFINITION_ITEM

    class _Cast_CustomReportDefinitionItem:
        """Special nested class for casting CustomReportDefinitionItem to subclasses."""

        def __init__(self, parent: 'CustomReportDefinitionItem'):
            self._parent = parent

        @property
        def custom_report_nameable_item(self):
            return self._parent._cast(_1760.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def ad_hoc_custom_table(self):
            from mastapy.utility.report import _1731
            
            return self._parent._cast(_1731.AdHocCustomTable)

        @property
        def custom_chart(self):
            from mastapy.utility.report import _1739
            
            return self._parent._cast(_1739.CustomChart)

        @property
        def custom_drawing(self):
            from mastapy.utility.report import _1740
            
            return self._parent._cast(_1740.CustomDrawing)

        @property
        def custom_graphic(self):
            from mastapy.utility.report import _1741
            
            return self._parent._cast(_1741.CustomGraphic)

        @property
        def custom_image(self):
            from mastapy.utility.report import _1742
            
            return self._parent._cast(_1742.CustomImage)

        @property
        def custom_report_html_item(self):
            from mastapy.utility.report import _1751
            
            return self._parent._cast(_1751.CustomReportHtmlItem)

        @property
        def custom_report_status_item(self):
            from mastapy.utility.report import _1763
            
            return self._parent._cast(_1763.CustomReportStatusItem)

        @property
        def custom_report_text(self):
            from mastapy.utility.report import _1766
            
            return self._parent._cast(_1766.CustomReportText)

        @property
        def custom_sub_report(self):
            from mastapy.utility.report import _1768
            
            return self._parent._cast(_1768.CustomSubReport)

        @property
        def loaded_bearing_chart_reporter(self):
            from mastapy.bearings.bearing_results import _1932
            
            return self._parent._cast(_1932.LoadedBearingChartReporter)

        @property
        def parametric_study_histogram(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4361
            
            return self._parent._cast(_4361.ParametricStudyHistogram)

        @property
        def custom_report_definition_item(self) -> 'CustomReportDefinitionItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportDefinitionItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomReportDefinitionItem._Cast_CustomReportDefinitionItem':
        return self._Cast_CustomReportDefinitionItem(self)
