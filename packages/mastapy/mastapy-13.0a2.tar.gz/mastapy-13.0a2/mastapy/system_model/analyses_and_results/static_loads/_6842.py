"""_6842.py

ElectricMachineHarmonicLoadExcelImportOptions
"""
from mastapy.system_model.analyses_and_results.static_loads import _6844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_EXCEL_IMPORT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadExcelImportOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadExcelImportOptions',)


class ElectricMachineHarmonicLoadExcelImportOptions(_6844.ElectricMachineHarmonicLoadImportOptionsBase):
    """ElectricMachineHarmonicLoadExcelImportOptions

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_EXCEL_IMPORT_OPTIONS

    class _Cast_ElectricMachineHarmonicLoadExcelImportOptions:
        """Special nested class for casting ElectricMachineHarmonicLoadExcelImportOptions to subclasses."""

        def __init__(self, parent: 'ElectricMachineHarmonicLoadExcelImportOptions'):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_import_options_base(self):
            return self._parent._cast(_6844.ElectricMachineHarmonicLoadImportOptionsBase)

        @property
        def electric_machine_harmonic_load_excel_import_options(self) -> 'ElectricMachineHarmonicLoadExcelImportOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadExcelImportOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineHarmonicLoadExcelImportOptions._Cast_ElectricMachineHarmonicLoadExcelImportOptions':
        return self._Cast_ElectricMachineHarmonicLoadExcelImportOptions(self)
