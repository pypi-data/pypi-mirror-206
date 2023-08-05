"""_1642.py

HeatTransfer
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HEAT_TRANSFER = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'HeatTransfer')


__docformat__ = 'restructuredtext en'
__all__ = ('HeatTransfer',)


class HeatTransfer(_1594.MeasurementBase):
    """HeatTransfer

    This is a mastapy class.
    """

    TYPE = _HEAT_TRANSFER

    class _Cast_HeatTransfer:
        """Special nested class for casting HeatTransfer to subclasses."""

        def __init__(self, parent: 'HeatTransfer'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def heat_transfer(self) -> 'HeatTransfer':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HeatTransfer.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'HeatTransfer._Cast_HeatTransfer':
        return self._Cast_HeatTransfer(self)
