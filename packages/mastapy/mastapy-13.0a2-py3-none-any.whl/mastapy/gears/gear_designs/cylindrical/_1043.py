"""_1043.py

GearSetManufacturingConfigurationSetup
"""
from typing import List

from mastapy.gears.gear_designs.cylindrical import _997, _1042
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_MANUFACTURING_CONFIGURATION_SETUP = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'GearSetManufacturingConfigurationSetup')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetManufacturingConfigurationSetup',)


class GearSetManufacturingConfigurationSetup(_0.APIBase):
    """GearSetManufacturingConfigurationSetup

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_MANUFACTURING_CONFIGURATION_SETUP

    class _Cast_GearSetManufacturingConfigurationSetup:
        """Special nested class for casting GearSetManufacturingConfigurationSetup to subclasses."""

        def __init__(self, parent: 'GearSetManufacturingConfigurationSetup'):
            self._parent = parent

        @property
        def gear_set_manufacturing_configuration_setup(self) -> 'GearSetManufacturingConfigurationSetup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetManufacturingConfigurationSetup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def create_new_suitable_cutters(self) -> '_997.CreateNewSuitableCutterOption':
        """CreateNewSuitableCutterOption: 'CreateNewSuitableCutters' is the original name of this property."""

        temp = self.wrapped.CreateNewSuitableCutters

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _997.CreateNewSuitableCutterOption)
        return constructor.new_from_mastapy_type(_997.CreateNewSuitableCutterOption)(value) if value is not None else None

    @create_new_suitable_cutters.setter
    def create_new_suitable_cutters(self, value: '_997.CreateNewSuitableCutterOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _997.CreateNewSuitableCutterOption.type_())
        self.wrapped.CreateNewSuitableCutters = value

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def use_as_design_mode_geometry(self) -> '_997.CreateNewSuitableCutterOption':
        """CreateNewSuitableCutterOption: 'UseAsDesignModeGeometry' is the original name of this property."""

        temp = self.wrapped.UseAsDesignModeGeometry

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _997.CreateNewSuitableCutterOption)
        return constructor.new_from_mastapy_type(_997.CreateNewSuitableCutterOption)(value) if value is not None else None

    @use_as_design_mode_geometry.setter
    def use_as_design_mode_geometry(self, value: '_997.CreateNewSuitableCutterOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _997.CreateNewSuitableCutterOption.type_())
        self.wrapped.UseAsDesignModeGeometry = value

    @property
    def gears(self) -> 'List[_1042.GearManufacturingConfigSetupViewModel]':
        """List[GearManufacturingConfigSetupViewModel]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

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
    def cast_to(self) -> 'GearSetManufacturingConfigurationSetup._Cast_GearSetManufacturingConfigurationSetup':
        return self._Cast_GearSetManufacturingConfigurationSetup(self)
