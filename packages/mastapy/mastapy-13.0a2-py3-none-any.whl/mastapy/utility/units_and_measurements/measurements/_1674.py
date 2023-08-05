"""_1674.py

MomentOfInertia
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOMENT_OF_INERTIA = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MomentOfInertia')


__docformat__ = 'restructuredtext en'
__all__ = ('MomentOfInertia',)


class MomentOfInertia(_1594.MeasurementBase):
    """MomentOfInertia

    This is a mastapy class.
    """

    TYPE = _MOMENT_OF_INERTIA

    class _Cast_MomentOfInertia:
        """Special nested class for casting MomentOfInertia to subclasses."""

        def __init__(self, parent: 'MomentOfInertia'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def moment_of_inertia(self) -> 'MomentOfInertia':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MomentOfInertia.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MomentOfInertia._Cast_MomentOfInertia':
        return self._Cast_MomentOfInertia(self)
