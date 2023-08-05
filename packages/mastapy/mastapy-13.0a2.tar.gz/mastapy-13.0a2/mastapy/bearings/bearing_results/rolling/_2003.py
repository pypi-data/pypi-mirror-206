"""_2003.py

LoadedFourPointContactBallBearingRow
"""
from typing import List

from mastapy.bearings.bearing_results.rolling import _2002, _2001, _1988
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedFourPointContactBallBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedFourPointContactBallBearingRow',)


class LoadedFourPointContactBallBearingRow(_1988.LoadedBallBearingRow):
    """LoadedFourPointContactBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ROW

    class _Cast_LoadedFourPointContactBallBearingRow:
        """Special nested class for casting LoadedFourPointContactBallBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedFourPointContactBallBearingRow'):
            self._parent = parent

        @property
        def loaded_ball_bearing_row(self):
            return self._parent._cast(_1988.LoadedBallBearingRow)

        @property
        def loaded_rolling_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2019
            
            return self._parent._cast(_2019.LoadedRollingBearingRow)

        @property
        def loaded_four_point_contact_ball_bearing_row(self) -> 'LoadedFourPointContactBallBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedFourPointContactBallBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_2002.LoadedFourPointContactBallBearingResults':
        """LoadedFourPointContactBallBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def race_results(self) -> 'List[_2001.LoadedFourPointContactBallBearingRaceResults]':
        """List[LoadedFourPointContactBallBearingRaceResults]: 'RaceResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'LoadedFourPointContactBallBearingRow._Cast_LoadedFourPointContactBallBearingRow':
        return self._Cast_LoadedFourPointContactBallBearingRow(self)
