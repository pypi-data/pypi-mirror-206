"""_1972.py

LoadedAngularContactThrustBallBearingRow
"""
from mastapy.bearings.bearing_results.rolling import _1971, _1969
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ANGULAR_CONTACT_THRUST_BALL_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedAngularContactThrustBallBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedAngularContactThrustBallBearingRow',)


class LoadedAngularContactThrustBallBearingRow(_1969.LoadedAngularContactBallBearingRow):
    """LoadedAngularContactThrustBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_ANGULAR_CONTACT_THRUST_BALL_BEARING_ROW

    class _Cast_LoadedAngularContactThrustBallBearingRow:
        """Special nested class for casting LoadedAngularContactThrustBallBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedAngularContactThrustBallBearingRow'):
            self._parent = parent

        @property
        def loaded_angular_contact_ball_bearing_row(self):
            return self._parent._cast(_1969.LoadedAngularContactBallBearingRow)

        @property
        def loaded_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1988
            
            return self._parent._cast(_1988.LoadedBallBearingRow)

        @property
        def loaded_rolling_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2019
            
            return self._parent._cast(_2019.LoadedRollingBearingRow)

        @property
        def loaded_angular_contact_thrust_ball_bearing_row(self) -> 'LoadedAngularContactThrustBallBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedAngularContactThrustBallBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_1971.LoadedAngularContactThrustBallBearingResults':
        """LoadedAngularContactThrustBallBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedAngularContactThrustBallBearingRow._Cast_LoadedAngularContactThrustBallBearingRow':
        return self._Cast_LoadedAngularContactThrustBallBearingRow(self)
