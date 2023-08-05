"""_1920.py

RollerBearingLundbergProfile
"""
from mastapy._internal import constructor
from mastapy.bearings.roller_bearing_profiles import _1921
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_LUNDBERG_PROFILE = python_net_import('SMT.MastaAPI.Bearings.RollerBearingProfiles', 'RollerBearingLundbergProfile')


__docformat__ = 'restructuredtext en'
__all__ = ('RollerBearingLundbergProfile',)


class RollerBearingLundbergProfile(_1921.RollerBearingProfile):
    """RollerBearingLundbergProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_LUNDBERG_PROFILE

    class _Cast_RollerBearingLundbergProfile:
        """Special nested class for casting RollerBearingLundbergProfile to subclasses."""

        def __init__(self, parent: 'RollerBearingLundbergProfile'):
            self._parent = parent

        @property
        def roller_bearing_profile(self):
            return self._parent._cast(_1921.RollerBearingProfile)

        @property
        def roller_bearing_lundberg_profile(self) -> 'RollerBearingLundbergProfile':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollerBearingLundbergProfile.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load(self) -> 'float':
        """float: 'Load' is the original name of this property."""

        temp = self.wrapped.Load

        if temp is None:
            return 0.0

        return temp

    @load.setter
    def load(self, value: 'float'):
        self.wrapped.Load = float(value) if value else 0.0

    @property
    def use_bearing_dynamic_capacity(self) -> 'bool':
        """bool: 'UseBearingDynamicCapacity' is the original name of this property."""

        temp = self.wrapped.UseBearingDynamicCapacity

        if temp is None:
            return False

        return temp

    @use_bearing_dynamic_capacity.setter
    def use_bearing_dynamic_capacity(self, value: 'bool'):
        self.wrapped.UseBearingDynamicCapacity = bool(value) if value else False

    @property
    def cast_to(self) -> 'RollerBearingLundbergProfile._Cast_RollerBearingLundbergProfile':
        return self._Cast_RollerBearingLundbergProfile(self)
