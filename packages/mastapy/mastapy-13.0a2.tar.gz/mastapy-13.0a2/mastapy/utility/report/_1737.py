"""_1737.py

ChartDefinition
"""
from typing import List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CHART_DEFINITION = python_net_import('SMT.MastaAPI.Utility.Report', 'ChartDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('ChartDefinition',)


class ChartDefinition(_0.APIBase):
    """ChartDefinition

    This is a mastapy class.
    """

    TYPE = _CHART_DEFINITION

    class _Cast_ChartDefinition:
        """Special nested class for casting ChartDefinition to subclasses."""

        def __init__(self, parent: 'ChartDefinition'):
            self._parent = parent

        @property
        def simple_chart_definition(self):
            from mastapy.utility.report import _1775
            
            return self._parent._cast(_1775.SimpleChartDefinition)

        @property
        def bubble_chart_definition(self):
            from mastapy.utility_gui.charts import _1838
            
            return self._parent._cast(_1838.BubbleChartDefinition)

        @property
        def legacy_chart_math_chart_definition(self):
            from mastapy.utility_gui.charts import _1842
            
            return self._parent._cast(_1842.LegacyChartMathChartDefinition)

        @property
        def nd_chart_definition(self):
            from mastapy.utility_gui.charts import _1844
            
            return self._parent._cast(_1844.NDChartDefinition)

        @property
        def parallel_coordinates_chart_definition(self):
            from mastapy.utility_gui.charts import _1845
            
            return self._parent._cast(_1845.ParallelCoordinatesChartDefinition)

        @property
        def scatter_chart_definition(self):
            from mastapy.utility_gui.charts import _1847
            
            return self._parent._cast(_1847.ScatterChartDefinition)

        @property
        def three_d_chart_definition(self):
            from mastapy.utility_gui.charts import _1850
            
            return self._parent._cast(_1850.ThreeDChartDefinition)

        @property
        def three_d_vector_chart_definition(self):
            from mastapy.utility_gui.charts import _1851
            
            return self._parent._cast(_1851.ThreeDVectorChartDefinition)

        @property
        def two_d_chart_definition(self):
            from mastapy.utility_gui.charts import _1852
            
            return self._parent._cast(_1852.TwoDChartDefinition)

        @property
        def chart_definition(self) -> 'ChartDefinition':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ChartDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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

    def to_bitmap(self) -> 'Image':
        """ 'ToBitmap' is the original name of this method.

        Returns:
            Image
        """

        return conversion.pn_to_mp_smt_bitmap(self.wrapped.ToBitmap())

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
    def cast_to(self) -> 'ChartDefinition._Cast_ChartDefinition':
        return self._Cast_ChartDefinition(self)
