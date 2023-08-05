"""_1717.py

TorquePerCurrent
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_PER_CURRENT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'TorquePerCurrent')


__docformat__ = 'restructuredtext en'
__all__ = ('TorquePerCurrent',)


class TorquePerCurrent(_1594.MeasurementBase):
    """TorquePerCurrent

    This is a mastapy class.
    """

    TYPE = _TORQUE_PER_CURRENT

    class _Cast_TorquePerCurrent:
        """Special nested class for casting TorquePerCurrent to subclasses."""

        def __init__(self, parent: 'TorquePerCurrent'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def torque_per_current(self) -> 'TorquePerCurrent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorquePerCurrent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TorquePerCurrent._Cast_TorquePerCurrent':
        return self._Cast_TorquePerCurrent(self)
