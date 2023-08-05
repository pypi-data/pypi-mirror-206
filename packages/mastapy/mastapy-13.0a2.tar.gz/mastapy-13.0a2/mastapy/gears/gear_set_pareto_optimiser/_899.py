"""_899.py

ChartInfoBase
"""
from typing import List, TypeVar, Generic

from PIL.Image import Image

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility.reporting_property_framework import _1778
from mastapy.math_utility.optimisation import _1540
from mastapy.gears.gear_set_pareto_optimiser import _901, _897, _909
from mastapy import _0
from mastapy.gears.analysis import _1211
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CHART_INFO_BASE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'ChartInfoBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ChartInfoBase',)


TAnalysis = TypeVar('TAnalysis', bound='_1211.AbstractGearSetAnalysis')
TCandidate = TypeVar('TCandidate')


class ChartInfoBase(_0.APIBase, Generic[TAnalysis, TCandidate]):
    """ChartInfoBase

    This is a mastapy class.

    Generic Types:
        TAnalysis
        TCandidate
    """

    TYPE = _CHART_INFO_BASE

    class _Cast_ChartInfoBase:
        """Special nested class for casting ChartInfoBase to subclasses."""

        def __init__(self, parent: 'ChartInfoBase'):
            self._parent = parent

        @property
        def micro_geometry_design_space_search_chart_information(self):
            from mastapy.gears.gear_set_pareto_optimiser import _913
            
            return self._parent._cast(_913.MicroGeometryDesignSpaceSearchChartInformation)

        @property
        def pareto_optimiser_chart_information(self):
            from mastapy.gears.gear_set_pareto_optimiser import _927
            
            return self._parent._cast(_927.ParetoOptimiserChartInformation)

        @property
        def chart_info_base(self) -> 'ChartInfoBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ChartInfoBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chart_name(self) -> 'str':
        """str: 'ChartName' is the original name of this property."""

        temp = self.wrapped.ChartName

        if temp is None:
            return ''

        return temp

    @chart_name.setter
    def chart_name(self, value: 'str'):
        self.wrapped.ChartName = str(value) if value else ''

    @property
    def chart_type(self) -> '_1778.CustomChartType':
        """CustomChartType: 'ChartType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ChartType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1778.CustomChartType)
        return constructor.new_from_mastapy_type(_1778.CustomChartType)(value) if value is not None else None

    @property
    def result_chart_bar_and_line(self) -> 'Image':
        """Image: 'ResultChartBarAndLine' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultChartBarAndLine

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def result_chart_scatter(self) -> 'Image':
        """Image: 'ResultChartScatter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultChartScatter

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def select_chart_type(self) -> '_1540.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart':
        """ParetoOptimisationStrategyChartInformation.ScatterOrBarChart: 'SelectChartType' is the original name of this property."""

        temp = self.wrapped.SelectChartType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1540.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart)
        return constructor.new_from_mastapy_type(_1540.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart)(value) if value is not None else None

    @select_chart_type.setter
    def select_chart_type(self, value: '_1540.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1540.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart.type_())
        self.wrapped.SelectChartType = value

    @property
    def selected_candidate_design(self) -> 'int':
        """int: 'SelectedCandidateDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedCandidateDesign

        if temp is None:
            return 0

        return temp

    @property
    def optimiser(self) -> '_901.DesignSpaceSearchBase[TAnalysis, TCandidate]':
        """DesignSpaceSearchBase[TAnalysis, TCandidate]: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Optimiser

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[TAnalysis, TCandidate](temp) if temp is not None else None

    @property
    def bars(self) -> 'List[_897.BarForPareto[TAnalysis, TCandidate]]':
        """List[BarForPareto[TAnalysis, TCandidate]]: 'Bars' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bars

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def input_sliders(self) -> 'List[_909.InputSliderForPareto[TAnalysis, TCandidate]]':
        """List[InputSliderForPareto[TAnalysis, TCandidate]]: 'InputSliders' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InputSliders

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def add_bar(self):
        """ 'AddBar' is the original name of this method."""

        self.wrapped.AddBar()

    def add_selected_design(self):
        """ 'AddSelectedDesign' is the original name of this method."""

        self.wrapped.AddSelectedDesign()

    def add_selected_designs(self):
        """ 'AddSelectedDesigns' is the original name of this method."""

        self.wrapped.AddSelectedDesigns()

    def remove_chart(self):
        """ 'RemoveChart' is the original name of this method."""

        self.wrapped.RemoveChart()

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'ChartInfoBase._Cast_ChartInfoBase':
        return self._Cast_ChartInfoBase(self)
