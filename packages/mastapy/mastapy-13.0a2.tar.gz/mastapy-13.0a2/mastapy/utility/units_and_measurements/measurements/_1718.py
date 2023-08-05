"""_1718.py

TorquePerSquareRootOfPower
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_PER_SQUARE_ROOT_OF_POWER = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'TorquePerSquareRootOfPower')


__docformat__ = 'restructuredtext en'
__all__ = ('TorquePerSquareRootOfPower',)


class TorquePerSquareRootOfPower(_1594.MeasurementBase):
    """TorquePerSquareRootOfPower

    This is a mastapy class.
    """

    TYPE = _TORQUE_PER_SQUARE_ROOT_OF_POWER

    class _Cast_TorquePerSquareRootOfPower:
        """Special nested class for casting TorquePerSquareRootOfPower to subclasses."""

        def __init__(self, parent: 'TorquePerSquareRootOfPower'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def torque_per_square_root_of_power(self) -> 'TorquePerSquareRootOfPower':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorquePerSquareRootOfPower.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TorquePerSquareRootOfPower._Cast_TorquePerSquareRootOfPower':
        return self._Cast_TorquePerSquareRootOfPower(self)
