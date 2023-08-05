"""_1604.py

AngleSmall
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGLE_SMALL = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'AngleSmall')


__docformat__ = 'restructuredtext en'
__all__ = ('AngleSmall',)


class AngleSmall(_1594.MeasurementBase):
    """AngleSmall

    This is a mastapy class.
    """

    TYPE = _ANGLE_SMALL

    class _Cast_AngleSmall:
        """Special nested class for casting AngleSmall to subclasses."""

        def __init__(self, parent: 'AngleSmall'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def angle_small(self) -> 'AngleSmall':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AngleSmall.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AngleSmall._Cast_AngleSmall':
        return self._Cast_AngleSmall(self)
