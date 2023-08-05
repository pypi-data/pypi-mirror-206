"""_1616.py

Cycles
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLES = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Cycles')


__docformat__ = 'restructuredtext en'
__all__ = ('Cycles',)


class Cycles(_1594.MeasurementBase):
    """Cycles

    This is a mastapy class.
    """

    TYPE = _CYCLES

    class _Cast_Cycles:
        """Special nested class for casting Cycles to subclasses."""

        def __init__(self, parent: 'Cycles'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def cycles(self) -> 'Cycles':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Cycles.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Cycles._Cast_Cycles':
        return self._Cast_Cycles(self)
