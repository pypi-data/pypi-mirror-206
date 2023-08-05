"""_1953.py

BallBearingRaceContactGeometry
"""
from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BALL_BEARING_RACE_CONTACT_GEOMETRY = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'BallBearingRaceContactGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('BallBearingRaceContactGeometry',)


class BallBearingRaceContactGeometry(_0.APIBase):
    """BallBearingRaceContactGeometry

    This is a mastapy class.
    """

    TYPE = _BALL_BEARING_RACE_CONTACT_GEOMETRY

    class _Cast_BallBearingRaceContactGeometry:
        """Special nested class for casting BallBearingRaceContactGeometry to subclasses."""

        def __init__(self, parent: 'BallBearingRaceContactGeometry'):
            self._parent = parent

        @property
        def ball_bearing_race_contact_geometry(self) -> 'BallBearingRaceContactGeometry':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BallBearingRaceContactGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ball_diameter(self) -> 'float':
        """float: 'BallDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BallDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def race_groove_radius(self) -> 'float':
        """float: 'RaceGrooveRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceGrooveRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def ball_centre(self) -> 'Vector2D':
        """Vector2D: 'BallCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BallCentre

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def race_centre(self) -> 'Vector2D':
        """Vector2D: 'RaceCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceCentre

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def cast_to(self) -> 'BallBearingRaceContactGeometry._Cast_BallBearingRaceContactGeometry':
        return self._Cast_BallBearingRaceContactGeometry(self)
