"""_1655.py

LengthPerUnitTemperature
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_PER_UNIT_TEMPERATURE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LengthPerUnitTemperature')


__docformat__ = 'restructuredtext en'
__all__ = ('LengthPerUnitTemperature',)


class LengthPerUnitTemperature(_1594.MeasurementBase):
    """LengthPerUnitTemperature

    This is a mastapy class.
    """

    TYPE = _LENGTH_PER_UNIT_TEMPERATURE

    class _Cast_LengthPerUnitTemperature:
        """Special nested class for casting LengthPerUnitTemperature to subclasses."""

        def __init__(self, parent: 'LengthPerUnitTemperature'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def length_per_unit_temperature(self) -> 'LengthPerUnitTemperature':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LengthPerUnitTemperature.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LengthPerUnitTemperature._Cast_LengthPerUnitTemperature':
        return self._Cast_LengthPerUnitTemperature(self)
