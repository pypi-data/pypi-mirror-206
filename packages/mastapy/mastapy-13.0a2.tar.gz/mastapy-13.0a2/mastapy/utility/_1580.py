"""_1580.py

MethodOutcomeWithResult
"""
from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy.utility import _1579
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_METHOD_OUTCOME_WITH_RESULT = python_net_import('SMT.MastaAPI.Utility', 'MethodOutcomeWithResult')


__docformat__ = 'restructuredtext en'
__all__ = ('MethodOutcomeWithResult',)


T = TypeVar('T')


class MethodOutcomeWithResult(_1579.MethodOutcome, Generic[T]):
    """MethodOutcomeWithResult

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _METHOD_OUTCOME_WITH_RESULT

    class _Cast_MethodOutcomeWithResult:
        """Special nested class for casting MethodOutcomeWithResult to subclasses."""

        def __init__(self, parent: 'MethodOutcomeWithResult'):
            self._parent = parent

        @property
        def method_outcome(self):
            return self._parent._cast(_1579.MethodOutcome)

        @property
        def method_outcome_with_result(self) -> 'MethodOutcomeWithResult':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MethodOutcomeWithResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def result(self) -> 'T':
        """T: 'Result' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Result

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(T)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MethodOutcomeWithResult._Cast_MethodOutcomeWithResult':
        return self._Cast_MethodOutcomeWithResult(self)
