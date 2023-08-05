"""_1684.py

PowerSmallPerMass
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_SMALL_PER_MASS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'PowerSmallPerMass')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerSmallPerMass',)


class PowerSmallPerMass(_1594.MeasurementBase):
    """PowerSmallPerMass

    This is a mastapy class.
    """

    TYPE = _POWER_SMALL_PER_MASS

    class _Cast_PowerSmallPerMass:
        """Special nested class for casting PowerSmallPerMass to subclasses."""

        def __init__(self, parent: 'PowerSmallPerMass'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def power_small_per_mass(self) -> 'PowerSmallPerMass':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PowerSmallPerMass.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PowerSmallPerMass._Cast_PowerSmallPerMass':
        return self._Cast_PowerSmallPerMass(self)
