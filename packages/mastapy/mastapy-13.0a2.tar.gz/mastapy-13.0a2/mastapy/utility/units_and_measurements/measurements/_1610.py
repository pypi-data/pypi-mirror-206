"""_1610.py

AngularVelocity
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_VELOCITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'AngularVelocity')


__docformat__ = 'restructuredtext en'
__all__ = ('AngularVelocity',)


class AngularVelocity(_1594.MeasurementBase):
    """AngularVelocity

    This is a mastapy class.
    """

    TYPE = _ANGULAR_VELOCITY

    class _Cast_AngularVelocity:
        """Special nested class for casting AngularVelocity to subclasses."""

        def __init__(self, parent: 'AngularVelocity'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def angular_velocity(self) -> 'AngularVelocity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AngularVelocity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AngularVelocity._Cast_AngularVelocity':
        return self._Cast_AngularVelocity(self)
