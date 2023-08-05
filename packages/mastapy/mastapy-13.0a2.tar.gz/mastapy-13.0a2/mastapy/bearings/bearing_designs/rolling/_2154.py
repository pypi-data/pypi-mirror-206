"""_2154.py

SphericalRollerBearing
"""
from mastapy.bearings.bearing_designs.rolling import _2127
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPHERICAL_ROLLER_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'SphericalRollerBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('SphericalRollerBearing',)


class SphericalRollerBearing(_2127.BarrelRollerBearing):
    """SphericalRollerBearing

    This is a mastapy class.
    """

    TYPE = _SPHERICAL_ROLLER_BEARING

    class _Cast_SphericalRollerBearing:
        """Special nested class for casting SphericalRollerBearing to subclasses."""

        def __init__(self, parent: 'SphericalRollerBearing'):
            self._parent = parent

        @property
        def barrel_roller_bearing(self):
            return self._parent._cast(_2127.BarrelRollerBearing)

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
        def spherical_roller_bearing(self) -> 'SphericalRollerBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SphericalRollerBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SphericalRollerBearing._Cast_SphericalRollerBearing':
        return self._Cast_SphericalRollerBearing(self)
