"""_85.py

SparseNodalMatrix
"""
from mastapy.nodal_analysis import _47
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPARSE_NODAL_MATRIX = python_net_import('SMT.MastaAPI.NodalAnalysis', 'SparseNodalMatrix')


__docformat__ = 'restructuredtext en'
__all__ = ('SparseNodalMatrix',)


class SparseNodalMatrix(_47.AbstractNodalMatrix):
    """SparseNodalMatrix

    This is a mastapy class.
    """

    TYPE = _SPARSE_NODAL_MATRIX

    class _Cast_SparseNodalMatrix:
        """Special nested class for casting SparseNodalMatrix to subclasses."""

        def __init__(self, parent: 'SparseNodalMatrix'):
            self._parent = parent

        @property
        def abstract_nodal_matrix(self):
            return self._parent._cast(_47.AbstractNodalMatrix)

        @property
        def sparse_nodal_matrix(self) -> 'SparseNodalMatrix':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SparseNodalMatrix.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SparseNodalMatrix._Cast_SparseNodalMatrix':
        return self._Cast_SparseNodalMatrix(self)
