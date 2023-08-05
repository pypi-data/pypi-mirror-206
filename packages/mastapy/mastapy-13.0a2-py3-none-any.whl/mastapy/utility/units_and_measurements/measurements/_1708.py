"""_1708.py

ThermalContactCoefficient
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THERMAL_CONTACT_COEFFICIENT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'ThermalContactCoefficient')


__docformat__ = 'restructuredtext en'
__all__ = ('ThermalContactCoefficient',)


class ThermalContactCoefficient(_1594.MeasurementBase):
    """ThermalContactCoefficient

    This is a mastapy class.
    """

    TYPE = _THERMAL_CONTACT_COEFFICIENT

    class _Cast_ThermalContactCoefficient:
        """Special nested class for casting ThermalContactCoefficient to subclasses."""

        def __init__(self, parent: 'ThermalContactCoefficient'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def thermal_contact_coefficient(self) -> 'ThermalContactCoefficient':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ThermalContactCoefficient.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ThermalContactCoefficient._Cast_ThermalContactCoefficient':
        return self._Cast_ThermalContactCoefficient(self)
