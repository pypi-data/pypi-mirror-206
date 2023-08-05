"""_1803.py

NamedTuple7
"""
from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_TUPLE_7 = python_net_import('SMT.MastaAPI.Utility.Generics', 'NamedTuple7')


__docformat__ = 'restructuredtext en'
__all__ = ('NamedTuple7',)


T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')
T4 = TypeVar('T4')
T5 = TypeVar('T5')
T6 = TypeVar('T6')
T7 = TypeVar('T7')


class NamedTuple7(_0.APIBase, Generic[T1, T2, T3, T4, T5, T6, T7]):
    """NamedTuple7

    This is a mastapy class.

    Generic Types:
        T1
        T2
        T3
        T4
        T5
        T6
        T7
    """

    TYPE = _NAMED_TUPLE_7

    class _Cast_NamedTuple7:
        """Special nested class for casting NamedTuple7 to subclasses."""

        def __init__(self, parent: 'NamedTuple7'):
            self._parent = parent

        @property
        def named_tuple_7(self) -> 'NamedTuple7':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NamedTuple7.TYPE'):
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
    def item_2(self) -> 'T2':
        """T2: 'Item2' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Item2

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(T2)(temp) if temp is not None else None

    @property
    def item_3(self) -> 'T3':
        """T3: 'Item3' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Item3

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(T3)(temp) if temp is not None else None

    @property
    def item_4(self) -> 'T4':
        """T4: 'Item4' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Item4

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(T4)(temp) if temp is not None else None

    @property
    def item_5(self) -> 'T5':
        """T5: 'Item5' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Item5

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(T5)(temp) if temp is not None else None

    @property
    def item_6(self) -> 'T6':
        """T6: 'Item6' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Item6

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(T6)(temp) if temp is not None else None

    @property
    def item_7(self) -> 'T7':
        """T7: 'Item7' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Item7

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(T7)(temp) if temp is not None else None

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
    def cast_to(self) -> 'NamedTuple7._Cast_NamedTuple7':
        return self._Cast_NamedTuple7(self)
