"""_1496.py

Eigenmodes
"""
from typing import List

from mastapy.math_utility import _1495
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EIGENMODES = python_net_import('SMT.MastaAPI.MathUtility', 'Eigenmodes')


__docformat__ = 'restructuredtext en'
__all__ = ('Eigenmodes',)


class Eigenmodes(_0.APIBase):
    """Eigenmodes

    This is a mastapy class.
    """

    TYPE = _EIGENMODES

    class _Cast_Eigenmodes:
        """Special nested class for casting Eigenmodes to subclasses."""

        def __init__(self, parent: 'Eigenmodes'):
            self._parent = parent

        @property
        def eigenmodes(self) -> 'Eigenmodes':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Eigenmodes.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def items(self) -> 'List[_1495.Eigenmode]':
        """List[Eigenmode]: 'Items' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Items

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'Eigenmodes._Cast_Eigenmodes':
        return self._Cast_Eigenmodes(self)
