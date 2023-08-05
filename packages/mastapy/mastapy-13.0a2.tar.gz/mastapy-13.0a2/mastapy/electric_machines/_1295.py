"""_1295.py

SynchronousReluctanceMachine
"""
from mastapy.electric_machines import _1267, _1276
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONOUS_RELUCTANCE_MACHINE = python_net_import('SMT.MastaAPI.ElectricMachines', 'SynchronousReluctanceMachine')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchronousReluctanceMachine',)


class SynchronousReluctanceMachine(_1276.NonCADElectricMachineDetail):
    """SynchronousReluctanceMachine

    This is a mastapy class.
    """

    TYPE = _SYNCHRONOUS_RELUCTANCE_MACHINE

    class _Cast_SynchronousReluctanceMachine:
        """Special nested class for casting SynchronousReluctanceMachine to subclasses."""

        def __init__(self, parent: 'SynchronousReluctanceMachine'):
            self._parent = parent

        @property
        def non_cad_electric_machine_detail(self):
            return self._parent._cast(_1276.NonCADElectricMachineDetail)

        @property
        def electric_machine_detail(self):
            from mastapy.electric_machines import _1254
            
            return self._parent._cast(_1254.ElectricMachineDetail)

        @property
        def synchronous_reluctance_machine(self) -> 'SynchronousReluctanceMachine':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchronousReluctanceMachine.TYPE'):
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
    def cast_to(self) -> 'SynchronousReluctanceMachine._Cast_SynchronousReluctanceMachine':
        return self._Cast_SynchronousReluctanceMachine(self)
