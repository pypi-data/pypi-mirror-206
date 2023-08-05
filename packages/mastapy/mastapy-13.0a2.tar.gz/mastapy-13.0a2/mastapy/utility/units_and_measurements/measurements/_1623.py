"""_1623.py

ElectricalResistivity
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRICAL_RESISTIVITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'ElectricalResistivity')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricalResistivity',)


class ElectricalResistivity(_1594.MeasurementBase):
    """ElectricalResistivity

    This is a mastapy class.
    """

    TYPE = _ELECTRICAL_RESISTIVITY

    class _Cast_ElectricalResistivity:
        """Special nested class for casting ElectricalResistivity to subclasses."""

        def __init__(self, parent: 'ElectricalResistivity'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def electrical_resistivity(self) -> 'ElectricalResistivity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricalResistivity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricalResistivity._Cast_ElectricalResistivity':
        return self._Cast_ElectricalResistivity(self)
