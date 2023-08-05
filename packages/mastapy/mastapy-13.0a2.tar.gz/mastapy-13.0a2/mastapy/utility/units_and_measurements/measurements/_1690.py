"""_1690.py

PressureVelocityProduct
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRESSURE_VELOCITY_PRODUCT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'PressureVelocityProduct')


__docformat__ = 'restructuredtext en'
__all__ = ('PressureVelocityProduct',)


class PressureVelocityProduct(_1594.MeasurementBase):
    """PressureVelocityProduct

    This is a mastapy class.
    """

    TYPE = _PRESSURE_VELOCITY_PRODUCT

    class _Cast_PressureVelocityProduct:
        """Special nested class for casting PressureVelocityProduct to subclasses."""

        def __init__(self, parent: 'PressureVelocityProduct'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def pressure_velocity_product(self) -> 'PressureVelocityProduct':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PressureVelocityProduct.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PressureVelocityProduct._Cast_PressureVelocityProduct':
        return self._Cast_PressureVelocityProduct(self)
