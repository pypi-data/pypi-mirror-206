"""_2010.py

LoadedNonBarrelRollerBearingRow
"""
from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2009, _2015
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedNonBarrelRollerBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedNonBarrelRollerBearingRow',)


class LoadedNonBarrelRollerBearingRow(_2015.LoadedRollerBearingRow):
    """LoadedNonBarrelRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_BARREL_ROLLER_BEARING_ROW

    class _Cast_LoadedNonBarrelRollerBearingRow:
        """Special nested class for casting LoadedNonBarrelRollerBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedNonBarrelRollerBearingRow'):
            self._parent = parent

        @property
        def loaded_roller_bearing_row(self):
            return self._parent._cast(_2015.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2019
            
            return self._parent._cast(_2019.LoadedRollingBearingRow)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1980
            
            return self._parent._cast(_1980.LoadedAxialThrustCylindricalRollerBearingRow)

        @property
        def loaded_axial_thrust_needle_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1983
            
            return self._parent._cast(_1983.LoadedAxialThrustNeedleRollerBearingRow)

        @property
        def loaded_cylindrical_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1995
            
            return self._parent._cast(_1995.LoadedCylindricalRollerBearingRow)

        @property
        def loaded_needle_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2007
            
            return self._parent._cast(_2007.LoadedNeedleRollerBearingRow)

        @property
        def loaded_taper_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2034
            
            return self._parent._cast(_2034.LoadedTaperRollerBearingRow)

        @property
        def loaded_non_barrel_roller_bearing_row(self) -> 'LoadedNonBarrelRollerBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedNonBarrelRollerBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rib_normal_contact_stress_inner_left(self) -> 'Image':
        """Image: 'RibNormalContactStressInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RibNormalContactStressInnerLeft

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def rib_normal_contact_stress_inner_right(self) -> 'Image':
        """Image: 'RibNormalContactStressInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RibNormalContactStressInnerRight

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def rib_normal_contact_stress_outer_left(self) -> 'Image':
        """Image: 'RibNormalContactStressOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RibNormalContactStressOuterLeft

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def rib_normal_contact_stress_outer_right(self) -> 'Image':
        """Image: 'RibNormalContactStressOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RibNormalContactStressOuterRight

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def loaded_bearing(self) -> '_2009.LoadedNonBarrelRollerBearingResults':
        """LoadedNonBarrelRollerBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow':
        return self._Cast_LoadedNonBarrelRollerBearingRow(self)
