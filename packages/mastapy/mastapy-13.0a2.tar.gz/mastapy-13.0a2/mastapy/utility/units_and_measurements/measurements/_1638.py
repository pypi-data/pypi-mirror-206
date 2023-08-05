"""_1638.py

FuelConsumptionEngine
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FUEL_CONSUMPTION_ENGINE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'FuelConsumptionEngine')


__docformat__ = 'restructuredtext en'
__all__ = ('FuelConsumptionEngine',)


class FuelConsumptionEngine(_1594.MeasurementBase):
    """FuelConsumptionEngine

    This is a mastapy class.
    """

    TYPE = _FUEL_CONSUMPTION_ENGINE

    class _Cast_FuelConsumptionEngine:
        """Special nested class for casting FuelConsumptionEngine to subclasses."""

        def __init__(self, parent: 'FuelConsumptionEngine'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def fuel_consumption_engine(self) -> 'FuelConsumptionEngine':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FuelConsumptionEngine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FuelConsumptionEngine._Cast_FuelConsumptionEngine':
        return self._Cast_FuelConsumptionEngine(self)
