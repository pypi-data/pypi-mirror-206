"""_1969.py

LoadedAngularContactBallBearingRow
"""
from mastapy.bearings.bearing_results.rolling import _1968, _1988
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ANGULAR_CONTACT_BALL_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedAngularContactBallBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedAngularContactBallBearingRow',)


class LoadedAngularContactBallBearingRow(_1988.LoadedBallBearingRow):
    """LoadedAngularContactBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_ANGULAR_CONTACT_BALL_BEARING_ROW

    class _Cast_LoadedAngularContactBallBearingRow:
        """Special nested class for casting LoadedAngularContactBallBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedAngularContactBallBearingRow'):
            self._parent = parent

        @property
        def loaded_ball_bearing_row(self):
            return self._parent._cast(_1988.LoadedBallBearingRow)

        @property
        def loaded_rolling_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2019
            
            return self._parent._cast(_2019.LoadedRollingBearingRow)

        @property
        def loaded_angular_contact_thrust_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1972
            
            return self._parent._cast(_1972.LoadedAngularContactThrustBallBearingRow)

        @property
        def loaded_angular_contact_ball_bearing_row(self) -> 'LoadedAngularContactBallBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedAngularContactBallBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_1968.LoadedAngularContactBallBearingResults':
        """LoadedAngularContactBallBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedAngularContactBallBearingRow._Cast_LoadedAngularContactBallBearingRow':
        return self._Cast_LoadedAngularContactBallBearingRow(self)
