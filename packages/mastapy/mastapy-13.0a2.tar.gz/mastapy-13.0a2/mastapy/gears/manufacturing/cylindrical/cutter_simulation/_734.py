"""_734.py

GearCutterSimulation
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import (
    _726, _742, _729, _730
)
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_CUTTER_SIMULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'GearCutterSimulation')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCutterSimulation',)


class GearCutterSimulation(_0.APIBase):
    """GearCutterSimulation

    This is a mastapy class.
    """

    TYPE = _GEAR_CUTTER_SIMULATION

    class _Cast_GearCutterSimulation:
        """Special nested class for casting GearCutterSimulation to subclasses."""

        def __init__(self, parent: 'GearCutterSimulation'):
            self._parent = parent

        @property
        def finish_cutter_simulation(self):
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _731
            
            return self._parent._cast(_731.FinishCutterSimulation)

        @property
        def rough_cutter_simulation(self):
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _739
            
            return self._parent._cast(_739.RoughCutterSimulation)

        @property
        def gear_cutter_simulation(self) -> 'GearCutterSimulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCutterSimulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def highest_finished_form_diameter(self) -> 'float':
        """float: 'HighestFinishedFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HighestFinishedFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def least_sap_to_form_radius_clearance(self) -> 'float':
        """float: 'LeastSAPToFormRadiusClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeastSAPToFormRadiusClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def lowest_finished_tip_form_diameter(self) -> 'float':
        """float: 'LowestFinishedTipFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LowestFinishedTipFormDiameter

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
    def average_thickness(self) -> '_726.CutterSimulationCalc':
        """CutterSimulationCalc: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageThickness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def average_thickness_virtual(self) -> '_742.VirtualSimulationCalculator':
        """VirtualSimulationCalculator: 'AverageThicknessVirtual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageThicknessVirtual

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_thickness(self) -> '_726.CutterSimulationCalc':
        """CutterSimulationCalc: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumThickness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_thickness_virtual(self) -> '_742.VirtualSimulationCalculator':
        """VirtualSimulationCalculator: 'MaximumThicknessVirtual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumThicknessVirtual

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_thickness(self) -> '_726.CutterSimulationCalc':
        """CutterSimulationCalc: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumThickness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_thickness_virtual(self) -> '_742.VirtualSimulationCalculator':
        """VirtualSimulationCalculator: 'MinimumThicknessVirtual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumThicknessVirtual

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cutter_simulation(self) -> 'GearCutterSimulation':
        """GearCutterSimulation: 'CutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CutterSimulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def smallest_active_profile(self) -> '_726.CutterSimulationCalc':
        """CutterSimulationCalc: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestActiveProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_mesh_cutter_simulations(self) -> 'List[_729.CylindricalManufacturedRealGearInMesh]':
        """List[CylindricalManufacturedRealGearInMesh]: 'GearMeshCutterSimulations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshCutterSimulations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_mesh_cutter_simulations_virtual(self) -> 'List[_730.CylindricalManufacturedVirtualGearInMesh]':
        """List[CylindricalManufacturedVirtualGearInMesh]: 'GearMeshCutterSimulationsVirtual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshCutterSimulationsVirtual

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def thickness_calculators(self) -> 'List[_726.CutterSimulationCalc]':
        """List[CutterSimulationCalc]: 'ThicknessCalculators' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThicknessCalculators

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def virtual_thickness_calculators(self) -> 'List[_742.VirtualSimulationCalculator]':
        """List[VirtualSimulationCalculator]: 'VirtualThicknessCalculators' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualThicknessCalculators

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
    def cast_to(self) -> 'GearCutterSimulation._Cast_GearCutterSimulation':
        return self._Cast_GearCutterSimulation(self)
