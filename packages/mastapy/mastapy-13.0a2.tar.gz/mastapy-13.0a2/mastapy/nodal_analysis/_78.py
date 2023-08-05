"""_78.py

NodalMatrix
"""
from typing import List

from mastapy.nodal_analysis import _79, _47
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_MATRIX = python_net_import('SMT.MastaAPI.NodalAnalysis', 'NodalMatrix')


__docformat__ = 'restructuredtext en'
__all__ = ('NodalMatrix',)


class NodalMatrix(_47.AbstractNodalMatrix):
    """NodalMatrix

    This is a mastapy class.
    """

    TYPE = _NODAL_MATRIX

    class _Cast_NodalMatrix:
        """Special nested class for casting NodalMatrix to subclasses."""

        def __init__(self, parent: 'NodalMatrix'):
            self._parent = parent

        @property
        def abstract_nodal_matrix(self):
            return self._parent._cast(_47.AbstractNodalMatrix)

        @property
        def nodal_matrix(self) -> 'NodalMatrix':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NodalMatrix.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rows(self) -> 'List[_79.NodalMatrixRow]':
        """List[NodalMatrixRow]: 'Rows' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rows

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'NodalMatrix._Cast_NodalMatrix':
        return self._Cast_NodalMatrix(self)
