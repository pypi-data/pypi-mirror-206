"""_1514.py

RealVector
"""
from mastapy.math_utility import _1513
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REAL_VECTOR = python_net_import('SMT.MastaAPI.MathUtility', 'RealVector')


__docformat__ = 'restructuredtext en'
__all__ = ('RealVector',)


class RealVector(_1513.RealMatrix):
    """RealVector

    This is a mastapy class.
    """

    TYPE = _REAL_VECTOR

    class _Cast_RealVector:
        """Special nested class for casting RealVector to subclasses."""

        def __init__(self, parent: 'RealVector'):
            self._parent = parent

        @property
        def real_matrix(self):
            return self._parent._cast(_1513.RealMatrix)

        @property
        def generic_matrix(self):
            from mastapy.math_utility import _1502
            
            return self._parent._cast(_1502.GenericMatrix)

        @property
        def euler_parameters(self):
            from mastapy.math_utility import _1497
            
            return self._parent._cast(_1497.EulerParameters)

        @property
        def quaternion(self):
            from mastapy.math_utility import _1512
            
            return self._parent._cast(_1512.Quaternion)

        @property
        def vector_6d(self):
            from mastapy.math_utility import _1524
            
            return self._parent._cast(_1524.Vector6D)

        @property
        def real_vector(self) -> 'RealVector':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RealVector.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RealVector._Cast_RealVector':
        return self._Cast_RealVector(self)
