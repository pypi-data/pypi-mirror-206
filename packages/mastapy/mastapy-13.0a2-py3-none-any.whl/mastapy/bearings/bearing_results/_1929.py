"""_1929.py

ElementForce
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_FORCE = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'ElementForce')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementForce',)


class ElementForce(_0.APIBase):
    """ElementForce

    This is a mastapy class.
    """

    TYPE = _ELEMENT_FORCE

    class _Cast_ElementForce:
        """Special nested class for casting ElementForce to subclasses."""

        def __init__(self, parent: 'ElementForce'):
            self._parent = parent

        @property
        def element_force(self) -> 'ElementForce':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementForce.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial(self) -> 'float':
        """float: 'Axial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Axial

        if temp is None:
            return 0.0

        return temp

    @property
    def moment(self) -> 'float':
        """float: 'Moment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Moment

        if temp is None:
            return 0.0

        return temp

    @property
    def radial(self) -> 'float':
        """float: 'Radial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Radial

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ElementForce._Cast_ElementForce':
        return self._Cast_ElementForce(self)
