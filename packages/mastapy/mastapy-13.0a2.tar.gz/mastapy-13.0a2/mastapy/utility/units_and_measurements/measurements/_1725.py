"""_1725.py

Volume
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VOLUME = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Volume')


__docformat__ = 'restructuredtext en'
__all__ = ('Volume',)


class Volume(_1594.MeasurementBase):
    """Volume

    This is a mastapy class.
    """

    TYPE = _VOLUME

    class _Cast_Volume:
        """Special nested class for casting Volume to subclasses."""

        def __init__(self, parent: 'Volume'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def volume(self) -> 'Volume':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Volume.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Volume._Cast_Volume':
        return self._Cast_Volume(self)
