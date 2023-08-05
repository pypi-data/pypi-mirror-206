"""_2022.py

LoadedSelfAligningBallBearingRow
"""
from mastapy.bearings.bearing_results.rolling import _2021, _1988
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SELF_ALIGNING_BALL_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedSelfAligningBallBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedSelfAligningBallBearingRow',)


class LoadedSelfAligningBallBearingRow(_1988.LoadedBallBearingRow):
    """LoadedSelfAligningBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_SELF_ALIGNING_BALL_BEARING_ROW

    class _Cast_LoadedSelfAligningBallBearingRow:
        """Special nested class for casting LoadedSelfAligningBallBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedSelfAligningBallBearingRow'):
            self._parent = parent

        @property
        def loaded_ball_bearing_row(self):
            return self._parent._cast(_1988.LoadedBallBearingRow)

        @property
        def loaded_rolling_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2019
            
            return self._parent._cast(_2019.LoadedRollingBearingRow)

        @property
        def loaded_self_aligning_ball_bearing_row(self) -> 'LoadedSelfAligningBallBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedSelfAligningBallBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_2021.LoadedSelfAligningBallBearingResults':
        """LoadedSelfAligningBallBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedSelfAligningBallBearingRow._Cast_LoadedSelfAligningBallBearingRow':
        return self._Cast_LoadedSelfAligningBallBearingRow(self)
