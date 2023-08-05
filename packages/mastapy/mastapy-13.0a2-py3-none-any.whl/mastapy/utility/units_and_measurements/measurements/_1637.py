"""_1637.py

Frequency
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FREQUENCY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Frequency')


__docformat__ = 'restructuredtext en'
__all__ = ('Frequency',)


class Frequency(_1594.MeasurementBase):
    """Frequency

    This is a mastapy class.
    """

    TYPE = _FREQUENCY

    class _Cast_Frequency:
        """Special nested class for casting Frequency to subclasses."""

        def __init__(self, parent: 'Frequency'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def frequency(self) -> 'Frequency':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Frequency.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Frequency._Cast_Frequency':
        return self._Cast_Frequency(self)
