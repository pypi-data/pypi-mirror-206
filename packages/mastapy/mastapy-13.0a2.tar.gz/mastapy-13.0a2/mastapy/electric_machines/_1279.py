"""_1279.py

PermanentMagnetAssistedSynchronousReluctanceMachine
"""
from mastapy.electric_machines import _1267, _1276
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERMANENT_MAGNET_ASSISTED_SYNCHRONOUS_RELUCTANCE_MACHINE = python_net_import('SMT.MastaAPI.ElectricMachines', 'PermanentMagnetAssistedSynchronousReluctanceMachine')


__docformat__ = 'restructuredtext en'
__all__ = ('PermanentMagnetAssistedSynchronousReluctanceMachine',)


class PermanentMagnetAssistedSynchronousReluctanceMachine(_1276.NonCADElectricMachineDetail):
    """PermanentMagnetAssistedSynchronousReluctanceMachine

    This is a mastapy class.
    """

    TYPE = _PERMANENT_MAGNET_ASSISTED_SYNCHRONOUS_RELUCTANCE_MACHINE

    class _Cast_PermanentMagnetAssistedSynchronousReluctanceMachine:
        """Special nested class for casting PermanentMagnetAssistedSynchronousReluctanceMachine to subclasses."""

        def __init__(self, parent: 'PermanentMagnetAssistedSynchronousReluctanceMachine'):
            self._parent = parent

        @property
        def non_cad_electric_machine_detail(self):
            return self._parent._cast(_1276.NonCADElectricMachineDetail)

        @property
        def electric_machine_detail(self):
            from mastapy.electric_machines import _1254
            
            return self._parent._cast(_1254.ElectricMachineDetail)

        @property
        def permanent_magnet_assisted_synchronous_reluctance_machine(self) -> 'PermanentMagnetAssistedSynchronousReluctanceMachine':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PermanentMagnetAssistedSynchronousReluctanceMachine.TYPE'):
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
    def cast_to(self) -> 'PermanentMagnetAssistedSynchronousReluctanceMachine._Cast_PermanentMagnetAssistedSynchronousReluctanceMachine':
        return self._Cast_PermanentMagnetAssistedSynchronousReluctanceMachine(self)
