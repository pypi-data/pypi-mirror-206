"""_1408.py

StandardSplineJointDesign
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.detailed_rigid_connectors.splines import (
    _1391, _1392, _1393, _1403
)
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STANDARD_SPLINE_JOINT_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'StandardSplineJointDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('StandardSplineJointDesign',)


class StandardSplineJointDesign(_1403.SplineJointDesign):
    """StandardSplineJointDesign

    This is a mastapy class.
    """

    TYPE = _STANDARD_SPLINE_JOINT_DESIGN

    class _Cast_StandardSplineJointDesign:
        """Special nested class for casting StandardSplineJointDesign to subclasses."""

        def __init__(self, parent: 'StandardSplineJointDesign'):
            self._parent = parent

        @property
        def spline_joint_design(self):
            return self._parent._cast(_1403.SplineJointDesign)

        @property
        def detailed_rigid_connector_design(self):
            from mastapy.detailed_rigid_connectors import _1375
            
            return self._parent._cast(_1375.DetailedRigidConnectorDesign)

        @property
        def din5480_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1381
            
            return self._parent._cast(_1381.DIN5480SplineJointDesign)

        @property
        def gbt3478_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1385
            
            return self._parent._cast(_1385.GBT3478SplineJointDesign)

        @property
        def iso4156_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1388
            
            return self._parent._cast(_1388.ISO4156SplineJointDesign)

        @property
        def jisb1603_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1389
            
            return self._parent._cast(_1389.JISB1603SplineJointDesign)

        @property
        def sae_spline_joint_design(self):
            from mastapy.detailed_rigid_connectors.splines import _1396
            
            return self._parent._cast(_1396.SAESplineJointDesign)

        @property
        def standard_spline_joint_design(self) -> 'StandardSplineJointDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StandardSplineJointDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diametral_pitch(self) -> 'float':
        """float: 'DiametralPitch' is the original name of this property."""

        temp = self.wrapped.DiametralPitch

        if temp is None:
            return 0.0

        return temp

    @diametral_pitch.setter
    def diametral_pitch(self, value: 'float'):
        self.wrapped.DiametralPitch = float(value) if value else 0.0

    @property
    def module(self) -> 'float':
        """float: 'Module' is the original name of this property."""

        temp = self.wrapped.Module

        if temp is None:
            return 0.0

        return temp

    @module.setter
    def module(self, value: 'float'):
        self.wrapped.Module = float(value) if value else 0.0

    @property
    def module_preferred(self) -> 'enum_with_selected_value.EnumWithSelectedValue_Modules':
        """enum_with_selected_value.EnumWithSelectedValue_Modules: 'ModulePreferred' is the original name of this property."""

        temp = self.wrapped.ModulePreferred

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_Modules.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @module_preferred.setter
    def module_preferred(self, value: 'enum_with_selected_value.EnumWithSelectedValue_Modules.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_Modules.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ModulePreferred = value

    @property
    def module_from_preferred_series(self) -> 'bool':
        """bool: 'ModuleFromPreferredSeries' is the original name of this property."""

        temp = self.wrapped.ModuleFromPreferredSeries

        if temp is None:
            return False

        return temp

    @module_from_preferred_series.setter
    def module_from_preferred_series(self, value: 'bool'):
        self.wrapped.ModuleFromPreferredSeries = bool(value) if value else False

    @property
    def pressure_angle(self) -> 'float':
        """float: 'PressureAngle' is the original name of this property."""

        temp = self.wrapped.PressureAngle

        if temp is None:
            return 0.0

        return temp

    @pressure_angle.setter
    def pressure_angle(self, value: 'float'):
        self.wrapped.PressureAngle = float(value) if value else 0.0

    @property
    def pressure_angle_preferred(self) -> 'enum_with_selected_value.EnumWithSelectedValue_PressureAngleTypes':
        """enum_with_selected_value.EnumWithSelectedValue_PressureAngleTypes: 'PressureAnglePreferred' is the original name of this property."""

        temp = self.wrapped.PressureAnglePreferred

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_PressureAngleTypes.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @pressure_angle_preferred.setter
    def pressure_angle_preferred(self, value: 'enum_with_selected_value.EnumWithSelectedValue_PressureAngleTypes.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_PressureAngleTypes.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.PressureAnglePreferred = value

    @property
    def root_type(self) -> '_1393.RootTypes':
        """RootTypes: 'RootType' is the original name of this property."""

        temp = self.wrapped.RootType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1393.RootTypes)
        return constructor.new_from_mastapy_type(_1393.RootTypes)(value) if value is not None else None

    @root_type.setter
    def root_type(self, value: '_1393.RootTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1393.RootTypes.type_())
        self.wrapped.RootType = value

    @property
    def cast_to(self) -> 'StandardSplineJointDesign._Cast_StandardSplineJointDesign':
        return self._Cast_StandardSplineJointDesign(self)
