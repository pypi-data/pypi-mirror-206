"""_6839.py

ElectricMachineHarmonicLoadDataFromMasta
"""
from mastapy.system_model.analyses_and_results.static_loads import _6835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MASTA = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadDataFromMasta')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadDataFromMasta',)


class ElectricMachineHarmonicLoadDataFromMasta(_6835.ElectricMachineHarmonicLoadData):
    """ElectricMachineHarmonicLoadDataFromMasta

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MASTA

    class _Cast_ElectricMachineHarmonicLoadDataFromMasta:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromMasta to subclasses."""

        def __init__(self, parent: 'ElectricMachineHarmonicLoadDataFromMasta'):
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
        def electric_machine_harmonic_load_data_from_masta(self) -> 'ElectricMachineHarmonicLoadDataFromMasta':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadDataFromMasta.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineHarmonicLoadDataFromMasta._Cast_ElectricMachineHarmonicLoadDataFromMasta':
        return self._Cast_ElectricMachineHarmonicLoadDataFromMasta(self)
