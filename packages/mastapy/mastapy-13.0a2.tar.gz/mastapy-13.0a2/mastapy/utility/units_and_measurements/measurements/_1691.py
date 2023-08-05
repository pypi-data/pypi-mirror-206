"""_1691.py

PressureViscosityCoefficient
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRESSURE_VISCOSITY_COEFFICIENT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'PressureViscosityCoefficient')


__docformat__ = 'restructuredtext en'
__all__ = ('PressureViscosityCoefficient',)


class PressureViscosityCoefficient(_1594.MeasurementBase):
    """PressureViscosityCoefficient

    This is a mastapy class.
    """

    TYPE = _PRESSURE_VISCOSITY_COEFFICIENT

    class _Cast_PressureViscosityCoefficient:
        """Special nested class for casting PressureViscosityCoefficient to subclasses."""

        def __init__(self, parent: 'PressureViscosityCoefficient'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def pressure_viscosity_coefficient(self) -> 'PressureViscosityCoefficient':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PressureViscosityCoefficient.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PressureViscosityCoefficient._Cast_PressureViscosityCoefficient':
        return self._Cast_PressureViscosityCoefficient(self)
