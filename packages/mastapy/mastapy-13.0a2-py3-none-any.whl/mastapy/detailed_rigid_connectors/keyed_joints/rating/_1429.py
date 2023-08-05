"""_1429.py

KeywayHalfRating
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KEYWAY_HALF_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.KeyedJoints.Rating', 'KeywayHalfRating')


__docformat__ = 'restructuredtext en'
__all__ = ('KeywayHalfRating',)


class KeywayHalfRating(_0.APIBase):
    """KeywayHalfRating

    This is a mastapy class.
    """

    TYPE = _KEYWAY_HALF_RATING

    class _Cast_KeywayHalfRating:
        """Special nested class for casting KeywayHalfRating to subclasses."""

        def __init__(self, parent: 'KeywayHalfRating'):
            self._parent = parent

        @property
        def keyway_half_rating(self) -> 'KeywayHalfRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KeywayHalfRating.TYPE'):
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
    def cast_to(self) -> 'KeywayHalfRating._Cast_KeywayHalfRating':
        return self._Cast_KeywayHalfRating(self)
