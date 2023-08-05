"""_1917.py

RollerBearingDinLundbergProfile
"""
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.math_utility import _1498
from mastapy.bearings.roller_bearing_profiles import _1921
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_DIN_LUNDBERG_PROFILE = python_net_import('SMT.MastaAPI.Bearings.RollerBearingProfiles', 'RollerBearingDinLundbergProfile')


__docformat__ = 'restructuredtext en'
__all__ = ('RollerBearingDinLundbergProfile',)


class RollerBearingDinLundbergProfile(_1921.RollerBearingProfile):
    """RollerBearingDinLundbergProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_DIN_LUNDBERG_PROFILE

    class _Cast_RollerBearingDinLundbergProfile:
        """Special nested class for casting RollerBearingDinLundbergProfile to subclasses."""

        def __init__(self, parent: 'RollerBearingDinLundbergProfile'):
            self._parent = parent

        @property
        def roller_bearing_profile(self):
            return self._parent._cast(_1921.RollerBearingProfile)

        @property
        def roller_bearing_din_lundberg_profile(self) -> 'RollerBearingDinLundbergProfile':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollerBearingDinLundbergProfile.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_offset(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AxialOffset' is the original name of this property."""

        temp = self.wrapped.AxialOffset

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @axial_offset.setter
    def axial_offset(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AxialOffset = value

    @property
    def effective_length(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'EffectiveLength' is the original name of this property."""

        temp = self.wrapped.EffectiveLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @effective_length.setter
    def effective_length(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.EffectiveLength = value

    @property
    def extrapolation_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions':
        """enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions: 'ExtrapolationMethod' is the original name of this property."""

        temp = self.wrapped.ExtrapolationMethod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @extrapolation_method.setter
    def extrapolation_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ExtrapolationMethod = value

    @property
    def cast_to(self) -> 'RollerBearingDinLundbergProfile._Cast_RollerBearingDinLundbergProfile':
        return self._Cast_RollerBearingDinLundbergProfile(self)
