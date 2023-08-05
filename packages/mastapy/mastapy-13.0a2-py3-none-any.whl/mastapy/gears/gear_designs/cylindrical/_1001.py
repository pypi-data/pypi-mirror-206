"""_1001.py

CylindricalGearAbstractRack
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.cylindrical import _1007, _1002
from mastapy.gears.manufacturing.cylindrical.cutters import _709
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ABSTRACT_RACK = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearAbstractRack')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearAbstractRack',)


class CylindricalGearAbstractRack(_0.APIBase):
    """CylindricalGearAbstractRack

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ABSTRACT_RACK

    class _Cast_CylindricalGearAbstractRack:
        """Special nested class for casting CylindricalGearAbstractRack to subclasses."""

        def __init__(self, parent: 'CylindricalGearAbstractRack'):
            self._parent = parent

        @property
        def cylindrical_gear_basic_rack(self):
            from mastapy.gears.gear_designs.cylindrical import _1003
            
            return self._parent._cast(_1003.CylindricalGearBasicRack)

        @property
        def cylindrical_gear_pinion_type_cutter(self):
            from mastapy.gears.gear_designs.cylindrical import _1018
            
            return self._parent._cast(_1018.CylindricalGearPinionTypeCutter)

        @property
        def standard_rack(self):
            from mastapy.gears.gear_designs.cylindrical import _1070
            
            return self._parent._cast(_1070.StandardRack)

        @property
        def cylindrical_gear_abstract_rack(self) -> 'CylindricalGearAbstractRack':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearAbstractRack.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_rack_addendum_factor(self) -> 'float':
        """float: 'BasicRackAddendumFactor' is the original name of this property."""

        temp = self.wrapped.BasicRackAddendumFactor

        if temp is None:
            return 0.0

        return temp

    @basic_rack_addendum_factor.setter
    def basic_rack_addendum_factor(self, value: 'float'):
        self.wrapped.BasicRackAddendumFactor = float(value) if value else 0.0

    @property
    def basic_rack_dedendum_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'BasicRackDedendumFactor' is the original name of this property."""

        temp = self.wrapped.BasicRackDedendumFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @basic_rack_dedendum_factor.setter
    def basic_rack_dedendum_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.BasicRackDedendumFactor = value

    @property
    def basic_rack_tip_thickness(self) -> 'float':
        """float: 'BasicRackTipThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicRackTipThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rack_tooth_depth_factor(self) -> 'float':
        """float: 'BasicRackToothDepthFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicRackToothDepthFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_tip_width_normal_module(self) -> 'float':
        """float: 'CutterTipWidthNormalModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CutterTipWidthNormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_possible_cutter_edge_radius(self) -> 'float':
        """float: 'MaximumPossibleCutterEdgeRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPossibleCutterEdgeRadius

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
    def use_maximum_edge_radius(self) -> 'bool':
        """bool: 'UseMaximumEdgeRadius' is the original name of this property."""

        temp = self.wrapped.UseMaximumEdgeRadius

        if temp is None:
            return False

        return temp

    @use_maximum_edge_radius.setter
    def use_maximum_edge_radius(self, value: 'bool'):
        self.wrapped.UseMaximumEdgeRadius = bool(value) if value else False

    @property
    def gear(self) -> '_1007.CylindricalGearDesign':
        """CylindricalGearDesign: 'Gear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_flank(self) -> '_1002.CylindricalGearAbstractRackFlank':
        """CylindricalGearAbstractRackFlank: 'LeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank(self) -> '_1002.CylindricalGearAbstractRackFlank':
        """CylindricalGearAbstractRackFlank: 'RightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaper_for_agma_rating(self) -> '_709.CylindricalGearShaper':
        """CylindricalGearShaper: 'ShaperForAGMARating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaperForAGMARating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def flanks(self) -> 'List[_1002.CylindricalGearAbstractRackFlank]':
        """List[CylindricalGearAbstractRackFlank]: 'Flanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Flanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def both_flanks(self) -> '_1002.CylindricalGearAbstractRackFlank':
        """CylindricalGearAbstractRackFlank: 'BothFlanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BothFlanks

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
    def cast_to(self) -> 'CylindricalGearAbstractRack._Cast_CylindricalGearAbstractRack':
        return self._Cast_CylindricalGearAbstractRack(self)
