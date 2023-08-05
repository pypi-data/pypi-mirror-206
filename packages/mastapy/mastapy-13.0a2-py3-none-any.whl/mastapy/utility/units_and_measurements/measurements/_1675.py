"""_1675.py

MomentOfInertiaPerUnitLength
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOMENT_OF_INERTIA_PER_UNIT_LENGTH = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MomentOfInertiaPerUnitLength')


__docformat__ = 'restructuredtext en'
__all__ = ('MomentOfInertiaPerUnitLength',)


class MomentOfInertiaPerUnitLength(_1594.MeasurementBase):
    """MomentOfInertiaPerUnitLength

    This is a mastapy class.
    """

    TYPE = _MOMENT_OF_INERTIA_PER_UNIT_LENGTH

    class _Cast_MomentOfInertiaPerUnitLength:
        """Special nested class for casting MomentOfInertiaPerUnitLength to subclasses."""

        def __init__(self, parent: 'MomentOfInertiaPerUnitLength'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def moment_of_inertia_per_unit_length(self) -> 'MomentOfInertiaPerUnitLength':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MomentOfInertiaPerUnitLength.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MomentOfInertiaPerUnitLength._Cast_MomentOfInertiaPerUnitLength':
        return self._Cast_MomentOfInertiaPerUnitLength(self)
