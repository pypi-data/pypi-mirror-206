"""_1534.py

OptimizationVariable
"""
from typing import List

from mastapy.utility.units_and_measurements import _1594
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_VARIABLE = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'OptimizationVariable')


__docformat__ = 'restructuredtext en'
__all__ = ('OptimizationVariable',)


class OptimizationVariable(_0.APIBase):
    """OptimizationVariable

    This is a mastapy class.
    """

    TYPE = _OPTIMIZATION_VARIABLE

    class _Cast_OptimizationVariable:
        """Special nested class for casting OptimizationVariable to subclasses."""

        def __init__(self, parent: 'OptimizationVariable'):
            self._parent = parent

        @property
        def optimization_input(self):
            from mastapy.math_utility.optimisation import _1533
            
            return self._parent._cast(_1533.OptimizationInput)

        @property
        def reporting_optimization_input(self):
            from mastapy.math_utility.optimisation import _1545
            
            return self._parent._cast(_1545.ReportingOptimizationInput)

        @property
        def optimization_variable(self) -> 'OptimizationVariable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OptimizationVariable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measurement(self) -> '_1594.MeasurementBase':
        """MeasurementBase: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement.setter
    def measurement(self, value: '_1594.MeasurementBase'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def results(self) -> 'List[float]':
        """List[float]: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Results

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def cast_to(self) -> 'OptimizationVariable._Cast_OptimizationVariable':
        return self._Cast_OptimizationVariable(self)
