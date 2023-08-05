"""_1672.py

MassPerUnitLength
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_PER_UNIT_LENGTH = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MassPerUnitLength')


__docformat__ = 'restructuredtext en'
__all__ = ('MassPerUnitLength',)


class MassPerUnitLength(_1594.MeasurementBase):
    """MassPerUnitLength

    This is a mastapy class.
    """

    TYPE = _MASS_PER_UNIT_LENGTH

    class _Cast_MassPerUnitLength:
        """Special nested class for casting MassPerUnitLength to subclasses."""

        def __init__(self, parent: 'MassPerUnitLength'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def mass_per_unit_length(self) -> 'MassPerUnitLength':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MassPerUnitLength.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MassPerUnitLength._Cast_MassPerUnitLength':
        return self._Cast_MassPerUnitLength(self)
