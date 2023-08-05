"""_1533.py

OptimizationInput
"""
from mastapy.math_utility.optimisation import _1534
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_INPUT = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'OptimizationInput')


__docformat__ = 'restructuredtext en'
__all__ = ('OptimizationInput',)


class OptimizationInput(_1534.OptimizationVariable):
    """OptimizationInput

    This is a mastapy class.
    """

    TYPE = _OPTIMIZATION_INPUT

    class _Cast_OptimizationInput:
        """Special nested class for casting OptimizationInput to subclasses."""

        def __init__(self, parent: 'OptimizationInput'):
            self._parent = parent

        @property
        def optimization_variable(self):
            return self._parent._cast(_1534.OptimizationVariable)

        @property
        def reporting_optimization_input(self):
            from mastapy.math_utility.optimisation import _1545
            
            return self._parent._cast(_1545.ReportingOptimizationInput)

        @property
        def optimization_input(self) -> 'OptimizationInput':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OptimizationInput.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'OptimizationInput._Cast_OptimizationInput':
        return self._Cast_OptimizationInput(self)
