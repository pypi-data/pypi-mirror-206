"""_2676.py

BearingDynamicResultsUIWrapper
"""
from typing import List

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2677, _2675, _2673, _2674
)
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DYNAMIC_RESULTS_UI_WRAPPER = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BearingDynamicResultsUIWrapper')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDynamicResultsUIWrapper',)


class BearingDynamicResultsUIWrapper(_0.APIBase):
    """BearingDynamicResultsUIWrapper

    This is a mastapy class.
    """

    TYPE = _BEARING_DYNAMIC_RESULTS_UI_WRAPPER

    class _Cast_BearingDynamicResultsUIWrapper:
        """Special nested class for casting BearingDynamicResultsUIWrapper to subclasses."""

        def __init__(self, parent: 'BearingDynamicResultsUIWrapper'):
            self._parent = parent

        @property
        def bearing_dynamic_results_ui_wrapper(self) -> 'BearingDynamicResultsUIWrapper':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingDynamicResultsUIWrapper.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_revolutions_to_plot(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumRevolutionsToPlot' is the original name of this property."""

        temp = self.wrapped.MaximumRevolutionsToPlot

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @maximum_revolutions_to_plot.setter
    def maximum_revolutions_to_plot(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumRevolutionsToPlot = value

    @property
    def maximum_time_to_plot(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumTimeToPlot' is the original name of this property."""

        temp = self.wrapped.MaximumTimeToPlot

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @maximum_time_to_plot.setter
    def maximum_time_to_plot(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumTimeToPlot = value

    @property
    def minimum_revolutions_to_plot(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MinimumRevolutionsToPlot' is the original name of this property."""

        temp = self.wrapped.MinimumRevolutionsToPlot

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @minimum_revolutions_to_plot.setter
    def minimum_revolutions_to_plot(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MinimumRevolutionsToPlot = value

    @property
    def minimum_time_to_plot(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MinimumTimeToPlot' is the original name of this property."""

        temp = self.wrapped.MinimumTimeToPlot

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @minimum_time_to_plot.setter
    def minimum_time_to_plot(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MinimumTimeToPlot = value

    @property
    def plot_against_number_of_revolutions(self) -> 'bool':
        """bool: 'PlotAgainstNumberOfRevolutions' is the original name of this property."""

        temp = self.wrapped.PlotAgainstNumberOfRevolutions

        if temp is None:
            return False

        return temp

    @plot_against_number_of_revolutions.setter
    def plot_against_number_of_revolutions(self, value: 'bool'):
        self.wrapped.PlotAgainstNumberOfRevolutions = bool(value) if value else False

    @property
    def bearing_system_deflection(self) -> '_2677.BearingSystemDeflection':
        """BearingSystemDeflection: 'BearingSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_results(self) -> 'List[_2675.BearingDynamicResultsPropertyWrapper]':
        """List[BearingDynamicResultsPropertyWrapper]: 'BearingResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cage_results(self) -> 'List[_2675.BearingDynamicResultsPropertyWrapper]':
        """List[BearingDynamicResultsPropertyWrapper]: 'CageResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CageResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def element_results(self) -> 'List[_2673.BearingDynamicElementPropertyWrapper]':
        """List[BearingDynamicElementPropertyWrapper]: 'ElementResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def post_analysis_results(self) -> 'List[_2674.BearingDynamicPostAnalysisResultWrapper]':
        """List[BearingDynamicPostAnalysisResultWrapper]: 'PostAnalysisResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PostAnalysisResults

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

    def clear_all_plots(self):
        """ 'ClearAllPlots' is the original name of this method."""

        self.wrapped.ClearAllPlots()

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
    def cast_to(self) -> 'BearingDynamicResultsUIWrapper._Cast_BearingDynamicResultsUIWrapper':
        return self._Cast_BearingDynamicResultsUIWrapper(self)
