"""_1693.py

PricePerUnitMass
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRICE_PER_UNIT_MASS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'PricePerUnitMass')


__docformat__ = 'restructuredtext en'
__all__ = ('PricePerUnitMass',)


class PricePerUnitMass(_1594.MeasurementBase):
    """PricePerUnitMass

    This is a mastapy class.
    """

    TYPE = _PRICE_PER_UNIT_MASS

    class _Cast_PricePerUnitMass:
        """Special nested class for casting PricePerUnitMass to subclasses."""

        def __init__(self, parent: 'PricePerUnitMass'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def price_per_unit_mass(self) -> 'PricePerUnitMass':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PricePerUnitMass.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PricePerUnitMass._Cast_PricePerUnitMass':
        return self._Cast_PricePerUnitMass(self)
