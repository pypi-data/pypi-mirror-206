"""_1644.py

HeatTransferResistance
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HEAT_TRANSFER_RESISTANCE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'HeatTransferResistance')


__docformat__ = 'restructuredtext en'
__all__ = ('HeatTransferResistance',)


class HeatTransferResistance(_1594.MeasurementBase):
    """HeatTransferResistance

    This is a mastapy class.
    """

    TYPE = _HEAT_TRANSFER_RESISTANCE

    class _Cast_HeatTransferResistance:
        """Special nested class for casting HeatTransferResistance to subclasses."""

        def __init__(self, parent: 'HeatTransferResistance'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def heat_transfer_resistance(self) -> 'HeatTransferResistance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HeatTransferResistance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'HeatTransferResistance._Cast_HeatTransferResistance':
        return self._Cast_HeatTransferResistance(self)
