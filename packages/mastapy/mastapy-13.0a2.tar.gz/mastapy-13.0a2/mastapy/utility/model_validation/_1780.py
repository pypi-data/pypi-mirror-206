"""_1780.py

Fix
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FIX = python_net_import('SMT.MastaAPI.Utility.ModelValidation', 'Fix')


__docformat__ = 'restructuredtext en'
__all__ = ('Fix',)


class Fix(_0.APIBase):
    """Fix

    This is a mastapy class.
    """

    TYPE = _FIX

    class _Cast_Fix:
        """Special nested class for casting Fix to subclasses."""

        def __init__(self, parent: 'Fix'):
            self._parent = parent

        @property
        def fix(self) -> 'Fix':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Fix.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def description(self) -> 'str':
        """str: 'Description' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Description

        if temp is None:
            return ''

        return temp

    def perform(self):
        """ 'Perform' is the original name of this method."""

        self.wrapped.Perform()

    @property
    def cast_to(self) -> 'Fix._Cast_Fix':
        return self._Cast_Fix(self)
