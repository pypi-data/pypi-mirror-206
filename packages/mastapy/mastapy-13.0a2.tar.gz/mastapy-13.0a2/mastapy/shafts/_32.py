"""_32.py

ShaftProfilePointCopy
"""
from mastapy.shafts import _31
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_PROFILE_POINT_COPY = python_net_import('SMT.MastaAPI.Shafts', 'ShaftProfilePointCopy')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftProfilePointCopy',)


class ShaftProfilePointCopy(_31.ShaftProfilePoint):
    """ShaftProfilePointCopy

    This is a mastapy class.
    """

    TYPE = _SHAFT_PROFILE_POINT_COPY

    class _Cast_ShaftProfilePointCopy:
        """Special nested class for casting ShaftProfilePointCopy to subclasses."""

        def __init__(self, parent: 'ShaftProfilePointCopy'):
            self._parent = parent

        @property
        def shaft_profile_point(self):
            return self._parent._cast(_31.ShaftProfilePoint)

        @property
        def shaft_profile_point_copy(self) -> 'ShaftProfilePointCopy':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftProfilePointCopy.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ShaftProfilePointCopy._Cast_ShaftProfilePointCopy':
        return self._Cast_ShaftProfilePointCopy(self)
