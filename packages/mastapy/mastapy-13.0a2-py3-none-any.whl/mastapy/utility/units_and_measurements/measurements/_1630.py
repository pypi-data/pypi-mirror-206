"""_1630.py

FlowRate
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLOW_RATE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'FlowRate')


__docformat__ = 'restructuredtext en'
__all__ = ('FlowRate',)


class FlowRate(_1594.MeasurementBase):
    """FlowRate

    This is a mastapy class.
    """

    TYPE = _FLOW_RATE

    class _Cast_FlowRate:
        """Special nested class for casting FlowRate to subclasses."""

        def __init__(self, parent: 'FlowRate'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def flow_rate(self) -> 'FlowRate':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlowRate.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FlowRate._Cast_FlowRate':
        return self._Cast_FlowRate(self)
