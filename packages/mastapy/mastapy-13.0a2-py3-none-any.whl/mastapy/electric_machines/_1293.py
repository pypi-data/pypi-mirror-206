"""_1293.py

SurfacePermanentMagnetMachine
"""
from mastapy.electric_machines import _1294, _1276
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SURFACE_PERMANENT_MAGNET_MACHINE = python_net_import('SMT.MastaAPI.ElectricMachines', 'SurfacePermanentMagnetMachine')


__docformat__ = 'restructuredtext en'
__all__ = ('SurfacePermanentMagnetMachine',)


class SurfacePermanentMagnetMachine(_1276.NonCADElectricMachineDetail):
    """SurfacePermanentMagnetMachine

    This is a mastapy class.
    """

    TYPE = _SURFACE_PERMANENT_MAGNET_MACHINE

    class _Cast_SurfacePermanentMagnetMachine:
        """Special nested class for casting SurfacePermanentMagnetMachine to subclasses."""

        def __init__(self, parent: 'SurfacePermanentMagnetMachine'):
            self._parent = parent

        @property
        def non_cad_electric_machine_detail(self):
            return self._parent._cast(_1276.NonCADElectricMachineDetail)

        @property
        def electric_machine_detail(self):
            from mastapy.electric_machines import _1254
            
            return self._parent._cast(_1254.ElectricMachineDetail)

        @property
        def surface_permanent_magnet_machine(self) -> 'SurfacePermanentMagnetMachine':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SurfacePermanentMagnetMachine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor(self) -> '_1294.SurfacePermanentMagnetRotor':
        """SurfacePermanentMagnetRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rotor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SurfacePermanentMagnetMachine._Cast_SurfacePermanentMagnetMachine':
        return self._Cast_SurfacePermanentMagnetMachine(self)
