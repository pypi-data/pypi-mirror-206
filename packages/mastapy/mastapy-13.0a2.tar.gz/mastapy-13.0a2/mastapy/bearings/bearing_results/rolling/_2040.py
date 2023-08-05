"""_2040.py

LoadedThrustBallBearingRow
"""
from mastapy.bearings.bearing_results.rolling import _2039, _1988
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_THRUST_BALL_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedThrustBallBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedThrustBallBearingRow',)


class LoadedThrustBallBearingRow(_1988.LoadedBallBearingRow):
    """LoadedThrustBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_THRUST_BALL_BEARING_ROW

    class _Cast_LoadedThrustBallBearingRow:
        """Special nested class for casting LoadedThrustBallBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedThrustBallBearingRow'):
            self._parent = parent

        @property
        def loaded_ball_bearing_row(self):
            return self._parent._cast(_1988.LoadedBallBearingRow)

        @property
        def loaded_rolling_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2019
            
            return self._parent._cast(_2019.LoadedRollingBearingRow)

        @property
        def loaded_thrust_ball_bearing_row(self) -> 'LoadedThrustBallBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedThrustBallBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_2039.LoadedThrustBallBearingResults':
        """LoadedThrustBallBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedThrustBallBearingRow._Cast_LoadedThrustBallBearingRow':
        return self._Cast_LoadedThrustBallBearingRow(self)
