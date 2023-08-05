"""_1608.py

AngularJerk
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_JERK = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'AngularJerk')


__docformat__ = 'restructuredtext en'
__all__ = ('AngularJerk',)


class AngularJerk(_1594.MeasurementBase):
    """AngularJerk

    This is a mastapy class.
    """

    TYPE = _ANGULAR_JERK

    class _Cast_AngularJerk:
        """Special nested class for casting AngularJerk to subclasses."""

        def __init__(self, parent: 'AngularJerk'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def angular_jerk(self) -> 'AngularJerk':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AngularJerk.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AngularJerk._Cast_AngularJerk':
        return self._Cast_AngularJerk(self)
