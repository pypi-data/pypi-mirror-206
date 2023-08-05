"""_1268.py

InteriorPermanentMagnetMachine
"""
from mastapy.electric_machines import _1267, _1276
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERIOR_PERMANENT_MAGNET_MACHINE = python_net_import('SMT.MastaAPI.ElectricMachines', 'InteriorPermanentMagnetMachine')


__docformat__ = 'restructuredtext en'
__all__ = ('InteriorPermanentMagnetMachine',)


class InteriorPermanentMagnetMachine(_1276.NonCADElectricMachineDetail):
    """InteriorPermanentMagnetMachine

    This is a mastapy class.
    """

    TYPE = _INTERIOR_PERMANENT_MAGNET_MACHINE

    class _Cast_InteriorPermanentMagnetMachine:
        """Special nested class for casting InteriorPermanentMagnetMachine to subclasses."""

        def __init__(self, parent: 'InteriorPermanentMagnetMachine'):
            self._parent = parent

        @property
        def non_cad_electric_machine_detail(self):
            return self._parent._cast(_1276.NonCADElectricMachineDetail)

        @property
        def electric_machine_detail(self):
            from mastapy.electric_machines import _1254
            
            return self._parent._cast(_1254.ElectricMachineDetail)

        @property
        def interior_permanent_magnet_machine(self) -> 'InteriorPermanentMagnetMachine':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InteriorPermanentMagnetMachine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor(self) -> '_1267.InteriorPermanentMagnetAndSynchronousReluctanceRotor':
        """InteriorPermanentMagnetAndSynchronousReluctanceRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rotor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'InteriorPermanentMagnetMachine._Cast_InteriorPermanentMagnetMachine':
        return self._Cast_InteriorPermanentMagnetMachine(self)
