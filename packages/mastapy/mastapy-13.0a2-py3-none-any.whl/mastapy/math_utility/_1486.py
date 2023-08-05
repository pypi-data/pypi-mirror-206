"""_1486.py

ComplexVector6D
"""
from mastapy.math_utility import _1484
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPLEX_VECTOR_6D = python_net_import('SMT.MastaAPI.MathUtility', 'ComplexVector6D')


__docformat__ = 'restructuredtext en'
__all__ = ('ComplexVector6D',)


class ComplexVector6D(_1484.ComplexVector):
    """ComplexVector6D

    This is a mastapy class.
    """

    TYPE = _COMPLEX_VECTOR_6D

    class _Cast_ComplexVector6D:
        """Special nested class for casting ComplexVector6D to subclasses."""

        def __init__(self, parent: 'ComplexVector6D'):
            self._parent = parent

        @property
        def complex_vector(self):
            return self._parent._cast(_1484.ComplexVector)

        @property
        def complex_matrix(self):
            from mastapy.math_utility import _1482
            
            return self._parent._cast(_1482.ComplexMatrix)

        @property
        def generic_matrix(self):
            from mastapy.math_utility import _1502, _1482
            
            return self._parent._cast(_1502.GenericMatrix)

        @property
        def complex_vector_6d(self) -> 'ComplexVector6D':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComplexVector6D.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ComplexVector6D._Cast_ComplexVector6D':
        return self._Cast_ComplexVector6D(self)
