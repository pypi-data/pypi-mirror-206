"""_4694.py

PerModeResultsReport
"""
from mastapy.utility.enums import _1807
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.utility.report import _1745
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PER_MODE_RESULTS_REPORT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting', 'PerModeResultsReport')


__docformat__ = 'restructuredtext en'
__all__ = ('PerModeResultsReport',)


class PerModeResultsReport(_1745.CustomReportChart):
    """PerModeResultsReport

    This is a mastapy class.
    """

    TYPE = _PER_MODE_RESULTS_REPORT

    class _Cast_PerModeResultsReport:
        """Special nested class for casting PerModeResultsReport to subclasses."""

        def __init__(self, parent: 'PerModeResultsReport'):
            self._parent = parent

        @property
        def custom_report_chart(self):
            return self._parent._cast(_1745.CustomReportChart)

        @property
        def custom_report_multi_property_item(self):
            from mastapy.utility.report import _1758, _1746
            
            return self._parent._cast(_1758.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(self):
            from mastapy.utility.report import _1759
            
            return self._parent._cast(_1759.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(self):
            from mastapy.utility.report import _1760
            
            return self._parent._cast(_1760.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def per_mode_results_report(self) -> 'PerModeResultsReport':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PerModeResultsReport.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def display_option(self) -> '_1807.TableAndChartOptions':
        """TableAndChartOptions: 'DisplayOption' is the original name of this property."""

        temp = self.wrapped.DisplayOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1807.TableAndChartOptions)
        return constructor.new_from_mastapy_type(_1807.TableAndChartOptions)(value) if value is not None else None

    @display_option.setter
    def display_option(self, value: '_1807.TableAndChartOptions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1807.TableAndChartOptions.type_())
        self.wrapped.DisplayOption = value

    @property
    def include_connected_parts_for_connections(self) -> 'bool':
        """bool: 'IncludeConnectedPartsForConnections' is the original name of this property."""

        temp = self.wrapped.IncludeConnectedPartsForConnections

        if temp is None:
            return False

        return temp

    @include_connected_parts_for_connections.setter
    def include_connected_parts_for_connections(self, value: 'bool'):
        self.wrapped.IncludeConnectedPartsForConnections = bool(value) if value else False

    @property
    def maximum_number_of_modes_to_show_on_a_single_table_or_chart(self) -> 'int':
        """int: 'MaximumNumberOfModesToShowOnASingleTableOrChart' is the original name of this property."""

        temp = self.wrapped.MaximumNumberOfModesToShowOnASingleTableOrChart

        if temp is None:
            return 0

        return temp

    @maximum_number_of_modes_to_show_on_a_single_table_or_chart.setter
    def maximum_number_of_modes_to_show_on_a_single_table_or_chart(self, value: 'int'):
        self.wrapped.MaximumNumberOfModesToShowOnASingleTableOrChart = int(value) if value else 0

    @property
    def show_all_modes(self) -> 'bool':
        """bool: 'ShowAllModes' is the original name of this property."""

        temp = self.wrapped.ShowAllModes

        if temp is None:
            return False

        return temp

    @show_all_modes.setter
    def show_all_modes(self, value: 'bool'):
        self.wrapped.ShowAllModes = bool(value) if value else False

    @property
    def transpose_chart(self) -> 'bool':
        """bool: 'TransposeChart' is the original name of this property."""

        temp = self.wrapped.TransposeChart

        if temp is None:
            return False

        return temp

    @transpose_chart.setter
    def transpose_chart(self, value: 'bool'):
        self.wrapped.TransposeChart = bool(value) if value else False

    @property
    def transpose_table(self) -> 'bool':
        """bool: 'TransposeTable' is the original name of this property."""

        temp = self.wrapped.TransposeTable

        if temp is None:
            return False

        return temp

    @transpose_table.setter
    def transpose_table(self, value: 'bool'):
        self.wrapped.TransposeTable = bool(value) if value else False

    @property
    def cast_to(self) -> 'PerModeResultsReport._Cast_PerModeResultsReport':
        return self._Cast_PerModeResultsReport(self)
