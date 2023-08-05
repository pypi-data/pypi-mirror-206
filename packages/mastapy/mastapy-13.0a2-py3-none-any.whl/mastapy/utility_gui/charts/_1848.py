"""_1848.py

Series2D
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SERIES_2D = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'Series2D')


__docformat__ = 'restructuredtext en'
__all__ = ('Series2D',)


class Series2D(_0.APIBase):
    """Series2D

    This is a mastapy class.
    """

    TYPE = _SERIES_2D

    class _Cast_Series2D:
        """Special nested class for casting Series2D to subclasses."""

        def __init__(self, parent: 'Series2D'):
            self._parent = parent

        @property
        def series_2d(self) -> 'Series2D':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Series2D.TYPE'):
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
    def points(self) -> 'List[Vector2D]':
        """List[Vector2D]: 'Points' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Points

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'Series2D._Cast_Series2D':
        return self._Cast_Series2D(self)
