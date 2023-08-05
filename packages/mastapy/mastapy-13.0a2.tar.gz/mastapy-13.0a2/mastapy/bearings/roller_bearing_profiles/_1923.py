"""_1923.py

RollerRaceProfilePoint
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_RACE_PROFILE_POINT = python_net_import('SMT.MastaAPI.Bearings.RollerBearingProfiles', 'RollerRaceProfilePoint')


__docformat__ = 'restructuredtext en'
__all__ = ('RollerRaceProfilePoint',)


class RollerRaceProfilePoint(_0.APIBase):
    """RollerRaceProfilePoint

    This is a mastapy class.
    """

    TYPE = _ROLLER_RACE_PROFILE_POINT

    class _Cast_RollerRaceProfilePoint:
        """Special nested class for casting RollerRaceProfilePoint to subclasses."""

        def __init__(self, parent: 'RollerRaceProfilePoint'):
            self._parent = parent

        @property
        def user_specified_roller_race_profile_point(self):
            from mastapy.bearings.roller_bearing_profiles import _1925
            
            return self._parent._cast(_1925.UserSpecifiedRollerRaceProfilePoint)

        @property
        def roller_race_profile_point(self) -> 'RollerRaceProfilePoint':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollerRaceProfilePoint.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset_from_roller_centre(self) -> 'float':
        """float: 'OffsetFromRollerCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OffsetFromRollerCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def race_deviation(self) -> 'float':
        """float: 'RaceDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def roller_deviation(self) -> 'float':
        """float: 'RollerDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollerDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def total_deviation(self) -> 'float':
        """float: 'TotalDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'RollerRaceProfilePoint._Cast_RollerRaceProfilePoint':
        return self._Cast_RollerRaceProfilePoint(self)
