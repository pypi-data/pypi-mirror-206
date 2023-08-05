"""_1634.py

ForcePerUnitTemperature
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_PER_UNIT_TEMPERATURE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'ForcePerUnitTemperature')


__docformat__ = 'restructuredtext en'
__all__ = ('ForcePerUnitTemperature',)


class ForcePerUnitTemperature(_1594.MeasurementBase):
    """ForcePerUnitTemperature

    This is a mastapy class.
    """

    TYPE = _FORCE_PER_UNIT_TEMPERATURE

    class _Cast_ForcePerUnitTemperature:
        """Special nested class for casting ForcePerUnitTemperature to subclasses."""

        def __init__(self, parent: 'ForcePerUnitTemperature'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def force_per_unit_temperature(self) -> 'ForcePerUnitTemperature':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ForcePerUnitTemperature.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ForcePerUnitTemperature._Cast_ForcePerUnitTemperature':
        return self._Cast_ForcePerUnitTemperature(self)
