"""_1759.py

CustomReportMultiPropertyItemBase
"""
from mastapy.utility.report import _1760
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_MULTI_PROPERTY_ITEM_BASE = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportMultiPropertyItemBase')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportMultiPropertyItemBase',)


class CustomReportMultiPropertyItemBase(_1760.CustomReportNameableItem):
    """CustomReportMultiPropertyItemBase

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_MULTI_PROPERTY_ITEM_BASE

    class _Cast_CustomReportMultiPropertyItemBase:
        """Special nested class for casting CustomReportMultiPropertyItemBase to subclasses."""

        def __init__(self, parent: 'CustomReportMultiPropertyItemBase'):
            self._parent = parent

        @property
        def custom_report_nameable_item(self):
            return self._parent._cast(_1760.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
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
        def custom_report_chart(self):
            from mastapy.utility.report import _1745
            
            return self._parent._cast(_1745.CustomReportChart)

        @property
        def custom_report_multi_property_item(self):
            from mastapy.utility.report import _1758
            
            return self._parent._cast(_1758.CustomReportMultiPropertyItem)

        @property
        def custom_table(self):
            from mastapy.utility.report import _1769
            
            return self._parent._cast(_1769.CustomTable)

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
        def campbell_diagram_report(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4690
            
            return self._parent._cast(_4690.CampbellDiagramReport)

        @property
        def per_mode_results_report(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4694
            
            return self._parent._cast(_4694.PerModeResultsReport)

        @property
        def custom_report_multi_property_item_base(self) -> 'CustomReportMultiPropertyItemBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportMultiPropertyItemBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase':
        return self._Cast_CustomReportMultiPropertyItemBase(self)
