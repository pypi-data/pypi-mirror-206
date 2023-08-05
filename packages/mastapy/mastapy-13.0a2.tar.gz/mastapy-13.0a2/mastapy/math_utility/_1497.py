"""_1497.py

EulerParameters
"""
from mastapy.math_utility import _1514
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EULER_PARAMETERS = python_net_import('SMT.MastaAPI.MathUtility', 'EulerParameters')


__docformat__ = 'restructuredtext en'
__all__ = ('EulerParameters',)


class EulerParameters(_1514.RealVector):
    """EulerParameters

    This is a mastapy class.
    """

    TYPE = _EULER_PARAMETERS

    class _Cast_EulerParameters:
        """Special nested class for casting EulerParameters to subclasses."""

        def __init__(self, parent: 'EulerParameters'):
            self._parent = parent

        @property
        def real_vector(self):
            return self._parent._cast(_1514.RealVector)

        @property
        def real_matrix(self):
            from mastapy.math_utility import _1513
            
            return self._parent._cast(_1513.RealMatrix)

        @property
        def generic_matrix(self):
            from mastapy.math_utility import _1502, _1513
            
            return self._parent._cast(_1502.GenericMatrix)

        @property
        def euler_parameters(self) -> 'EulerParameters':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'EulerParameters.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'EulerParameters._Cast_EulerParameters':
        return self._Cast_EulerParameters(self)
