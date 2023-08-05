"""_1724.py

VoltagePerAngularVelocity
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VOLTAGE_PER_ANGULAR_VELOCITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'VoltagePerAngularVelocity')


__docformat__ = 'restructuredtext en'
__all__ = ('VoltagePerAngularVelocity',)


class VoltagePerAngularVelocity(_1594.MeasurementBase):
    """VoltagePerAngularVelocity

    This is a mastapy class.
    """

    TYPE = _VOLTAGE_PER_ANGULAR_VELOCITY

    class _Cast_VoltagePerAngularVelocity:
        """Special nested class for casting VoltagePerAngularVelocity to subclasses."""

        def __init__(self, parent: 'VoltagePerAngularVelocity'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def voltage_per_angular_velocity(self) -> 'VoltagePerAngularVelocity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VoltagePerAngularVelocity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'VoltagePerAngularVelocity._Cast_VoltagePerAngularVelocity':
        return self._Cast_VoltagePerAngularVelocity(self)
