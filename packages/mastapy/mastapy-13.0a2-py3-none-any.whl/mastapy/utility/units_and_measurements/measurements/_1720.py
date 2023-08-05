"""_1720.py

Velocity
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VELOCITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Velocity')


__docformat__ = 'restructuredtext en'
__all__ = ('Velocity',)


class Velocity(_1594.MeasurementBase):
    """Velocity

    This is a mastapy class.
    """

    TYPE = _VELOCITY

    class _Cast_Velocity:
        """Special nested class for casting Velocity to subclasses."""

        def __init__(self, parent: 'Velocity'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def velocity(self) -> 'Velocity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Velocity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Velocity._Cast_Velocity':
        return self._Cast_Velocity(self)
