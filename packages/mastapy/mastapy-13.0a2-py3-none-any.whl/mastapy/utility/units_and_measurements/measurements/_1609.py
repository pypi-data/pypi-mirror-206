"""_1609.py

AngularStiffness
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_STIFFNESS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'AngularStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('AngularStiffness',)


class AngularStiffness(_1594.MeasurementBase):
    """AngularStiffness

    This is a mastapy class.
    """

    TYPE = _ANGULAR_STIFFNESS

    class _Cast_AngularStiffness:
        """Special nested class for casting AngularStiffness to subclasses."""

        def __init__(self, parent: 'AngularStiffness'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def angular_stiffness(self) -> 'AngularStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AngularStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AngularStiffness._Cast_AngularStiffness':
        return self._Cast_AngularStiffness(self)
