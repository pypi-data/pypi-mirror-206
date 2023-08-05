"""_323.py

GearNurbSurface
"""
from mastapy.gears import _316
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_NURB_SURFACE = python_net_import('SMT.MastaAPI.Gears', 'GearNurbSurface')


__docformat__ = 'restructuredtext en'
__all__ = ('GearNurbSurface',)


class GearNurbSurface(_316.ConicalGearToothSurface):
    """GearNurbSurface

    This is a mastapy class.
    """

    TYPE = _GEAR_NURB_SURFACE

    class _Cast_GearNurbSurface:
        """Special nested class for casting GearNurbSurface to subclasses."""

        def __init__(self, parent: 'GearNurbSurface'):
            self._parent = parent

        @property
        def conical_gear_tooth_surface(self):
            return self._parent._cast(_316.ConicalGearToothSurface)

        @property
        def gear_nurb_surface(self) -> 'GearNurbSurface':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearNurbSurface.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearNurbSurface._Cast_GearNurbSurface':
        return self._Cast_GearNurbSurface(self)
