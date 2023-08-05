"""_1626.py

EnergyPerUnitArea
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENERGY_PER_UNIT_AREA = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'EnergyPerUnitArea')


__docformat__ = 'restructuredtext en'
__all__ = ('EnergyPerUnitArea',)


class EnergyPerUnitArea(_1594.MeasurementBase):
    """EnergyPerUnitArea

    This is a mastapy class.
    """

    TYPE = _ENERGY_PER_UNIT_AREA

    class _Cast_EnergyPerUnitArea:
        """Special nested class for casting EnergyPerUnitArea to subclasses."""

        def __init__(self, parent: 'EnergyPerUnitArea'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def energy_per_unit_area(self) -> 'EnergyPerUnitArea':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'EnergyPerUnitArea.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'EnergyPerUnitArea._Cast_EnergyPerUnitArea':
        return self._Cast_EnergyPerUnitArea(self)
