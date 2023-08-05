"""_628.py

MicroGeometryInputs
"""
from typing import List, TypeVar, Generic

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy.gears.manufacturing.cylindrical import _631
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_INPUTS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'MicroGeometryInputs')


__docformat__ = 'restructuredtext en'
__all__ = ('MicroGeometryInputs',)


T = TypeVar('T', bound='_631.ModificationSegment')


class MicroGeometryInputs(_0.APIBase, Generic[T]):
    """MicroGeometryInputs

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _MICRO_GEOMETRY_INPUTS

    class _Cast_MicroGeometryInputs:
        """Special nested class for casting MicroGeometryInputs to subclasses."""

        def __init__(self, parent: 'MicroGeometryInputs'):
            self._parent = parent

        @property
        def micro_geometry_inputs_lead(self):
            from mastapy.gears.manufacturing.cylindrical import _629
            
            return self._parent._cast(_629.MicroGeometryInputsLead)

        @property
        def micro_geometry_inputs_profile(self):
            from mastapy.gears.manufacturing.cylindrical import _630
            
            return self._parent._cast(_630.MicroGeometryInputsProfile)

        @property
        def micro_geometry_inputs(self) -> 'MicroGeometryInputs':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MicroGeometryInputs.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def modification_at_starting_point(self) -> 'float':
        """float: 'ModificationAtStartingPoint' is the original name of this property."""

        temp = self.wrapped.ModificationAtStartingPoint

        if temp is None:
            return 0.0

        return temp

    @modification_at_starting_point.setter
    def modification_at_starting_point(self, value: 'float'):
        self.wrapped.ModificationAtStartingPoint = float(value) if value else 0.0

    @property
    def micro_geometry_segments(self) -> 'List[T]':
        """List[T]: 'MicroGeometrySegments' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometrySegments

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
    def cast_to(self) -> 'MicroGeometryInputs._Cast_MicroGeometryInputs':
        return self._Cast_MicroGeometryInputs(self)
