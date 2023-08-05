"""_1995.py

LoadedCylindricalRollerBearingRow
"""
from mastapy.bearings.bearing_results.rolling import _1994, _2010
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CYLINDRICAL_ROLLER_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedCylindricalRollerBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedCylindricalRollerBearingRow',)


class LoadedCylindricalRollerBearingRow(_2010.LoadedNonBarrelRollerBearingRow):
    """LoadedCylindricalRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_CYLINDRICAL_ROLLER_BEARING_ROW

    class _Cast_LoadedCylindricalRollerBearingRow:
        """Special nested class for casting LoadedCylindricalRollerBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedCylindricalRollerBearingRow'):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_row(self):
            return self._parent._cast(_2010.LoadedNonBarrelRollerBearingRow)

        @property
        def loaded_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2015
            
            return self._parent._cast(_2015.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2019
            
            return self._parent._cast(_2019.LoadedRollingBearingRow)

        @property
        def loaded_needle_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2007
            
            return self._parent._cast(_2007.LoadedNeedleRollerBearingRow)

        @property
        def loaded_cylindrical_roller_bearing_row(self) -> 'LoadedCylindricalRollerBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedCylindricalRollerBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_1994.LoadedCylindricalRollerBearingResults':
        """LoadedCylindricalRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedCylindricalRollerBearingRow._Cast_LoadedCylindricalRollerBearingRow':
        return self._Cast_LoadedCylindricalRollerBearingRow(self)
