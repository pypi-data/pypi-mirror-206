"""_1705.py

TemperatureDifference
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TEMPERATURE_DIFFERENCE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'TemperatureDifference')


__docformat__ = 'restructuredtext en'
__all__ = ('TemperatureDifference',)


class TemperatureDifference(_1594.MeasurementBase):
    """TemperatureDifference

    This is a mastapy class.
    """

    TYPE = _TEMPERATURE_DIFFERENCE

    class _Cast_TemperatureDifference:
        """Special nested class for casting TemperatureDifference to subclasses."""

        def __init__(self, parent: 'TemperatureDifference'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def temperature_difference(self) -> 'TemperatureDifference':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TemperatureDifference.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TemperatureDifference._Cast_TemperatureDifference':
        return self._Cast_TemperatureDifference(self)
