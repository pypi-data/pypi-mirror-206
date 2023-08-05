"""_1688.py

Pressure
"""
from mastapy.utility.units_and_measurements.measurements import _1703
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PRESSURE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Pressure')


__docformat__ = 'restructuredtext en'
__all__ = ('Pressure',)


class Pressure(_1703.Stress):
    """Pressure

    This is a mastapy class.
    """

    TYPE = _PRESSURE

    class _Cast_Pressure:
        """Special nested class for casting Pressure to subclasses."""

        def __init__(self, parent: 'Pressure'):
            self._parent = parent

        @property
        def stress(self):
            return self._parent._cast(_1703.Stress)

        @property
        def measurement_base(self):
            from mastapy.utility.units_and_measurements import _1594
            
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def pressure(self) -> 'Pressure':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Pressure.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Pressure._Cast_Pressure':
        return self._Cast_Pressure(self)
