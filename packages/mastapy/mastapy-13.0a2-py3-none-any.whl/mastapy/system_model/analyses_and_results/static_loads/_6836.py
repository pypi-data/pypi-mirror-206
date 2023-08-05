"""_6836.py

ElectricMachineHarmonicLoadDataFromExcel
"""
from mastapy.system_model.analyses_and_results.static_loads import _6835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_EXCEL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadDataFromExcel')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadDataFromExcel',)


class ElectricMachineHarmonicLoadDataFromExcel(_6835.ElectricMachineHarmonicLoadData):
    """ElectricMachineHarmonicLoadDataFromExcel

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_EXCEL

    class _Cast_ElectricMachineHarmonicLoadDataFromExcel:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromExcel to subclasses."""

        def __init__(self, parent: 'ElectricMachineHarmonicLoadDataFromExcel'):
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
        def electric_machine_harmonic_load_data_from_excel(self) -> 'ElectricMachineHarmonicLoadDataFromExcel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadDataFromExcel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineHarmonicLoadDataFromExcel._Cast_ElectricMachineHarmonicLoadDataFromExcel':
        return self._Cast_ElectricMachineHarmonicLoadDataFromExcel(self)
