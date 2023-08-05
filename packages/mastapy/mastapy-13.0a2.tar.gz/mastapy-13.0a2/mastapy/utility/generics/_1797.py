"""_1797.py

NamedTuple1
"""
from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_TUPLE_1 = python_net_import('SMT.MastaAPI.Utility.Generics', 'NamedTuple1')


__docformat__ = 'restructuredtext en'
__all__ = ('NamedTuple1',)


T1 = TypeVar('T1')


class NamedTuple1(_0.APIBase, Generic[T1]):
    """NamedTuple1

    This is a mastapy class.

    Generic Types:
        T1
    """

    TYPE = _NAMED_TUPLE_1

    class _Cast_NamedTuple1:
        """Special nested class for casting NamedTuple1 to subclasses."""

        def __init__(self, parent: 'NamedTuple1'):
            self._parent = parent

        @property
        def named_tuple_1(self) -> 'NamedTuple1':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NamedTuple1.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def item_1(self) -> 'T1':
        """T1: 'Item1' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Item1

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(T1)(temp) if temp is not None else None

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
    def cast_to(self) -> 'NamedTuple1._Cast_NamedTuple1':
        return self._Cast_NamedTuple1(self)
