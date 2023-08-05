"""_1676.py

MomentPerUnitPressure
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOMENT_PER_UNIT_PRESSURE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MomentPerUnitPressure')


__docformat__ = 'restructuredtext en'
__all__ = ('MomentPerUnitPressure',)


class MomentPerUnitPressure(_1594.MeasurementBase):
    """MomentPerUnitPressure

    This is a mastapy class.
    """

    TYPE = _MOMENT_PER_UNIT_PRESSURE

    class _Cast_MomentPerUnitPressure:
        """Special nested class for casting MomentPerUnitPressure to subclasses."""

        def __init__(self, parent: 'MomentPerUnitPressure'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def moment_per_unit_pressure(self) -> 'MomentPerUnitPressure':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MomentPerUnitPressure.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MomentPerUnitPressure._Cast_MomentPerUnitPressure':
        return self._Cast_MomentPerUnitPressure(self)
