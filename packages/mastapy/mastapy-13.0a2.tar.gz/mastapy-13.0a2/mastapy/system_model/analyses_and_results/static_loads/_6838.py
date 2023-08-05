"""_6838.py

ElectricMachineHarmonicLoadDataFromJMAG
"""
from mastapy.system_model.analyses_and_results.static_loads import _6841, _6845
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_JMAG = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadDataFromJMAG')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadDataFromJMAG',)


class ElectricMachineHarmonicLoadDataFromJMAG(_6841.ElectricMachineHarmonicLoadDataFromMotorPackages['_6845.ElectricMachineHarmonicLoadJMAGImportOptions']):
    """ElectricMachineHarmonicLoadDataFromJMAG

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_JMAG

    class _Cast_ElectricMachineHarmonicLoadDataFromJMAG:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromJMAG to subclasses."""

        def __init__(self, parent: 'ElectricMachineHarmonicLoadDataFromJMAG'):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(self):
            return self._parent._cast(_6841.ElectricMachineHarmonicLoadDataFromMotorPackages)

        @property
        def electric_machine_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6835
            
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
        def electric_machine_harmonic_load_data_from_jmag(self) -> 'ElectricMachineHarmonicLoadDataFromJMAG':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadDataFromJMAG.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineHarmonicLoadDataFromJMAG._Cast_ElectricMachineHarmonicLoadDataFromJMAG':
        return self._Cast_ElectricMachineHarmonicLoadDataFromJMAG(self)
