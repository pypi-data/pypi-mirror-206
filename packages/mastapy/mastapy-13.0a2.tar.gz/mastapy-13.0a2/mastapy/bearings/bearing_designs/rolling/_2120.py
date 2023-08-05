"""_2120.py

AngularContactBallBearing
"""
from mastapy.bearings.bearing_designs.rolling import _2125
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_CONTACT_BALL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'AngularContactBallBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('AngularContactBallBearing',)


class AngularContactBallBearing(_2125.BallBearing):
    """AngularContactBallBearing

    This is a mastapy class.
    """

    TYPE = _ANGULAR_CONTACT_BALL_BEARING

    class _Cast_AngularContactBallBearing:
        """Special nested class for casting AngularContactBallBearing to subclasses."""

        def __init__(self, parent: 'AngularContactBallBearing'):
            self._parent = parent

        @property
        def ball_bearing(self):
            return self._parent._cast(_2125.BallBearing)

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
        def angular_contact_thrust_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2121
            
            return self._parent._cast(_2121.AngularContactThrustBallBearing)

        @property
        def angular_contact_ball_bearing(self) -> 'AngularContactBallBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AngularContactBallBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AngularContactBallBearing._Cast_AngularContactBallBearing':
        return self._Cast_AngularContactBallBearing(self)
