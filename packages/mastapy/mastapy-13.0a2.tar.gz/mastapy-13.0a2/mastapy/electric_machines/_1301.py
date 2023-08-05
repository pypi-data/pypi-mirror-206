"""_1301.py

WindingConductor
"""
from typing import List

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WINDING_CONDUCTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'WindingConductor')


__docformat__ = 'restructuredtext en'
__all__ = ('WindingConductor',)


class WindingConductor(_0.APIBase):
    """WindingConductor

    This is a mastapy class.
    """

    TYPE = _WINDING_CONDUCTOR

    class _Cast_WindingConductor:
        """Special nested class for casting WindingConductor to subclasses."""

        def __init__(self, parent: 'WindingConductor'):
            self._parent = parent

        @property
        def cad_conductor(self):
            from mastapy.electric_machines import _1239
            
            return self._parent._cast(_1239.CADConductor)

        @property
        def hairpin_conductor(self):
            from mastapy.electric_machines import _1264
            
            return self._parent._cast(_1264.HairpinConductor)

        @property
        def winding_conductor(self) -> 'WindingConductor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WindingConductor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conductor_dimension_for_dq_model_ac_winding_loss_scaling_for_skin_depth(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ConductorDimensionForDQModelACWindingLossScalingForSkinDepth' is the original name of this property."""

        temp = self.wrapped.ConductorDimensionForDQModelACWindingLossScalingForSkinDepth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @conductor_dimension_for_dq_model_ac_winding_loss_scaling_for_skin_depth.setter
    def conductor_dimension_for_dq_model_ac_winding_loss_scaling_for_skin_depth(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ConductorDimensionForDQModelACWindingLossScalingForSkinDepth = value

    @property
    def layer_index(self) -> 'int':
        """int: 'LayerIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LayerIndex

        if temp is None:
            return 0

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
    def cast_to(self) -> 'WindingConductor._Cast_WindingConductor':
        return self._Cast_WindingConductor(self)
