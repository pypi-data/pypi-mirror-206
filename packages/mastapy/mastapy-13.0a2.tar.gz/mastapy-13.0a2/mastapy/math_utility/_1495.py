"""_1495.py

Eigenmode
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EIGENMODE = python_net_import('SMT.MastaAPI.MathUtility', 'Eigenmode')


__docformat__ = 'restructuredtext en'
__all__ = ('Eigenmode',)


class Eigenmode(_0.APIBase):
    """Eigenmode

    This is a mastapy class.
    """

    TYPE = _EIGENMODE

    class _Cast_Eigenmode:
        """Special nested class for casting Eigenmode to subclasses."""

        def __init__(self, parent: 'Eigenmode'):
            self._parent = parent

        @property
        def eigenmode(self) -> 'Eigenmode':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Eigenmode.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def frequency(self) -> 'float':
        """float: 'Frequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Frequency

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(self) -> 'Eigenmode._Cast_Eigenmode':
        return self._Cast_Eigenmode(self)
