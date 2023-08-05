"""_1105.py

CylindricalGearTriangularEndModificationAtOrientation
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1123
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION_AT_ORIENTATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearTriangularEndModificationAtOrientation')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearTriangularEndModificationAtOrientation',)


class CylindricalGearTriangularEndModificationAtOrientation(_0.APIBase):
    """CylindricalGearTriangularEndModificationAtOrientation

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION_AT_ORIENTATION

    class _Cast_CylindricalGearTriangularEndModificationAtOrientation:
        """Special nested class for casting CylindricalGearTriangularEndModificationAtOrientation to subclasses."""

        def __init__(self, parent: 'CylindricalGearTriangularEndModificationAtOrientation'):
            self._parent = parent

        @property
        def cylindrical_gear_triangular_end_modification_at_orientation(self) -> 'CylindricalGearTriangularEndModificationAtOrientation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearTriangularEndModificationAtOrientation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orientation(self) -> 'str':
        """str: 'Orientation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Orientation

        if temp is None:
            return ''

        return temp

    @property
    def linear(self) -> '_1123.SingleCylindricalGearTriangularEndModification':
        """SingleCylindricalGearTriangularEndModification: 'Linear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Linear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def parabolic(self) -> '_1123.SingleCylindricalGearTriangularEndModification':
        """SingleCylindricalGearTriangularEndModification: 'Parabolic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Parabolic

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
    def cast_to(self) -> 'CylindricalGearTriangularEndModificationAtOrientation._Cast_CylindricalGearTriangularEndModificationAtOrientation':
        return self._Cast_CylindricalGearTriangularEndModificationAtOrientation(self)
