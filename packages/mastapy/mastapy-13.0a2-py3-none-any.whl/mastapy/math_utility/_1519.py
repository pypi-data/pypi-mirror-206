"""_1519.py

SquareMatrix
"""
from mastapy.math_utility import _1513
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SQUARE_MATRIX = python_net_import('SMT.MastaAPI.MathUtility', 'SquareMatrix')


__docformat__ = 'restructuredtext en'
__all__ = ('SquareMatrix',)


class SquareMatrix(_1513.RealMatrix):
    """SquareMatrix

    This is a mastapy class.
    """

    TYPE = _SQUARE_MATRIX

    class _Cast_SquareMatrix:
        """Special nested class for casting SquareMatrix to subclasses."""

        def __init__(self, parent: 'SquareMatrix'):
            self._parent = parent

        @property
        def real_matrix(self):
            return self._parent._cast(_1513.RealMatrix)

        @property
        def generic_matrix(self):
            from mastapy.math_utility import _1502
            
            return self._parent._cast(_1502.GenericMatrix)

        @property
        def square_matrix(self) -> 'SquareMatrix':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SquareMatrix.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SquareMatrix._Cast_SquareMatrix':
        return self._Cast_SquareMatrix(self)
