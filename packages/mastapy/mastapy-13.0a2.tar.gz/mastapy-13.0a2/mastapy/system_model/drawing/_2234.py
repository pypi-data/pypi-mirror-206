"""_2234.py

PartAnalysisCaseWithContourViewable
"""
from typing import List

from mastapy._internal.implicit import enum_with_selected_value
from mastapy.utility.enums import _1809, _1810
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.system_model.drawing import _2227
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_ANALYSIS_CASE_WITH_CONTOUR_VIEWABLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'PartAnalysisCaseWithContourViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('PartAnalysisCaseWithContourViewable',)


class PartAnalysisCaseWithContourViewable(_0.APIBase):
    """PartAnalysisCaseWithContourViewable

    This is a mastapy class.
    """

    TYPE = _PART_ANALYSIS_CASE_WITH_CONTOUR_VIEWABLE

    class _Cast_PartAnalysisCaseWithContourViewable:
        """Special nested class for casting PartAnalysisCaseWithContourViewable to subclasses."""

        def __init__(self, parent: 'PartAnalysisCaseWithContourViewable'):
            self._parent = parent

        @property
        def abstract_system_deflection_viewable(self):
            from mastapy.system_model.drawing import _2224
            
            return self._parent._cast(_2224.AbstractSystemDeflectionViewable)

        @property
        def advanced_system_deflection_viewable(self):
            from mastapy.system_model.drawing import _2225
            
            return self._parent._cast(_2225.AdvancedSystemDeflectionViewable)

        @property
        def dynamic_analysis_viewable(self):
            from mastapy.system_model.drawing import _2229
            
            return self._parent._cast(_2229.DynamicAnalysisViewable)

        @property
        def harmonic_analysis_viewable(self):
            from mastapy.system_model.drawing import _2230
            
            return self._parent._cast(_2230.HarmonicAnalysisViewable)

        @property
        def modal_analysis_viewable(self):
            from mastapy.system_model.drawing import _2232
            
            return self._parent._cast(_2232.ModalAnalysisViewable)

        @property
        def system_deflection_viewable(self):
            from mastapy.system_model.drawing import _2241
            
            return self._parent._cast(_2241.SystemDeflectionViewable)

        @property
        def part_analysis_case_with_contour_viewable(self) -> 'PartAnalysisCaseWithContourViewable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartAnalysisCaseWithContourViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contour(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection':
        """enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection: 'Contour' is the original name of this property."""

        temp = self.wrapped.Contour

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @contour.setter
    def contour(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Contour = value

    @property
    def contour_secondary(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection':
        """enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection: 'ContourSecondary' is the original name of this property."""

        temp = self.wrapped.ContourSecondary

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @contour_secondary.setter
    def contour_secondary(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ContourSecondary = value

    @property
    def contour_draw_style(self) -> '_2227.ContourDrawStyle':
        """ContourDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def cast_to(self) -> 'PartAnalysisCaseWithContourViewable._Cast_PartAnalysisCaseWithContourViewable':
        return self._Cast_PartAnalysisCaseWithContourViewable(self)
