"""_2144.py

MultiPointContactBallBearing
"""
from mastapy.bearings.bearing_designs.rolling import _2125
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_POINT_CONTACT_BALL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'MultiPointContactBallBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('MultiPointContactBallBearing',)


class MultiPointContactBallBearing(_2125.BallBearing):
    """MultiPointContactBallBearing

    This is a mastapy class.
    """

    TYPE = _MULTI_POINT_CONTACT_BALL_BEARING

    class _Cast_MultiPointContactBallBearing:
        """Special nested class for casting MultiPointContactBallBearing to subclasses."""

        def __init__(self, parent: 'MultiPointContactBallBearing'):
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
        def four_point_contact_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2139
            
            return self._parent._cast(_2139.FourPointContactBallBearing)

        @property
        def three_point_contact_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2157
            
            return self._parent._cast(_2157.ThreePointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(self) -> 'MultiPointContactBallBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MultiPointContactBallBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MultiPointContactBallBearing._Cast_MultiPointContactBallBearing':
        return self._Cast_MultiPointContactBallBearing(self)
