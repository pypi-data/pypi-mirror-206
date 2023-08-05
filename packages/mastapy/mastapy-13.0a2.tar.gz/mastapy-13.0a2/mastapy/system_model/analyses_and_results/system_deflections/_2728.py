"""_2728.py

CylindricalMeshedGearSystemDeflection
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2727, _2724, _2718
from mastapy.gears.ltca import _840
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESHED_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CylindricalMeshedGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalMeshedGearSystemDeflection',)


class CylindricalMeshedGearSystemDeflection(_0.APIBase):
    """CylindricalMeshedGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESHED_GEAR_SYSTEM_DEFLECTION

    class _Cast_CylindricalMeshedGearSystemDeflection:
        """Special nested class for casting CylindricalMeshedGearSystemDeflection to subclasses."""

        def __init__(self, parent: 'CylindricalMeshedGearSystemDeflection'):
            self._parent = parent

        @property
        def cylindrical_meshed_gear_system_deflection(self) -> 'CylindricalMeshedGearSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalMeshedGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def change_in_operating_pitch_diameter_due_to_thermal_effects(self) -> 'float':
        """float: 'ChangeInOperatingPitchDiameterDueToThermalEffects' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ChangeInOperatingPitchDiameterDueToThermalEffects

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_operating_tip_clearance(self) -> 'float':
        """float: 'MinimumOperatingTipClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumOperatingTipClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def operating_tip_diameter(self) -> 'float':
        """float: 'OperatingTipDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OperatingTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tilt_x(self) -> 'float':
        """float: 'TiltX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TiltX

        if temp is None:
            return 0.0

        return temp

    @property
    def tilt_y(self) -> 'float':
        """float: 'TiltY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TiltY

        if temp is None:
            return 0.0

        return temp

    @property
    def left_flank(self) -> '_2727.CylindricalMeshedGearFlankSystemDeflection':
        """CylindricalMeshedGearFlankSystemDeflection: 'LeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank(self) -> '_2727.CylindricalMeshedGearFlankSystemDeflection':
        """CylindricalMeshedGearFlankSystemDeflection: 'RightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compression_side_fillet_results(self) -> 'List[_840.GearRootFilletStressResults]':
        """List[GearRootFilletStressResults]: 'CompressionSideFilletResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompressionSideFilletResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def flanks(self) -> 'List[_2727.CylindricalMeshedGearFlankSystemDeflection]':
        """List[CylindricalMeshedGearFlankSystemDeflection]: 'Flanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Flanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def tension_side_fillet_results(self) -> 'List[_840.GearRootFilletStressResults]':
        """List[GearRootFilletStressResults]: 'TensionSideFilletResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TensionSideFilletResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def both_flanks(self) -> '_2727.CylindricalMeshedGearFlankSystemDeflection':
        """CylindricalMeshedGearFlankSystemDeflection: 'BothFlanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BothFlanks

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_system_deflection(self) -> '_2724.CylindricalGearSystemDeflection':
        """CylindricalGearSystemDeflection: 'CylindricalGearSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_mesh_system_deflection(self) -> '_2718.CylindricalGearMeshSystemDeflection':
        """CylindricalGearMeshSystemDeflection: 'CylindricalGearMeshSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMeshSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def other_cylindrical_gear_system_deflection(self) -> '_2724.CylindricalGearSystemDeflection':
        """CylindricalGearSystemDeflection: 'OtherCylindricalGearSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OtherCylindricalGearSystemDeflection

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
    def cast_to(self) -> 'CylindricalMeshedGearSystemDeflection._Cast_CylindricalMeshedGearSystemDeflection':
        return self._Cast_CylindricalMeshedGearSystemDeflection(self)
