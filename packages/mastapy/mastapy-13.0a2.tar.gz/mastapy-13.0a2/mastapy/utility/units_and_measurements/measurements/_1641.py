"""_1641.py

HeatConductivity
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HEAT_CONDUCTIVITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'HeatConductivity')


__docformat__ = 'restructuredtext en'
__all__ = ('HeatConductivity',)


class HeatConductivity(_1594.MeasurementBase):
    """HeatConductivity

    This is a mastapy class.
    """

    TYPE = _HEAT_CONDUCTIVITY

    class _Cast_HeatConductivity:
        """Special nested class for casting HeatConductivity to subclasses."""

        def __init__(self, parent: 'HeatConductivity'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def heat_conductivity(self) -> 'HeatConductivity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HeatConductivity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'HeatConductivity._Cast_HeatConductivity':
        return self._Cast_HeatConductivity(self)
