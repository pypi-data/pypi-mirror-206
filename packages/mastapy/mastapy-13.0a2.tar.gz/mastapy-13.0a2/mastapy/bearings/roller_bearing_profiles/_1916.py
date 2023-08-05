"""_1916.py

RollerBearingCrownedProfile
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.bearings.roller_bearing_profiles import _1921
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_CROWNED_PROFILE = python_net_import('SMT.MastaAPI.Bearings.RollerBearingProfiles', 'RollerBearingCrownedProfile')


__docformat__ = 'restructuredtext en'
__all__ = ('RollerBearingCrownedProfile',)


class RollerBearingCrownedProfile(_1921.RollerBearingProfile):
    """RollerBearingCrownedProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_CROWNED_PROFILE

    class _Cast_RollerBearingCrownedProfile:
        """Special nested class for casting RollerBearingCrownedProfile to subclasses."""

        def __init__(self, parent: 'RollerBearingCrownedProfile'):
            self._parent = parent

        @property
        def roller_bearing_profile(self):
            return self._parent._cast(_1921.RollerBearingProfile)

        @property
        def roller_bearing_crowned_profile(self) -> 'RollerBearingCrownedProfile':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollerBearingCrownedProfile.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crown_end_drop(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CrownEndDrop' is the original name of this property."""

        temp = self.wrapped.CrownEndDrop

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @crown_end_drop.setter
    def crown_end_drop(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CrownEndDrop = value

    @property
    def crown_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CrownRadius' is the original name of this property."""

        temp = self.wrapped.CrownRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @crown_radius.setter
    def crown_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CrownRadius = value

    @property
    def offset(self) -> 'float':
        """float: 'Offset' is the original name of this property."""

        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    def offset(self, value: 'float'):
        self.wrapped.Offset = float(value) if value else 0.0

    @property
    def parallel_length(self) -> 'float':
        """float: 'ParallelLength' is the original name of this property."""

        temp = self.wrapped.ParallelLength

        if temp is None:
            return 0.0

        return temp

    @parallel_length.setter
    def parallel_length(self, value: 'float'):
        self.wrapped.ParallelLength = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'RollerBearingCrownedProfile._Cast_RollerBearingCrownedProfile':
        return self._Cast_RollerBearingCrownedProfile(self)
