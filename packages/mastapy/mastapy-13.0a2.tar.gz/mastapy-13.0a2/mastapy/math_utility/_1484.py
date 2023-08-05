"""_1484.py

ComplexVector
"""
from mastapy.math_utility import _1482
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPLEX_VECTOR = python_net_import('SMT.MastaAPI.MathUtility', 'ComplexVector')


__docformat__ = 'restructuredtext en'
__all__ = ('ComplexVector',)


class ComplexVector(_1482.ComplexMatrix):
    """ComplexVector

    This is a mastapy class.
    """

    TYPE = _COMPLEX_VECTOR

    class _Cast_ComplexVector:
        """Special nested class for casting ComplexVector to subclasses."""

        def __init__(self, parent: 'ComplexVector'):
            self._parent = parent

        @property
        def complex_matrix(self):
            return self._parent._cast(_1482.ComplexMatrix)

        @property
        def generic_matrix(self):
            from mastapy.math_utility import _1502
            
            return self._parent._cast(_1502.GenericMatrix)

        @property
        def complex_vector_3d(self):
            from mastapy.math_utility import _1485
            
            return self._parent._cast(_1485.ComplexVector3D)

        @property
        def complex_vector_6d(self):
            from mastapy.math_utility import _1486
            
            return self._parent._cast(_1486.ComplexVector6D)

        @property
        def complex_vector(self) -> 'ComplexVector':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComplexVector.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ComplexVector._Cast_ComplexVector':
        return self._Cast_ComplexVector(self)
