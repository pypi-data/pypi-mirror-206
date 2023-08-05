"""_1622.py

ElectricalResistance
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRICAL_RESISTANCE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'ElectricalResistance')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricalResistance',)


class ElectricalResistance(_1594.MeasurementBase):
    """ElectricalResistance

    This is a mastapy class.
    """

    TYPE = _ELECTRICAL_RESISTANCE

    class _Cast_ElectricalResistance:
        """Special nested class for casting ElectricalResistance to subclasses."""

        def __init__(self, parent: 'ElectricalResistance'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def electrical_resistance(self) -> 'ElectricalResistance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricalResistance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricalResistance._Cast_ElectricalResistance':
        return self._Cast_ElectricalResistance(self)
