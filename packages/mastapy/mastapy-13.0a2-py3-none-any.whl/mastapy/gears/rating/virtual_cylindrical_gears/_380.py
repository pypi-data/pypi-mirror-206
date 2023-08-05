"""_380.py

KlingelnbergHypoidVirtualCylindricalGear
"""
from mastapy.gears.rating.virtual_cylindrical_gears import _382
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_HYPOID_VIRTUAL_CYLINDRICAL_GEAR = python_net_import('SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears', 'KlingelnbergHypoidVirtualCylindricalGear')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergHypoidVirtualCylindricalGear',)


class KlingelnbergHypoidVirtualCylindricalGear(_382.KlingelnbergVirtualCylindricalGear):
    """KlingelnbergHypoidVirtualCylindricalGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_HYPOID_VIRTUAL_CYLINDRICAL_GEAR

    class _Cast_KlingelnbergHypoidVirtualCylindricalGear:
        """Special nested class for casting KlingelnbergHypoidVirtualCylindricalGear to subclasses."""

        def __init__(self, parent: 'KlingelnbergHypoidVirtualCylindricalGear'):
            self._parent = parent

        @property
        def klingelnberg_virtual_cylindrical_gear(self):
            return self._parent._cast(_382.KlingelnbergVirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _384
            
            return self._parent._cast(_384.VirtualCylindricalGear)

        @property
        def virtual_cylindrical_gear_basic(self):
            from mastapy.gears.rating.virtual_cylindrical_gears import _385
            
            return self._parent._cast(_385.VirtualCylindricalGearBasic)

        @property
        def klingelnberg_hypoid_virtual_cylindrical_gear(self) -> 'KlingelnbergHypoidVirtualCylindricalGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergHypoidVirtualCylindricalGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KlingelnbergHypoidVirtualCylindricalGear._Cast_KlingelnbergHypoidVirtualCylindricalGear':
        return self._Cast_KlingelnbergHypoidVirtualCylindricalGear(self)
