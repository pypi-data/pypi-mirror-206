"""_1721.py

VelocitySmall
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VELOCITY_SMALL = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'VelocitySmall')


__docformat__ = 'restructuredtext en'
__all__ = ('VelocitySmall',)


class VelocitySmall(_1594.MeasurementBase):
    """VelocitySmall

    This is a mastapy class.
    """

    TYPE = _VELOCITY_SMALL

    class _Cast_VelocitySmall:
        """Special nested class for casting VelocitySmall to subclasses."""

        def __init__(self, parent: 'VelocitySmall'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def velocity_small(self) -> 'VelocitySmall':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VelocitySmall.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'VelocitySmall._Cast_VelocitySmall':
        return self._Cast_VelocitySmall(self)
