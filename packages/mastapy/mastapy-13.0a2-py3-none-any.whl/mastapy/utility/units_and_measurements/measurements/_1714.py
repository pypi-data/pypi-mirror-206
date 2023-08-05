"""_1714.py

Torque
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Torque')


__docformat__ = 'restructuredtext en'
__all__ = ('Torque',)


class Torque(_1594.MeasurementBase):
    """Torque

    This is a mastapy class.
    """

    TYPE = _TORQUE

    class _Cast_Torque:
        """Special nested class for casting Torque to subclasses."""

        def __init__(self, parent: 'Torque'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def torque(self) -> 'Torque':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Torque.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Torque._Cast_Torque':
        return self._Cast_Torque(self)
