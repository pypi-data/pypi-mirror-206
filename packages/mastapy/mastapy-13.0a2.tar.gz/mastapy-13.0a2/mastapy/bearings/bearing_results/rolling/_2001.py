"""_2001.py

LoadedFourPointContactBallBearingRaceResults
"""
from mastapy.bearings.bearing_results.rolling import _1986
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_FOUR_POINT_CONTACT_BALL_BEARING_RACE_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedFourPointContactBallBearingRaceResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedFourPointContactBallBearingRaceResults',)


class LoadedFourPointContactBallBearingRaceResults(_1986.LoadedBallBearingRaceResults):
    """LoadedFourPointContactBallBearingRaceResults

    This is a mastapy class.
    """

    TYPE = _LOADED_FOUR_POINT_CONTACT_BALL_BEARING_RACE_RESULTS

    class _Cast_LoadedFourPointContactBallBearingRaceResults:
        """Special nested class for casting LoadedFourPointContactBallBearingRaceResults to subclasses."""

        def __init__(self, parent: 'LoadedFourPointContactBallBearingRaceResults'):
            self._parent = parent

        @property
        def loaded_ball_bearing_race_results(self):
            return self._parent._cast(_1986.LoadedBallBearingRaceResults)

        @property
        def loaded_rolling_bearing_race_results(self):
            from mastapy.bearings.bearing_results.rolling import _2017
            
            return self._parent._cast(_2017.LoadedRollingBearingRaceResults)

        @property
        def loaded_four_point_contact_ball_bearing_race_results(self) -> 'LoadedFourPointContactBallBearingRaceResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedFourPointContactBallBearingRaceResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedFourPointContactBallBearingRaceResults._Cast_LoadedFourPointContactBallBearingRaceResults':
        return self._Cast_LoadedFourPointContactBallBearingRaceResults(self)
