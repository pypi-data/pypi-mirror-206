"""_1545.py

ReportingOptimizationInput
"""
from mastapy.math_utility.optimisation import _1533
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REPORTING_OPTIMIZATION_INPUT = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'ReportingOptimizationInput')


__docformat__ = 'restructuredtext en'
__all__ = ('ReportingOptimizationInput',)


class ReportingOptimizationInput(_1533.OptimizationInput):
    """ReportingOptimizationInput

    This is a mastapy class.
    """

    TYPE = _REPORTING_OPTIMIZATION_INPUT

    class _Cast_ReportingOptimizationInput:
        """Special nested class for casting ReportingOptimizationInput to subclasses."""

        def __init__(self, parent: 'ReportingOptimizationInput'):
            self._parent = parent

        @property
        def optimization_input(self):
            return self._parent._cast(_1533.OptimizationInput)

        @property
        def optimization_variable(self):
            from mastapy.math_utility.optimisation import _1534
            
            return self._parent._cast(_1534.OptimizationVariable)

        @property
        def reporting_optimization_input(self) -> 'ReportingOptimizationInput':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ReportingOptimizationInput.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ReportingOptimizationInput._Cast_ReportingOptimizationInput':
        return self._Cast_ReportingOptimizationInput(self)
