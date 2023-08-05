"""_1414.py

DIN5466SplineRating
"""
from mastapy._internal import constructor
from mastapy.detailed_rigid_connectors.splines.ratings import _1420
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DIN5466_SPLINE_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings', 'DIN5466SplineRating')


__docformat__ = 'restructuredtext en'
__all__ = ('DIN5466SplineRating',)


class DIN5466SplineRating(_1420.SplineJointRating):
    """DIN5466SplineRating

    This is a mastapy class.
    """

    TYPE = _DIN5466_SPLINE_RATING

    class _Cast_DIN5466SplineRating:
        """Special nested class for casting DIN5466SplineRating to subclasses."""

        def __init__(self, parent: 'DIN5466SplineRating'):
            self._parent = parent

        @property
        def spline_joint_rating(self):
            return self._parent._cast(_1420.SplineJointRating)

        @property
        def shaft_hub_connection_rating(self):
            from mastapy.detailed_rigid_connectors.rating import _1424
            
            return self._parent._cast(_1424.ShaftHubConnectionRating)

        @property
        def din5466_spline_rating(self) -> 'DIN5466SplineRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DIN5466SplineRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def resultant_shear_force(self) -> 'float':
        """float: 'ResultantShearForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultantShearForce

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'DIN5466SplineRating._Cast_DIN5466SplineRating':
        return self._Cast_DIN5466SplineRating(self)
