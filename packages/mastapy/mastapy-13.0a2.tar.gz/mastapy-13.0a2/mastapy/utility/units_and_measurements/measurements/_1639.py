"""_1639.py

FuelEfficiencyVehicle
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FUEL_EFFICIENCY_VEHICLE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'FuelEfficiencyVehicle')


__docformat__ = 'restructuredtext en'
__all__ = ('FuelEfficiencyVehicle',)


class FuelEfficiencyVehicle(_1594.MeasurementBase):
    """FuelEfficiencyVehicle

    This is a mastapy class.
    """

    TYPE = _FUEL_EFFICIENCY_VEHICLE

    class _Cast_FuelEfficiencyVehicle:
        """Special nested class for casting FuelEfficiencyVehicle to subclasses."""

        def __init__(self, parent: 'FuelEfficiencyVehicle'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def fuel_efficiency_vehicle(self) -> 'FuelEfficiencyVehicle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FuelEfficiencyVehicle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FuelEfficiencyVehicle._Cast_FuelEfficiencyVehicle':
        return self._Cast_FuelEfficiencyVehicle(self)
