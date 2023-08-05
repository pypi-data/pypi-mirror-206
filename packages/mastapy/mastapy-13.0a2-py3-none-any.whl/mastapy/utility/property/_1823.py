"""_1823.py

DeletableCollectionMember
"""
from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DELETABLE_COLLECTION_MEMBER = python_net_import('SMT.MastaAPI.Utility.Property', 'DeletableCollectionMember')


__docformat__ = 'restructuredtext en'
__all__ = ('DeletableCollectionMember',)


T = TypeVar('T')


class DeletableCollectionMember(_0.APIBase, Generic[T]):
    """DeletableCollectionMember

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _DELETABLE_COLLECTION_MEMBER

    class _Cast_DeletableCollectionMember:
        """Special nested class for casting DeletableCollectionMember to subclasses."""

        def __init__(self, parent: 'DeletableCollectionMember'):
            self._parent = parent

        @property
        def deletable_collection_member(self) -> 'DeletableCollectionMember':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DeletableCollectionMember.TYPE'):
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
    def item(self) -> 'T':
        """T: 'Item' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Item

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(T)(temp) if temp is not None else None

    def delete(self):
        """ 'Delete' is the original name of this method."""

        self.wrapped.Delete()

    @property
    def cast_to(self) -> 'DeletableCollectionMember._Cast_DeletableCollectionMember':
        return self._Cast_DeletableCollectionMember(self)
