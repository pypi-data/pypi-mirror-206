"""_2124.py

AxialThrustNeedleRollerBearing
"""
from mastapy.bearings.bearing_designs.rolling import _2123
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_THRUST_NEEDLE_ROLLER_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'AxialThrustNeedleRollerBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('AxialThrustNeedleRollerBearing',)


class AxialThrustNeedleRollerBearing(_2123.AxialThrustCylindricalRollerBearing):
    """AxialThrustNeedleRollerBearing

    This is a mastapy class.
    """

    TYPE = _AXIAL_THRUST_NEEDLE_ROLLER_BEARING

    class _Cast_AxialThrustNeedleRollerBearing:
        """Special nested class for casting AxialThrustNeedleRollerBearing to subclasses."""

        def __init__(self, parent: 'AxialThrustNeedleRollerBearing'):
            self._parent = parent

        @property
        def axial_thrust_cylindrical_roller_bearing(self):
            return self._parent._cast(_2123.AxialThrustCylindricalRollerBearing)

        @property
        def non_barrel_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2146
            
            return self._parent._cast(_2146.NonBarrelRollerBearing)

        @property
        def roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2147
            
            return self._parent._cast(_2147.RollerBearing)

        @property
        def rolling_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2150
            
            return self._parent._cast(_2150.RollingBearing)

        @property
        def detailed_bearing(self):
            from mastapy.bearings.bearing_designs import _2116
            
            return self._parent._cast(_2116.DetailedBearing)

        @property
        def non_linear_bearing(self):
            from mastapy.bearings.bearing_designs import _2119
            
            return self._parent._cast(_2119.NonLinearBearing)

        @property
        def bearing_design(self):
            from mastapy.bearings.bearing_designs import _2115
            
            return self._parent._cast(_2115.BearingDesign)

        @property
        def axial_thrust_needle_roller_bearing(self) -> 'AxialThrustNeedleRollerBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AxialThrustNeedleRollerBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AxialThrustNeedleRollerBearing._Cast_AxialThrustNeedleRollerBearing':
        return self._Cast_AxialThrustNeedleRollerBearing(self)
