"""_1632.py

ForcePerUnitLength
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_PER_UNIT_LENGTH = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'ForcePerUnitLength')


__docformat__ = 'restructuredtext en'
__all__ = ('ForcePerUnitLength',)


class ForcePerUnitLength(_1594.MeasurementBase):
    """ForcePerUnitLength

    This is a mastapy class.
    """

    TYPE = _FORCE_PER_UNIT_LENGTH

    class _Cast_ForcePerUnitLength:
        """Special nested class for casting ForcePerUnitLength to subclasses."""

        def __init__(self, parent: 'ForcePerUnitLength'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def force_per_unit_length(self) -> 'ForcePerUnitLength':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ForcePerUnitLength.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ForcePerUnitLength._Cast_ForcePerUnitLength':
        return self._Cast_ForcePerUnitLength(self)
