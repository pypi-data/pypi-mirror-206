"""_1921.py

RollerBearingProfile
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_PROFILE = python_net_import('SMT.MastaAPI.Bearings.RollerBearingProfiles', 'RollerBearingProfile')


__docformat__ = 'restructuredtext en'
__all__ = ('RollerBearingProfile',)


class RollerBearingProfile(_0.APIBase):
    """RollerBearingProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_PROFILE

    class _Cast_RollerBearingProfile:
        """Special nested class for casting RollerBearingProfile to subclasses."""

        def __init__(self, parent: 'RollerBearingProfile'):
            self._parent = parent

        @property
        def roller_bearing_conical_profile(self):
            from mastapy.bearings.roller_bearing_profiles import _1915
            
            return self._parent._cast(_1915.RollerBearingConicalProfile)

        @property
        def roller_bearing_crowned_profile(self):
            from mastapy.bearings.roller_bearing_profiles import _1916
            
            return self._parent._cast(_1916.RollerBearingCrownedProfile)

        @property
        def roller_bearing_din_lundberg_profile(self):
            from mastapy.bearings.roller_bearing_profiles import _1917
            
            return self._parent._cast(_1917.RollerBearingDinLundbergProfile)

        @property
        def roller_bearing_flat_profile(self):
            from mastapy.bearings.roller_bearing_profiles import _1918
            
            return self._parent._cast(_1918.RollerBearingFlatProfile)

        @property
        def roller_bearing_johns_gohar_profile(self):
            from mastapy.bearings.roller_bearing_profiles import _1919
            
            return self._parent._cast(_1919.RollerBearingJohnsGoharProfile)

        @property
        def roller_bearing_lundberg_profile(self):
            from mastapy.bearings.roller_bearing_profiles import _1920
            
            return self._parent._cast(_1920.RollerBearingLundbergProfile)

        @property
        def roller_bearing_user_specified_profile(self):
            from mastapy.bearings.roller_bearing_profiles import _1922
            
            return self._parent._cast(_1922.RollerBearingUserSpecifiedProfile)

        @property
        def roller_bearing_profile(self) -> 'RollerBearingProfile':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollerBearingProfile.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def covers_two_rows_of_elements(self) -> 'bool':
        """bool: 'CoversTwoRowsOfElements' is the original name of this property."""

        temp = self.wrapped.CoversTwoRowsOfElements

        if temp is None:
            return False

        return temp

    @covers_two_rows_of_elements.setter
    def covers_two_rows_of_elements(self, value: 'bool'):
        self.wrapped.CoversTwoRowsOfElements = bool(value) if value else False

    @property
    def cast_to(self) -> 'RollerBearingProfile._Cast_RollerBearingProfile':
        return self._Cast_RollerBearingProfile(self)
