"""_1413.py

DIN5466SplineHalfRating
"""
from mastapy.detailed_rigid_connectors.splines.ratings import _1419
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DIN5466_SPLINE_HALF_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings', 'DIN5466SplineHalfRating')


__docformat__ = 'restructuredtext en'
__all__ = ('DIN5466SplineHalfRating',)


class DIN5466SplineHalfRating(_1419.SplineHalfRating):
    """DIN5466SplineHalfRating

    This is a mastapy class.
    """

    TYPE = _DIN5466_SPLINE_HALF_RATING

    class _Cast_DIN5466SplineHalfRating:
        """Special nested class for casting DIN5466SplineHalfRating to subclasses."""

        def __init__(self, parent: 'DIN5466SplineHalfRating'):
            self._parent = parent

        @property
        def spline_half_rating(self):
            return self._parent._cast(_1419.SplineHalfRating)

        @property
        def din5466_spline_half_rating(self) -> 'DIN5466SplineHalfRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DIN5466SplineHalfRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DIN5466SplineHalfRating._Cast_DIN5466SplineHalfRating':
        return self._Cast_DIN5466SplineHalfRating(self)
