"""_558.py

SpiralBevelRateableGear
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_RATEABLE_GEAR = python_net_import('SMT.MastaAPI.Gears.Rating.Bevel.Standards', 'SpiralBevelRateableGear')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelRateableGear',)


class SpiralBevelRateableGear(_0.APIBase):
    """SpiralBevelRateableGear

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_RATEABLE_GEAR

    class _Cast_SpiralBevelRateableGear:
        """Special nested class for casting SpiralBevelRateableGear to subclasses."""

        def __init__(self, parent: 'SpiralBevelRateableGear'):
            self._parent = parent

        @property
        def spiral_bevel_rateable_gear(self) -> 'SpiralBevelRateableGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelRateableGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_blank_temperature(self) -> 'float':
        """float: 'GearBlankTemperature' is the original name of this property."""

        temp = self.wrapped.GearBlankTemperature

        if temp is None:
            return 0.0

        return temp

    @gear_blank_temperature.setter
    def gear_blank_temperature(self, value: 'float'):
        self.wrapped.GearBlankTemperature = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'SpiralBevelRateableGear._Cast_SpiralBevelRateableGear':
        return self._Cast_SpiralBevelRateableGear(self)
