"""_1986.py

LoadedBallBearingRaceResults
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2017
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BALL_BEARING_RACE_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedBallBearingRaceResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBallBearingRaceResults',)


class LoadedBallBearingRaceResults(_2017.LoadedRollingBearingRaceResults):
    """LoadedBallBearingRaceResults

    This is a mastapy class.
    """

    TYPE = _LOADED_BALL_BEARING_RACE_RESULTS

    class _Cast_LoadedBallBearingRaceResults:
        """Special nested class for casting LoadedBallBearingRaceResults to subclasses."""

        def __init__(self, parent: 'LoadedBallBearingRaceResults'):
            self._parent = parent

        @property
        def loaded_rolling_bearing_race_results(self):
            return self._parent._cast(_2017.LoadedRollingBearingRaceResults)

        @property
        def loaded_four_point_contact_ball_bearing_race_results(self):
            from mastapy.bearings.bearing_results.rolling import _2001
            
            return self._parent._cast(_2001.LoadedFourPointContactBallBearingRaceResults)

        @property
        def loaded_ball_bearing_race_results(self) -> 'LoadedBallBearingRaceResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedBallBearingRaceResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_radius_at_right_angles_to_rolling_direction(self) -> 'float':
        """float: 'ContactRadiusAtRightAnglesToRollingDirection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactRadiusAtRightAnglesToRollingDirection

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_highest_load(self) -> 'float':
        """float: 'HertzianSemiMajorDimensionHighestLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMajorDimensionHighestLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_highest_load(self) -> 'float':
        """float: 'HertzianSemiMinorDimensionHighestLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMinorDimensionHighestLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedBallBearingRaceResults._Cast_LoadedBallBearingRaceResults':
        return self._Cast_LoadedBallBearingRaceResults(self)
