"""_724.py

NamedPoint
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_POINT = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles', 'NamedPoint')


__docformat__ = 'restructuredtext en'
__all__ = ('NamedPoint',)


class NamedPoint(_0.APIBase):
    """NamedPoint

    This is a mastapy class.
    """

    TYPE = _NAMED_POINT

    class _Cast_NamedPoint:
        """Special nested class for casting NamedPoint to subclasses."""

        def __init__(self, parent: 'NamedPoint'):
            self._parent = parent

        @property
        def named_point(self) -> 'NamedPoint':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NamedPoint.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def x(self) -> 'float':
        """float: 'X' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.X

        if temp is None:
            return 0.0

        return temp

    @property
    def y(self) -> 'float':
        """float: 'Y' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Y

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'NamedPoint._Cast_NamedPoint':
        return self._Cast_NamedPoint(self)
