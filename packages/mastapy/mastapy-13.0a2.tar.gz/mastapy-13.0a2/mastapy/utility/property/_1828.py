"""_1828.py

DutyCyclePropertySummaryStress
"""
from typing import TypeVar

from mastapy._internal import constructor
from mastapy.utility.property import _1824
from mastapy.utility.units_and_measurements.measurements import _1703
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_PROPERTY_SUMMARY_STRESS = python_net_import('SMT.MastaAPI.Utility.Property', 'DutyCyclePropertySummaryStress')


__docformat__ = 'restructuredtext en'
__all__ = ('DutyCyclePropertySummaryStress',)


T = TypeVar('T')


class DutyCyclePropertySummaryStress(_1824.DutyCyclePropertySummary['_1703.Stress', T]):
    """DutyCyclePropertySummaryStress

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _DUTY_CYCLE_PROPERTY_SUMMARY_STRESS

    class _Cast_DutyCyclePropertySummaryStress:
        """Special nested class for casting DutyCyclePropertySummaryStress to subclasses."""

        def __init__(self, parent: 'DutyCyclePropertySummaryStress'):
            self._parent = parent

        @property
        def duty_cycle_property_summary(self):
            return self._parent._cast(_1824.DutyCyclePropertySummary)

        @property
        def duty_cycle_property_summary_stress(self) -> 'DutyCyclePropertySummaryStress':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DutyCyclePropertySummaryStress.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_value(self) -> 'float':
        """float: 'AverageValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageValue

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_value(self) -> 'float':
        """float: 'MaximumValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumValue

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_value(self) -> 'float':
        """float: 'MinimumValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumValue

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'DutyCyclePropertySummaryStress._Cast_DutyCyclePropertySummaryStress':
        return self._Cast_DutyCyclePropertySummaryStress(self)
