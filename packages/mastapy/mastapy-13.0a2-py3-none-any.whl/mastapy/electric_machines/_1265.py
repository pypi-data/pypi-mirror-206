"""_1265.py

HarmonicLoadDataControlExcitationOptionForElectricMachineMode
"""
from mastapy.electric_machines.harmonic_load_data import _1369
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_CONTROL_EXCITATION_OPTION_FOR_ELECTRIC_MACHINE_MODE = python_net_import('SMT.MastaAPI.ElectricMachines', 'HarmonicLoadDataControlExcitationOptionForElectricMachineMode')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicLoadDataControlExcitationOptionForElectricMachineMode',)


class HarmonicLoadDataControlExcitationOptionForElectricMachineMode(_1369.HarmonicLoadDataControlExcitationOptionBase):
    """HarmonicLoadDataControlExcitationOptionForElectricMachineMode

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_CONTROL_EXCITATION_OPTION_FOR_ELECTRIC_MACHINE_MODE

    class _Cast_HarmonicLoadDataControlExcitationOptionForElectricMachineMode:
        """Special nested class for casting HarmonicLoadDataControlExcitationOptionForElectricMachineMode to subclasses."""

        def __init__(self, parent: 'HarmonicLoadDataControlExcitationOptionForElectricMachineMode'):
            self._parent = parent

        @property
        def harmonic_load_data_control_excitation_option_base(self):
            return self._parent._cast(_1369.HarmonicLoadDataControlExcitationOptionBase)

        @property
        def harmonic_load_data_control_excitation_option_for_electric_machine_mode(self) -> 'HarmonicLoadDataControlExcitationOptionForElectricMachineMode':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicLoadDataControlExcitationOptionForElectricMachineMode.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'HarmonicLoadDataControlExcitationOptionForElectricMachineMode._Cast_HarmonicLoadDataControlExcitationOptionForElectricMachineMode':
        return self._Cast_HarmonicLoadDataControlExcitationOptionForElectricMachineMode(self)
