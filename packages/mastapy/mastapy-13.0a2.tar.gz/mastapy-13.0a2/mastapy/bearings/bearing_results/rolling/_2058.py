"""_2058.py

StressAtPosition
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRESS_AT_POSITION = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'StressAtPosition')


__docformat__ = 'restructuredtext en'
__all__ = ('StressAtPosition',)


class StressAtPosition(_0.APIBase):
    """StressAtPosition

    This is a mastapy class.
    """

    TYPE = _STRESS_AT_POSITION

    class _Cast_StressAtPosition:
        """Special nested class for casting StressAtPosition to subclasses."""

        def __init__(self, parent: 'StressAtPosition'):
            self._parent = parent

        @property
        def stress_at_position(self) -> 'StressAtPosition':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StressAtPosition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def position(self) -> 'float':
        """float: 'Position' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Position

        if temp is None:
            return 0.0

        return temp

    @property
    def stress(self) -> 'float':
        """float: 'Stress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Stress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'StressAtPosition._Cast_StressAtPosition':
        return self._Cast_StressAtPosition(self)
