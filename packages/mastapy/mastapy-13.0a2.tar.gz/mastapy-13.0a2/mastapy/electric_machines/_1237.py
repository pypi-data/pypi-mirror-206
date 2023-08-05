"""_1237.py

AbstractStator
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.electric_machines import _1238, _1305
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_ABSTRACT_STATOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'AbstractStator')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractStator',)


class AbstractStator(_0.APIBase):
    """AbstractStator

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_STATOR

    class _Cast_AbstractStator:
        """Special nested class for casting AbstractStator to subclasses."""

        def __init__(self, parent: 'AbstractStator'):
            self._parent = parent

        @property
        def cad_stator(self):
            from mastapy.electric_machines import _1243
            
            return self._parent._cast(_1243.CADStator)

        @property
        def stator(self):
            from mastapy.electric_machines import _1289
            
            return self._parent._cast(_1289.Stator)

        @property
        def abstract_stator(self) -> 'AbstractStator':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractStator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def back_iron_inner_radius(self) -> 'float':
        """float: 'BackIronInnerRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BackIronInnerRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def back_iron_mid_radius(self) -> 'float':
        """float: 'BackIronMidRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BackIronMidRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_diameter_of_stator_teeth(self) -> 'float':
        """float: 'InnerDiameterOfStatorTeeth' is the original name of this property."""

        temp = self.wrapped.InnerDiameterOfStatorTeeth

        if temp is None:
            return 0.0

        return temp

    @inner_diameter_of_stator_teeth.setter
    def inner_diameter_of_stator_teeth(self, value: 'float'):
        self.wrapped.InnerDiameterOfStatorTeeth = float(value) if value else 0.0

    @property
    def mid_tooth_radius(self) -> 'float':
        """float: 'MidToothRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MidToothRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_slots(self) -> 'int':
        """int: 'NumberOfSlots' is the original name of this property."""

        temp = self.wrapped.NumberOfSlots

        if temp is None:
            return 0

        return temp

    @number_of_slots.setter
    def number_of_slots(self, value: 'int'):
        self.wrapped.NumberOfSlots = int(value) if value else 0

    @property
    def outer_diameter(self) -> 'float':
        """float: 'OuterDiameter' is the original name of this property."""

        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    def outer_diameter(self, value: 'float'):
        self.wrapped.OuterDiameter = float(value) if value else 0.0

    @property
    def outer_radius(self) -> 'float':
        """float: 'OuterRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def stator_length(self) -> 'float':
        """float: 'StatorLength' is the original name of this property."""

        temp = self.wrapped.StatorLength

        if temp is None:
            return 0.0

        return temp

    @stator_length.setter
    def stator_length(self, value: 'float'):
        self.wrapped.StatorLength = float(value) if value else 0.0

    @property
    def stator_material_database(self) -> 'str':
        """str: 'StatorMaterialDatabase' is the original name of this property."""

        temp = self.wrapped.StatorMaterialDatabase.SelectedItemName

        if temp is None:
            return ''

        return temp

    @stator_material_database.setter
    def stator_material_database(self, value: 'str'):
        self.wrapped.StatorMaterialDatabase.SetSelectedItem(str(value) if value else '')

    @property
    def tooth_and_slot(self) -> '_1238.AbstractToothAndSlot':
        """AbstractToothAndSlot: 'ToothAndSlot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothAndSlot

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def windings(self) -> '_1305.Windings':
        """Windings: 'Windings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Windings

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
    def cast_to(self) -> 'AbstractStator._Cast_AbstractStator':
        return self._Cast_AbstractStator(self)
