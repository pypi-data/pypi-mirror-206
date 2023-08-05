"""_1563.py

ConvergenceLogger
"""
from mastapy.math_utility.convergence import _1564
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONVERGENCE_LOGGER = python_net_import('SMT.MastaAPI.MathUtility.Convergence', 'ConvergenceLogger')


__docformat__ = 'restructuredtext en'
__all__ = ('ConvergenceLogger',)


class ConvergenceLogger(_1564.DataLogger):
    """ConvergenceLogger

    This is a mastapy class.
    """

    TYPE = _CONVERGENCE_LOGGER

    class _Cast_ConvergenceLogger:
        """Special nested class for casting ConvergenceLogger to subclasses."""

        def __init__(self, parent: 'ConvergenceLogger'):
            self._parent = parent

        @property
        def data_logger(self):
            return self._parent._cast(_1564.DataLogger)

        @property
        def convergence_logger(self) -> 'ConvergenceLogger':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConvergenceLogger.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConvergenceLogger._Cast_ConvergenceLogger':
        return self._Cast_ConvergenceLogger(self)
