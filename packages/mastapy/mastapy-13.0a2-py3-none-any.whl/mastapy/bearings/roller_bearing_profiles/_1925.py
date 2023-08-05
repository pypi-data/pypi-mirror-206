"""_1925.py

UserSpecifiedRollerRaceProfilePoint
"""
from mastapy._internal import constructor
from mastapy.bearings.roller_bearing_profiles import _1923
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_USER_SPECIFIED_ROLLER_RACE_PROFILE_POINT = python_net_import('SMT.MastaAPI.Bearings.RollerBearingProfiles', 'UserSpecifiedRollerRaceProfilePoint')


__docformat__ = 'restructuredtext en'
__all__ = ('UserSpecifiedRollerRaceProfilePoint',)


class UserSpecifiedRollerRaceProfilePoint(_1923.RollerRaceProfilePoint):
    """UserSpecifiedRollerRaceProfilePoint

    This is a mastapy class.
    """

    TYPE = _USER_SPECIFIED_ROLLER_RACE_PROFILE_POINT

    class _Cast_UserSpecifiedRollerRaceProfilePoint:
        """Special nested class for casting UserSpecifiedRollerRaceProfilePoint to subclasses."""

        def __init__(self, parent: 'UserSpecifiedRollerRaceProfilePoint'):
            self._parent = parent

        @property
        def roller_race_profile_point(self):
            return self._parent._cast(_1923.RollerRaceProfilePoint)

        @property
        def user_specified_roller_race_profile_point(self) -> 'UserSpecifiedRollerRaceProfilePoint':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'UserSpecifiedRollerRaceProfilePoint.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def race_analysis_deviation(self) -> 'float':
        """float: 'RaceAnalysisDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceAnalysisDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def roller_analysis_deviation(self) -> 'float':
        """float: 'RollerAnalysisDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollerAnalysisDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'UserSpecifiedRollerRaceProfilePoint._Cast_UserSpecifiedRollerRaceProfilePoint':
        return self._Cast_UserSpecifiedRollerRaceProfilePoint(self)
