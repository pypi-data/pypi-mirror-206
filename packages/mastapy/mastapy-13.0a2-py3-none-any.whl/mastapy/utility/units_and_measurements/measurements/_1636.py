"""_1636.py

FractionPerTemperature
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FRACTION_PER_TEMPERATURE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'FractionPerTemperature')


__docformat__ = 'restructuredtext en'
__all__ = ('FractionPerTemperature',)


class FractionPerTemperature(_1594.MeasurementBase):
    """FractionPerTemperature

    This is a mastapy class.
    """

    TYPE = _FRACTION_PER_TEMPERATURE

    class _Cast_FractionPerTemperature:
        """Special nested class for casting FractionPerTemperature to subclasses."""

        def __init__(self, parent: 'FractionPerTemperature'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def fraction_per_temperature(self) -> 'FractionPerTemperature':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FractionPerTemperature.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FractionPerTemperature._Cast_FractionPerTemperature':
        return self._Cast_FractionPerTemperature(self)
