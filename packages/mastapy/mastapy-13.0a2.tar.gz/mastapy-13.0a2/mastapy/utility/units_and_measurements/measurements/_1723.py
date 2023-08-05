"""_1723.py

Voltage
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VOLTAGE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Voltage')


__docformat__ = 'restructuredtext en'
__all__ = ('Voltage',)


class Voltage(_1594.MeasurementBase):
    """Voltage

    This is a mastapy class.
    """

    TYPE = _VOLTAGE

    class _Cast_Voltage:
        """Special nested class for casting Voltage to subclasses."""

        def __init__(self, parent: 'Voltage'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def voltage(self) -> 'Voltage':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Voltage.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Voltage._Cast_Voltage':
        return self._Cast_Voltage(self)
