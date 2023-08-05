"""_1579.py

MethodOutcome
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_METHOD_OUTCOME = python_net_import('SMT.MastaAPI.Utility', 'MethodOutcome')


__docformat__ = 'restructuredtext en'
__all__ = ('MethodOutcome',)


class MethodOutcome(_0.APIBase):
    """MethodOutcome

    This is a mastapy class.
    """

    TYPE = _METHOD_OUTCOME

    class _Cast_MethodOutcome:
        """Special nested class for casting MethodOutcome to subclasses."""

        def __init__(self, parent: 'MethodOutcome'):
            self._parent = parent

        @property
        def method_outcome_with_result(self):
            from mastapy.utility import _1580
            
            return self._parent._cast(_1580.MethodOutcomeWithResult)

        @property
        def method_outcome(self) -> 'MethodOutcome':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MethodOutcome.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def failure_message(self) -> 'str':
        """str: 'FailureMessage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FailureMessage

        if temp is None:
            return ''

        return temp

    @property
    def successful(self) -> 'bool':
        """bool: 'Successful' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Successful

        if temp is None:
            return False

        return temp

    @property
    def cast_to(self) -> 'MethodOutcome._Cast_MethodOutcome':
        return self._Cast_MethodOutcome(self)
