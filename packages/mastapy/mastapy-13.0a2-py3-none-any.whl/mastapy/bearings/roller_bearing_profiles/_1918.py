"""_1918.py

RollerBearingFlatProfile
"""
from mastapy.bearings.roller_bearing_profiles import _1921
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_FLAT_PROFILE = python_net_import('SMT.MastaAPI.Bearings.RollerBearingProfiles', 'RollerBearingFlatProfile')


__docformat__ = 'restructuredtext en'
__all__ = ('RollerBearingFlatProfile',)


class RollerBearingFlatProfile(_1921.RollerBearingProfile):
    """RollerBearingFlatProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_FLAT_PROFILE

    class _Cast_RollerBearingFlatProfile:
        """Special nested class for casting RollerBearingFlatProfile to subclasses."""

        def __init__(self, parent: 'RollerBearingFlatProfile'):
            self._parent = parent

        @property
        def roller_bearing_profile(self):
            return self._parent._cast(_1921.RollerBearingProfile)

        @property
        def roller_bearing_flat_profile(self) -> 'RollerBearingFlatProfile':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollerBearingFlatProfile.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RollerBearingFlatProfile._Cast_RollerBearingFlatProfile':
        return self._Cast_RollerBearingFlatProfile(self)
