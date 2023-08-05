"""_1442.py

CycloidalDiscDesign
"""
from typing import List

from mastapy.utility_gui.charts import _1852
from mastapy._internal import constructor, conversion
from mastapy.cycloidal import _1443, _1446
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_DESIGN = python_net_import('SMT.MastaAPI.Cycloidal', 'CycloidalDiscDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscDesign',)


class CycloidalDiscDesign(_0.APIBase):
    """CycloidalDiscDesign

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_DESIGN

    class _Cast_CycloidalDiscDesign:
        """Special nested class for casting CycloidalDiscDesign to subclasses."""

        def __init__(self, parent: 'CycloidalDiscDesign'):
            self._parent = parent

        @property
        def cycloidal_disc_design(self) -> 'CycloidalDiscDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'CrowningChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CrowningChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def disc_id(self) -> 'int':
        """int: 'DiscID' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiscID

        if temp is None:
            return 0

        return temp

    @property
    def estimated_modifications_from_spline_fit(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'EstimatedModificationsFromSplineFit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EstimatedModificationsFromSplineFit

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property."""

        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value else 0.0

    @property
    def generating_wheel_centre_circle_diameter(self) -> 'float':
        """float: 'GeneratingWheelCentreCircleDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeneratingWheelCentreCircleDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def generating_wheel_diameter(self) -> 'float':
        """float: 'GeneratingWheelDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeneratingWheelDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def lobe_symmetry_angle_with_no_lobe_modifications(self) -> 'float':
        """float: 'LobeSymmetryAngleWithNoLobeModifications' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LobeSymmetryAngleWithNoLobeModifications

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def exporter(self) -> '_1443.CycloidalDiscDesignExporter':
        """CycloidalDiscDesignExporter: 'Exporter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Exporter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def modifications_specification(self) -> '_1446.CycloidalDiscModificationsSpecification':
        """CycloidalDiscModificationsSpecification: 'ModificationsSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModificationsSpecification

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
    def cast_to(self) -> 'CycloidalDiscDesign._Cast_CycloidalDiscDesign':
        return self._Cast_CycloidalDiscDesign(self)
