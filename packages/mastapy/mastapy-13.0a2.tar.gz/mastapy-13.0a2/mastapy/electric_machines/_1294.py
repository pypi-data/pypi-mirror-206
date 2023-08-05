"""_1294.py

SurfacePermanentMagnetRotor
"""
from mastapy.electric_machines import _1280
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SURFACE_PERMANENT_MAGNET_ROTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'SurfacePermanentMagnetRotor')


__docformat__ = 'restructuredtext en'
__all__ = ('SurfacePermanentMagnetRotor',)


class SurfacePermanentMagnetRotor(_1280.PermanentMagnetRotor):
    """SurfacePermanentMagnetRotor

    This is a mastapy class.
    """

    TYPE = _SURFACE_PERMANENT_MAGNET_ROTOR

    class _Cast_SurfacePermanentMagnetRotor:
        """Special nested class for casting SurfacePermanentMagnetRotor to subclasses."""

        def __init__(self, parent: 'SurfacePermanentMagnetRotor'):
            self._parent = parent

        @property
        def permanent_magnet_rotor(self):
            return self._parent._cast(_1280.PermanentMagnetRotor)

        @property
        def rotor(self):
            from mastapy.electric_machines import _1283
            
            return self._parent._cast(_1283.Rotor)

        @property
        def surface_permanent_magnet_rotor(self) -> 'SurfacePermanentMagnetRotor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SurfacePermanentMagnetRotor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SurfacePermanentMagnetRotor._Cast_SurfacePermanentMagnetRotor':
        return self._Cast_SurfacePermanentMagnetRotor(self)
