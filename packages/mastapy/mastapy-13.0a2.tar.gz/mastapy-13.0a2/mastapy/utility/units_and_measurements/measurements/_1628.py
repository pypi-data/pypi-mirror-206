"""_1628.py

EnergySmall
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENERGY_SMALL = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'EnergySmall')


__docformat__ = 'restructuredtext en'
__all__ = ('EnergySmall',)


class EnergySmall(_1594.MeasurementBase):
    """EnergySmall

    This is a mastapy class.
    """

    TYPE = _ENERGY_SMALL

    class _Cast_EnergySmall:
        """Special nested class for casting EnergySmall to subclasses."""

        def __init__(self, parent: 'EnergySmall'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def energy_small(self) -> 'EnergySmall':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'EnergySmall.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'EnergySmall._Cast_EnergySmall':
        return self._Cast_EnergySmall(self)
