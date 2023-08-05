"""_1679.py

Power
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Power')


__docformat__ = 'restructuredtext en'
__all__ = ('Power',)


class Power(_1594.MeasurementBase):
    """Power

    This is a mastapy class.
    """

    TYPE = _POWER

    class _Cast_Power:
        """Special nested class for casting Power to subclasses."""

        def __init__(self, parent: 'Power'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def power(self) -> 'Power':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Power.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Power._Cast_Power':
        return self._Cast_Power(self)
