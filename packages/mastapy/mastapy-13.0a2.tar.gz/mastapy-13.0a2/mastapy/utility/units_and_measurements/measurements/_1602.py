"""_1602.py

Angle
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGLE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Angle')


__docformat__ = 'restructuredtext en'
__all__ = ('Angle',)


class Angle(_1594.MeasurementBase):
    """Angle

    This is a mastapy class.
    """

    TYPE = _ANGLE

    class _Cast_Angle:
        """Special nested class for casting Angle to subclasses."""

        def __init__(self, parent: 'Angle'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def angle(self) -> 'Angle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Angle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Angle._Cast_Angle':
        return self._Cast_Angle(self)
