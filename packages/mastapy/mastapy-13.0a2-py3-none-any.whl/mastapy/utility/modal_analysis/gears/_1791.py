"""_1791.py

OrderForTE
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ORDER_FOR_TE = python_net_import('SMT.MastaAPI.Utility.ModalAnalysis.Gears', 'OrderForTE')


__docformat__ = 'restructuredtext en'
__all__ = ('OrderForTE',)


class OrderForTE(_0.APIBase):
    """OrderForTE

    This is a mastapy class.
    """

    TYPE = _ORDER_FOR_TE

    class _Cast_OrderForTE:
        """Special nested class for casting OrderForTE to subclasses."""

        def __init__(self, parent: 'OrderForTE'):
            self._parent = parent

        @property
        def gear_mesh_for_te(self):
            from mastapy.utility.modal_analysis.gears import _1786
            
            return self._parent._cast(_1786.GearMeshForTE)

        @property
        def gear_order_for_te(self):
            from mastapy.utility.modal_analysis.gears import _1787
            
            return self._parent._cast(_1787.GearOrderForTE)

        @property
        def harmonic_order_for_te(self):
            from mastapy.utility.modal_analysis.gears import _1789
            
            return self._parent._cast(_1789.HarmonicOrderForTE)

        @property
        def label_only_order(self):
            from mastapy.utility.modal_analysis.gears import _1790
            
            return self._parent._cast(_1790.LabelOnlyOrder)

        @property
        def order_selector(self):
            from mastapy.utility.modal_analysis.gears import _1792
            
            return self._parent._cast(_1792.OrderSelector)

        @property
        def order_with_radius(self):
            from mastapy.utility.modal_analysis.gears import _1793
            
            return self._parent._cast(_1793.OrderWithRadius)

        @property
        def rolling_bearing_order(self):
            from mastapy.utility.modal_analysis.gears import _1794
            
            return self._parent._cast(_1794.RollingBearingOrder)

        @property
        def shaft_order_for_te(self):
            from mastapy.utility.modal_analysis.gears import _1795
            
            return self._parent._cast(_1795.ShaftOrderForTE)

        @property
        def user_defined_order_for_te(self):
            from mastapy.utility.modal_analysis.gears import _1796
            
            return self._parent._cast(_1796.UserDefinedOrderForTE)

        @property
        def order_for_te(self) -> 'OrderForTE':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OrderForTE.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def frequency_offset(self) -> 'float':
        """float: 'FrequencyOffset' is the original name of this property."""

        temp = self.wrapped.FrequencyOffset

        if temp is None:
            return 0.0

        return temp

    @frequency_offset.setter
    def frequency_offset(self, value: 'float'):
        self.wrapped.FrequencyOffset = float(value) if value else 0.0

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
    def order(self) -> 'float':
        """float: 'Order' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Order

        if temp is None:
            return 0.0

        return temp

    @property
    def children(self) -> 'List[OrderForTE]':
        """List[OrderForTE]: 'Children' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Children

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
    def cast_to(self) -> 'OrderForTE._Cast_OrderForTE':
        return self._Cast_OrderForTE(self)
