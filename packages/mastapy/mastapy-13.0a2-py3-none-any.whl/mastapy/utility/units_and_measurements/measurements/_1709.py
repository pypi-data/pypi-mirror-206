"""_1709.py

ThermalExpansionCoefficient
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THERMAL_EXPANSION_COEFFICIENT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'ThermalExpansionCoefficient')


__docformat__ = 'restructuredtext en'
__all__ = ('ThermalExpansionCoefficient',)


class ThermalExpansionCoefficient(_1594.MeasurementBase):
    """ThermalExpansionCoefficient

    This is a mastapy class.
    """

    TYPE = _THERMAL_EXPANSION_COEFFICIENT

    class _Cast_ThermalExpansionCoefficient:
        """Special nested class for casting ThermalExpansionCoefficient to subclasses."""

        def __init__(self, parent: 'ThermalExpansionCoefficient'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def thermal_expansion_coefficient(self) -> 'ThermalExpansionCoefficient':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ThermalExpansionCoefficient.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ThermalExpansionCoefficient._Cast_ThermalExpansionCoefficient':
        return self._Cast_ThermalExpansionCoefficient(self)
