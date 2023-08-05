"""_6841.py

ElectricMachineHarmonicLoadDataFromMotorPackages
"""
from typing import TypeVar, Generic

from mastapy.system_model.analyses_and_results.static_loads import _6835, _6844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_PACKAGES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadDataFromMotorPackages')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadDataFromMotorPackages',)


T = TypeVar('T', bound='_6844.ElectricMachineHarmonicLoadImportOptionsBase')


class ElectricMachineHarmonicLoadDataFromMotorPackages(_6835.ElectricMachineHarmonicLoadData, Generic[T]):
    """ElectricMachineHarmonicLoadDataFromMotorPackages

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_PACKAGES

    class _Cast_ElectricMachineHarmonicLoadDataFromMotorPackages:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromMotorPackages to subclasses."""

        def __init__(self, parent: 'ElectricMachineHarmonicLoadDataFromMotorPackages'):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_data(self):
            return self._parent._cast(_6835.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_base(self):
            from mastapy.electric_machines.harmonic_load_data import _1366
            
            return self._parent._cast(_1366.ElectricMachineHarmonicLoadDataBase)

        @property
        def speed_dependent_harmonic_load_data(self):
            from mastapy.electric_machines.harmonic_load_data import _1371
            
            return self._parent._cast(_1371.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(self):
            from mastapy.electric_machines.harmonic_load_data import _1368
            
            return self._parent._cast(_1368.HarmonicLoadDataBase)

        @property
        def electric_machine_harmonic_load_data_from_flux(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6837
            
            return self._parent._cast(_6837.ElectricMachineHarmonicLoadDataFromFlux)

        @property
        def electric_machine_harmonic_load_data_from_jmag(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6838
            
            return self._parent._cast(_6838.ElectricMachineHarmonicLoadDataFromJMAG)

        @property
        def electric_machine_harmonic_load_data_from_motor_cad(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6840
            
            return self._parent._cast(_6840.ElectricMachineHarmonicLoadDataFromMotorCAD)

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(self) -> 'ElectricMachineHarmonicLoadDataFromMotorPackages':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadDataFromMotorPackages.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages':
        return self._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages(self)
