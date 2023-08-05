"""_1095.py

CylindricalGearMicroGeometryBase
"""
from typing import List

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.utility.report import _1775
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1088, _1103
from mastapy.gears.gear_designs.cylindrical import _1007, _1020
from mastapy.gears.analysis import _1215
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_BASE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearMicroGeometryBase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroGeometryBase',)


class CylindricalGearMicroGeometryBase(_1215.GearImplementationDetail):
    """CylindricalGearMicroGeometryBase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_BASE

    class _Cast_CylindricalGearMicroGeometryBase:
        """Special nested class for casting CylindricalGearMicroGeometryBase to subclasses."""

        def __init__(self, parent: 'CylindricalGearMicroGeometryBase'):
            self._parent = parent

        @property
        def gear_implementation_detail(self):
            return self._parent._cast(_1215.GearImplementationDetail)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def cylindrical_gear_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1094
            
            return self._parent._cast(_1094.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1098
            
            return self._parent._cast(_1098.CylindricalGearMicroGeometryPerTooth)

        @property
        def cylindrical_gear_micro_geometry_base(self) -> 'CylindricalGearMicroGeometryBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroGeometryBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adjust_micro_geometry_for_analysis_when_including_pitch_errors(self) -> 'overridable.Overridable_bool':
        """overridable.Overridable_bool: 'AdjustMicroGeometryForAnalysisWhenIncludingPitchErrors' is the original name of this property."""

        temp = self.wrapped.AdjustMicroGeometryForAnalysisWhenIncludingPitchErrors

        if temp is None:
            return False

        return constructor.new_from_mastapy_type(overridable.Overridable_bool)(temp) if temp is not None else False

    @adjust_micro_geometry_for_analysis_when_including_pitch_errors.setter
    def adjust_micro_geometry_for_analysis_when_including_pitch_errors(self, value: 'overridable.Overridable_bool.implicit_type()'):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else False, is_overridden)
        self.wrapped.AdjustMicroGeometryForAnalysisWhenIncludingPitchErrors = value

    @property
    def lead_form_chart(self) -> '_1775.SimpleChartDefinition':
        """SimpleChartDefinition: 'LeadFormChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadFormChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_slope_chart(self) -> '_1775.SimpleChartDefinition':
        """SimpleChartDefinition: 'LeadSlopeChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadSlopeChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_total_nominal_chart(self) -> '_1775.SimpleChartDefinition':
        """SimpleChartDefinition: 'LeadTotalNominalChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadTotalNominalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_total_chart(self) -> '_1775.SimpleChartDefinition':
        """SimpleChartDefinition: 'LeadTotalChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadTotalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_control_point_is_user_specified(self) -> 'bool':
        """bool: 'ProfileControlPointIsUserSpecified' is the original name of this property."""

        temp = self.wrapped.ProfileControlPointIsUserSpecified

        if temp is None:
            return False

        return temp

    @profile_control_point_is_user_specified.setter
    def profile_control_point_is_user_specified(self, value: 'bool'):
        self.wrapped.ProfileControlPointIsUserSpecified = bool(value) if value else False

    @property
    def profile_form_10_percent_chart(self) -> '_1775.SimpleChartDefinition':
        """SimpleChartDefinition: 'ProfileForm10PercentChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileForm10PercentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_form_50_percent_chart(self) -> '_1775.SimpleChartDefinition':
        """SimpleChartDefinition: 'ProfileForm50PercentChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileForm50PercentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_form_90_percent_chart(self) -> '_1775.SimpleChartDefinition':
        """SimpleChartDefinition: 'ProfileForm90PercentChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileForm90PercentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_form_chart(self) -> '_1775.SimpleChartDefinition':
        """SimpleChartDefinition: 'ProfileFormChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_total_nominal_chart(self) -> '_1775.SimpleChartDefinition':
        """SimpleChartDefinition: 'ProfileTotalNominalChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileTotalNominalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_total_chart(self) -> '_1775.SimpleChartDefinition':
        """SimpleChartDefinition: 'ProfileTotalChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileTotalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def use_same_micro_geometry_on_both_flanks(self) -> 'bool':
        """bool: 'UseSameMicroGeometryOnBothFlanks' is the original name of this property."""

        temp = self.wrapped.UseSameMicroGeometryOnBothFlanks

        if temp is None:
            return False

        return temp

    @use_same_micro_geometry_on_both_flanks.setter
    def use_same_micro_geometry_on_both_flanks(self, value: 'bool'):
        self.wrapped.UseSameMicroGeometryOnBothFlanks = bool(value) if value else False

    @property
    def common_micro_geometry_of_left_flank(self) -> '_1088.CylindricalGearCommonFlankMicroGeometry':
        """CylindricalGearCommonFlankMicroGeometry: 'CommonMicroGeometryOfLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CommonMicroGeometryOfLeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def common_micro_geometry_of_right_flank(self) -> '_1088.CylindricalGearCommonFlankMicroGeometry':
        """CylindricalGearCommonFlankMicroGeometry: 'CommonMicroGeometryOfRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CommonMicroGeometryOfRightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear(self) -> '_1007.CylindricalGearDesign':
        """CylindricalGearDesign: 'CylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_control_point(self) -> '_1020.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'ProfileControlPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileControlPoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def common_micro_geometries_of_flanks(self) -> 'List[_1088.CylindricalGearCommonFlankMicroGeometry]':
        """List[CylindricalGearCommonFlankMicroGeometry]: 'CommonMicroGeometriesOfFlanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CommonMicroGeometriesOfFlanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def tooth_micro_geometries(self) -> 'List[_1103.CylindricalGearToothMicroGeometry]':
        """List[CylindricalGearToothMicroGeometry]: 'ToothMicroGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearMicroGeometryBase._Cast_CylindricalGearMicroGeometryBase':
        return self._Cast_CylindricalGearMicroGeometryBase(self)
