"""_1760.py

CustomReportNameableItem
"""
from mastapy._internal import constructor
from mastapy.utility.report import _1752
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_NAMEABLE_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportNameableItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportNameableItem',)


class CustomReportNameableItem(_1752.CustomReportItem):
    """CustomReportNameableItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_NAMEABLE_ITEM

    class _Cast_CustomReportNameableItem:
        """Special nested class for casting CustomReportNameableItem to subclasses."""

        def __init__(self, parent: 'CustomReportNameableItem'):
            self._parent = parent

        @property
        def custom_report_item(self):
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def shaft_damage_results_table_and_chart(self):
            from mastapy.shafts import _20
            
            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def cylindrical_gear_table_with_mg_charts(self):
            from mastapy.gears.gear_designs.cylindrical import _1029
            
            return self._parent._cast(_1029.CylindricalGearTableWithMGCharts)

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
        def custom_report_cad_drawing(self):
            from mastapy.utility.report import _1744
            
            return self._parent._cast(_1744.CustomReportCadDrawing)

        @property
        def custom_report_chart(self):
            from mastapy.utility.report import _1745
            
            return self._parent._cast(_1745.CustomReportChart)

        @property
        def custom_report_definition_item(self):
            from mastapy.utility.report import _1749
            
            return self._parent._cast(_1749.CustomReportDefinitionItem)

        @property
        def custom_report_html_item(self):
            from mastapy.utility.report import _1751
            
            return self._parent._cast(_1751.CustomReportHtmlItem)

        @property
        def custom_report_multi_property_item(self):
            from mastapy.utility.report import _1758
            
            return self._parent._cast(_1758.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(self):
            from mastapy.utility.report import _1759
            
            return self._parent._cast(_1759.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_named_item(self):
            from mastapy.utility.report import _1761
            
            return self._parent._cast(_1761.CustomReportNamedItem)

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
        def custom_table(self):
            from mastapy.utility.report import _1769
            
            return self._parent._cast(_1769.CustomTable)

        @property
        def dynamic_custom_report_item(self):
            from mastapy.utility.report import _1771
            
            return self._parent._cast(_1771.DynamicCustomReportItem)

        @property
        def custom_line_chart(self):
            from mastapy.utility_gui.charts import _1840
            
            return self._parent._cast(_1840.CustomLineChart)

        @property
        def custom_table_and_chart(self):
            from mastapy.utility_gui.charts import _1841
            
            return self._parent._cast(_1841.CustomTableAndChart)

        @property
        def loaded_ball_element_chart_reporter(self):
            from mastapy.bearings.bearing_results import _1931
            
            return self._parent._cast(_1931.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_chart_reporter(self):
            from mastapy.bearings.bearing_results import _1932
            
            return self._parent._cast(_1932.LoadedBearingChartReporter)

        @property
        def loaded_bearing_temperature_chart(self):
            from mastapy.bearings.bearing_results import _1935
            
            return self._parent._cast(_1935.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(self):
            from mastapy.bearings.bearing_results import _1943
            
            return self._parent._cast(_1943.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(self):
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import _2828
            
            return self._parent._cast(_2828.ShaftSystemDeflectionSectionsReport)

        @property
        def parametric_study_histogram(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4361
            
            return self._parent._cast(_4361.ParametricStudyHistogram)

        @property
        def campbell_diagram_report(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4690
            
            return self._parent._cast(_4690.CampbellDiagramReport)

        @property
        def per_mode_results_report(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4694
            
            return self._parent._cast(_4694.PerModeResultsReport)

        @property
        def custom_report_nameable_item(self) -> 'CustomReportNameableItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportNameableItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def x_position_for_cad(self) -> 'float':
        """float: 'XPositionForCAD' is the original name of this property."""

        temp = self.wrapped.XPositionForCAD

        if temp is None:
            return 0.0

        return temp

    @x_position_for_cad.setter
    def x_position_for_cad(self, value: 'float'):
        self.wrapped.XPositionForCAD = float(value) if value else 0.0

    @property
    def y_position_for_cad(self) -> 'float':
        """float: 'YPositionForCAD' is the original name of this property."""

        temp = self.wrapped.YPositionForCAD

        if temp is None:
            return 0.0

        return temp

    @y_position_for_cad.setter
    def y_position_for_cad(self, value: 'float'):
        self.wrapped.YPositionForCAD = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'CustomReportNameableItem._Cast_CustomReportNameableItem':
        return self._Cast_CustomReportNameableItem(self)
