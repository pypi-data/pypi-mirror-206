"""_47.py

AbstractNodalMatrix
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_NODAL_MATRIX = python_net_import('SMT.MastaAPI.NodalAnalysis', 'AbstractNodalMatrix')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractNodalMatrix',)


class AbstractNodalMatrix(_0.APIBase):
    """AbstractNodalMatrix

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_NODAL_MATRIX

    class _Cast_AbstractNodalMatrix:
        """Special nested class for casting AbstractNodalMatrix to subclasses."""

        def __init__(self, parent: 'AbstractNodalMatrix'):
            self._parent = parent

        @property
        def nodal_matrix(self):
            from mastapy.nodal_analysis import _78
            
            return self._parent._cast(_78.NodalMatrix)

        @property
        def sparse_nodal_matrix(self):
            from mastapy.nodal_analysis import _85
            
            return self._parent._cast(_85.SparseNodalMatrix)

        @property
        def abstract_nodal_matrix(self) -> 'AbstractNodalMatrix':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractNodalMatrix.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AbstractNodalMatrix._Cast_AbstractNodalMatrix':
        return self._Cast_AbstractNodalMatrix(self)
