"""_1143.py

SpiralBevelGearSetCreationOptions
"""
from mastapy.gears.gear_designs.creation_options import _1141
from mastapy.gears.gear_designs.spiral_bevel import _966
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.CreationOptions', 'SpiralBevelGearSetCreationOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetCreationOptions',)


class SpiralBevelGearSetCreationOptions(_1141.GearSetCreationOptions['_966.SpiralBevelGearSetDesign']):
    """SpiralBevelGearSetCreationOptions

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_CREATION_OPTIONS

    class _Cast_SpiralBevelGearSetCreationOptions:
        """Special nested class for casting SpiralBevelGearSetCreationOptions to subclasses."""

        def __init__(self, parent: 'SpiralBevelGearSetCreationOptions'):
            self._parent = parent

        @property
        def gear_set_creation_options(self):
            return self._parent._cast(_1141.GearSetCreationOptions)

        @property
        def spiral_bevel_gear_set_creation_options(self) -> 'SpiralBevelGearSetCreationOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetCreationOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SpiralBevelGearSetCreationOptions._Cast_SpiralBevelGearSetCreationOptions':
        return self._Cast_SpiralBevelGearSetCreationOptions(self)
