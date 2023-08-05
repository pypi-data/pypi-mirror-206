"""_2043.py

LoadedToroidalRollerBearingRow
"""
from mastapy.bearings.bearing_results.rolling import _2042, _2015
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TOROIDAL_ROLLER_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedToroidalRollerBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedToroidalRollerBearingRow',)


class LoadedToroidalRollerBearingRow(_2015.LoadedRollerBearingRow):
    """LoadedToroidalRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_TOROIDAL_ROLLER_BEARING_ROW

    class _Cast_LoadedToroidalRollerBearingRow:
        """Special nested class for casting LoadedToroidalRollerBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedToroidalRollerBearingRow'):
            self._parent = parent

        @property
        def loaded_roller_bearing_row(self):
            return self._parent._cast(_2015.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2019
            
            return self._parent._cast(_2019.LoadedRollingBearingRow)

        @property
        def loaded_toroidal_roller_bearing_row(self) -> 'LoadedToroidalRollerBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedToroidalRollerBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_2042.LoadedToroidalRollerBearingResults':
        """LoadedToroidalRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedToroidalRollerBearingRow._Cast_LoadedToroidalRollerBearingRow':
        return self._Cast_LoadedToroidalRollerBearingRow(self)
