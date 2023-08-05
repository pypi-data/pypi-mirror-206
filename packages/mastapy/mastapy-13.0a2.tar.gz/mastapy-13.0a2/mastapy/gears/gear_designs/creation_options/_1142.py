"""_1142.py

HypoidGearSetCreationOptions
"""
from mastapy.gears.gear_designs.creation_options import _1141
from mastapy.gears.gear_designs.hypoid import _982
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.CreationOptions', 'HypoidGearSetCreationOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetCreationOptions',)


class HypoidGearSetCreationOptions(_1141.GearSetCreationOptions['_982.HypoidGearSetDesign']):
    """HypoidGearSetCreationOptions

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_CREATION_OPTIONS

    class _Cast_HypoidGearSetCreationOptions:
        """Special nested class for casting HypoidGearSetCreationOptions to subclasses."""

        def __init__(self, parent: 'HypoidGearSetCreationOptions'):
            self._parent = parent

        @property
        def gear_set_creation_options(self):
            return self._parent._cast(_1141.GearSetCreationOptions)

        @property
        def hypoid_gear_set_creation_options(self) -> 'HypoidGearSetCreationOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearSetCreationOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'HypoidGearSetCreationOptions._Cast_HypoidGearSetCreationOptions':
        return self._Cast_HypoidGearSetCreationOptions(self)
