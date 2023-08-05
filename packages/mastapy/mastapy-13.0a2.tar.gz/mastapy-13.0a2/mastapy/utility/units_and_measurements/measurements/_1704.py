"""_1704.py

Temperature
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TEMPERATURE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Temperature')


__docformat__ = 'restructuredtext en'
__all__ = ('Temperature',)


class Temperature(_1594.MeasurementBase):
    """Temperature

    This is a mastapy class.
    """

    TYPE = _TEMPERATURE

    class _Cast_Temperature:
        """Special nested class for casting Temperature to subclasses."""

        def __init__(self, parent: 'Temperature'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def temperature(self) -> 'Temperature':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Temperature.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Temperature._Cast_Temperature':
        return self._Cast_Temperature(self)
