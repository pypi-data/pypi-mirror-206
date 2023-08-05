"""_2272.py

RealignmentResult
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REALIGNMENT_RESULT = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'RealignmentResult')


__docformat__ = 'restructuredtext en'
__all__ = ('RealignmentResult',)


class RealignmentResult(_0.APIBase):
    """RealignmentResult

    This is a mastapy class.
    """

    TYPE = _REALIGNMENT_RESULT

    class _Cast_RealignmentResult:
        """Special nested class for casting RealignmentResult to subclasses."""

        def __init__(self, parent: 'RealignmentResult'):
            self._parent = parent

        @property
        def realignment_result(self) -> 'RealignmentResult':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RealignmentResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def successful(self) -> 'bool':
        """bool: 'Successful' is the original name of this property."""

        temp = self.wrapped.Successful

        if temp is None:
            return False

        return temp

    @successful.setter
    def successful(self, value: 'bool'):
        self.wrapped.Successful = bool(value) if value else False

    @property
    def cast_to(self) -> 'RealignmentResult._Cast_RealignmentResult':
        return self._Cast_RealignmentResult(self)
