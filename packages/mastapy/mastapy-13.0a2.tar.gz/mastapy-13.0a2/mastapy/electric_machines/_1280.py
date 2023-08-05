"""_1280.py

PermanentMagnetRotor
"""
from mastapy.electric_machines import _1283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERMANENT_MAGNET_ROTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'PermanentMagnetRotor')


__docformat__ = 'restructuredtext en'
__all__ = ('PermanentMagnetRotor',)


class PermanentMagnetRotor(_1283.Rotor):
    """PermanentMagnetRotor

    This is a mastapy class.
    """

    TYPE = _PERMANENT_MAGNET_ROTOR

    class _Cast_PermanentMagnetRotor:
        """Special nested class for casting PermanentMagnetRotor to subclasses."""

        def __init__(self, parent: 'PermanentMagnetRotor'):
            self._parent = parent

        @property
        def rotor(self):
            return self._parent._cast(_1283.Rotor)

        @property
        def interior_permanent_magnet_and_synchronous_reluctance_rotor(self):
            from mastapy.electric_machines import _1267
            
            return self._parent._cast(_1267.InteriorPermanentMagnetAndSynchronousReluctanceRotor)

        @property
        def surface_permanent_magnet_rotor(self):
            from mastapy.electric_machines import _1294
            
            return self._parent._cast(_1294.SurfacePermanentMagnetRotor)

        @property
        def permanent_magnet_rotor(self) -> 'PermanentMagnetRotor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PermanentMagnetRotor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PermanentMagnetRotor._Cast_PermanentMagnetRotor':
        return self._Cast_PermanentMagnetRotor(self)
