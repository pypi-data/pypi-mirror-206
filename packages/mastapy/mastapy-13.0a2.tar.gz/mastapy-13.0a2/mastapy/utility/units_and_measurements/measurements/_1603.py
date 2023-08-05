"""_1603.py

AnglePerUnitTemperature
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGLE_PER_UNIT_TEMPERATURE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'AnglePerUnitTemperature')


__docformat__ = 'restructuredtext en'
__all__ = ('AnglePerUnitTemperature',)


class AnglePerUnitTemperature(_1594.MeasurementBase):
    """AnglePerUnitTemperature

    This is a mastapy class.
    """

    TYPE = _ANGLE_PER_UNIT_TEMPERATURE

    class _Cast_AnglePerUnitTemperature:
        """Special nested class for casting AnglePerUnitTemperature to subclasses."""

        def __init__(self, parent: 'AnglePerUnitTemperature'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def angle_per_unit_temperature(self) -> 'AnglePerUnitTemperature':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AnglePerUnitTemperature.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AnglePerUnitTemperature._Cast_AnglePerUnitTemperature':
        return self._Cast_AnglePerUnitTemperature(self)
