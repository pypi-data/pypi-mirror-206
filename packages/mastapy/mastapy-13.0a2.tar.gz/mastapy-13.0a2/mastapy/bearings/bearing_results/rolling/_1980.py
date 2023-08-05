"""_1980.py

LoadedAxialThrustCylindricalRollerBearingRow
"""
from mastapy.bearings.bearing_results.rolling import _1979, _2010
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedAxialThrustCylindricalRollerBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedAxialThrustCylindricalRollerBearingRow',)


class LoadedAxialThrustCylindricalRollerBearingRow(_2010.LoadedNonBarrelRollerBearingRow):
    """LoadedAxialThrustCylindricalRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_ROW

    class _Cast_LoadedAxialThrustCylindricalRollerBearingRow:
        """Special nested class for casting LoadedAxialThrustCylindricalRollerBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedAxialThrustCylindricalRollerBearingRow'):
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
        def loaded_axial_thrust_needle_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1983
            
            return self._parent._cast(_1983.LoadedAxialThrustNeedleRollerBearingRow)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_row(self) -> 'LoadedAxialThrustCylindricalRollerBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedAxialThrustCylindricalRollerBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_1979.LoadedAxialThrustCylindricalRollerBearingResults':
        """LoadedAxialThrustCylindricalRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow':
        return self._Cast_LoadedAxialThrustCylindricalRollerBearingRow(self)
