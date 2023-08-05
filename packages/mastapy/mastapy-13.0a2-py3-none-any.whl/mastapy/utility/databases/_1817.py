"""_1817.py

NamedKey
"""
from mastapy._internal import constructor
from mastapy.utility.databases import _1813
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_KEY = python_net_import('SMT.MastaAPI.Utility.Databases', 'NamedKey')


__docformat__ = 'restructuredtext en'
__all__ = ('NamedKey',)


class NamedKey(_1813.DatabaseKey):
    """NamedKey

    This is a mastapy class.
    """

    TYPE = _NAMED_KEY

    class _Cast_NamedKey:
        """Special nested class for casting NamedKey to subclasses."""

        def __init__(self, parent: 'NamedKey'):
            self._parent = parent

        @property
        def database_key(self):
            return self._parent._cast(_1813.DatabaseKey)

        @property
        def named_key(self) -> 'NamedKey':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NamedKey.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def cast_to(self) -> 'NamedKey._Cast_NamedKey':
        return self._Cast_NamedKey(self)
