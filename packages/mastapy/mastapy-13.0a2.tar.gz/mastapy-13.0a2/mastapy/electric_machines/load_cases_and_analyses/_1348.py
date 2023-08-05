"""_1348.py

ElectricMachineMechanicalLoadCase
"""
from mastapy._internal import constructor
from mastapy.electric_machines.load_cases_and_analyses import _1346
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_MECHANICAL_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineMechanicalLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineMechanicalLoadCase',)


class ElectricMachineMechanicalLoadCase(_1346.ElectricMachineLoadCaseBase):
    """ElectricMachineMechanicalLoadCase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_MECHANICAL_LOAD_CASE

    class _Cast_ElectricMachineMechanicalLoadCase:
        """Special nested class for casting ElectricMachineMechanicalLoadCase to subclasses."""

        def __init__(self, parent: 'ElectricMachineMechanicalLoadCase'):
            self._parent = parent

        @property
        def electric_machine_load_case_base(self):
            return self._parent._cast(_1346.ElectricMachineLoadCaseBase)

        @property
        def electric_machine_mechanical_load_case(self) -> 'ElectricMachineMechanicalLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineMechanicalLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def speed(self) -> 'float':
        """float: 'Speed' is the original name of this property."""

        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @speed.setter
    def speed(self, value: 'float'):
        self.wrapped.Speed = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'ElectricMachineMechanicalLoadCase._Cast_ElectricMachineMechanicalLoadCase':
        return self._Cast_ElectricMachineMechanicalLoadCase(self)
