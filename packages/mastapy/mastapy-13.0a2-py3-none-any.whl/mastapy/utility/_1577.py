"""_1577.py

IntegerRange
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTEGER_RANGE = python_net_import('SMT.MastaAPI.Utility', 'IntegerRange')


__docformat__ = 'restructuredtext en'
__all__ = ('IntegerRange',)


class IntegerRange(_0.APIBase):
    """IntegerRange

    This is a mastapy class.
    """

    TYPE = _INTEGER_RANGE

    class _Cast_IntegerRange:
        """Special nested class for casting IntegerRange to subclasses."""

        def __init__(self, parent: 'IntegerRange'):
            self._parent = parent

        @property
        def integer_range(self) -> 'IntegerRange':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'IntegerRange.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def max(self) -> 'int':
        """int: 'Max' is the original name of this property."""

        temp = self.wrapped.Max

        if temp is None:
            return 0

        return temp

    @max.setter
    def max(self, value: 'int'):
        self.wrapped.Max = int(value) if value else 0

    @property
    def min(self) -> 'int':
        """int: 'Min' is the original name of this property."""

        temp = self.wrapped.Min

        if temp is None:
            return 0

        return temp

    @min.setter
    def min(self, value: 'int'):
        self.wrapped.Min = int(value) if value else 0

    @property
    def cast_to(self) -> 'IntegerRange._Cast_IntegerRange':
        return self._Cast_IntegerRange(self)
