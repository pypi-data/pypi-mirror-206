"""_1824.py

DutyCyclePropertySummary
"""
from typing import TypeVar, Generic

from mastapy import _0
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_PROPERTY_SUMMARY = python_net_import('SMT.MastaAPI.Utility.Property', 'DutyCyclePropertySummary')


__docformat__ = 'restructuredtext en'
__all__ = ('DutyCyclePropertySummary',)


TMeasurement = TypeVar('TMeasurement', bound='_1594.MeasurementBase')
T = TypeVar('T')


class DutyCyclePropertySummary(_0.APIBase, Generic[TMeasurement, T]):
    """DutyCyclePropertySummary

    This is a mastapy class.

    Generic Types:
        TMeasurement
        T
    """

    TYPE = _DUTY_CYCLE_PROPERTY_SUMMARY

    class _Cast_DutyCyclePropertySummary:
        """Special nested class for casting DutyCyclePropertySummary to subclasses."""

        def __init__(self, parent: 'DutyCyclePropertySummary'):
            self._parent = parent

        @property
        def duty_cycle_property_summary_force(self):
            from mastapy.utility.property import _1825
            
            return self._parent._cast(_1825.DutyCyclePropertySummaryForce)

        @property
        def duty_cycle_property_summary_percentage(self):
            from mastapy.utility.property import _1826
            
            return self._parent._cast(_1826.DutyCyclePropertySummaryPercentage)

        @property
        def duty_cycle_property_summary_small_angle(self):
            from mastapy.utility.property import _1827
            
            return self._parent._cast(_1827.DutyCyclePropertySummarySmallAngle)

        @property
        def duty_cycle_property_summary_stress(self):
            from mastapy.utility.property import _1828
            
            return self._parent._cast(_1828.DutyCyclePropertySummaryStress)

        @property
        def duty_cycle_property_summary(self) -> 'DutyCyclePropertySummary':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DutyCyclePropertySummary.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DutyCyclePropertySummary._Cast_DutyCyclePropertySummary':
        return self._Cast_DutyCyclePropertySummary(self)
