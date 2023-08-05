"""_1309.py

WoundFieldSynchronousMachine
"""
from mastapy.electric_machines import _1267, _1276
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WOUND_FIELD_SYNCHRONOUS_MACHINE = python_net_import('SMT.MastaAPI.ElectricMachines', 'WoundFieldSynchronousMachine')


__docformat__ = 'restructuredtext en'
__all__ = ('WoundFieldSynchronousMachine',)


class WoundFieldSynchronousMachine(_1276.NonCADElectricMachineDetail):
    """WoundFieldSynchronousMachine

    This is a mastapy class.
    """

    TYPE = _WOUND_FIELD_SYNCHRONOUS_MACHINE

    class _Cast_WoundFieldSynchronousMachine:
        """Special nested class for casting WoundFieldSynchronousMachine to subclasses."""

        def __init__(self, parent: 'WoundFieldSynchronousMachine'):
            self._parent = parent

        @property
        def non_cad_electric_machine_detail(self):
            return self._parent._cast(_1276.NonCADElectricMachineDetail)

        @property
        def electric_machine_detail(self):
            from mastapy.electric_machines import _1254
            
            return self._parent._cast(_1254.ElectricMachineDetail)

        @property
        def wound_field_synchronous_machine(self) -> 'WoundFieldSynchronousMachine':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WoundFieldSynchronousMachine.TYPE'):
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
    def cast_to(self) -> 'WoundFieldSynchronousMachine._Cast_WoundFieldSynchronousMachine':
        return self._Cast_WoundFieldSynchronousMachine(self)
