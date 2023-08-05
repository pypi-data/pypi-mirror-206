"""_6843.py

ElectricMachineHarmonicLoadFluxImportOptions
"""
from mastapy.system_model.analyses_and_results.static_loads import _6844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_FLUX_IMPORT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadFluxImportOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadFluxImportOptions',)


class ElectricMachineHarmonicLoadFluxImportOptions(_6844.ElectricMachineHarmonicLoadImportOptionsBase):
    """ElectricMachineHarmonicLoadFluxImportOptions

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_FLUX_IMPORT_OPTIONS

    class _Cast_ElectricMachineHarmonicLoadFluxImportOptions:
        """Special nested class for casting ElectricMachineHarmonicLoadFluxImportOptions to subclasses."""

        def __init__(self, parent: 'ElectricMachineHarmonicLoadFluxImportOptions'):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_import_options_base(self):
            return self._parent._cast(_6844.ElectricMachineHarmonicLoadImportOptionsBase)

        @property
        def electric_machine_harmonic_load_flux_import_options(self) -> 'ElectricMachineHarmonicLoadFluxImportOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadFluxImportOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineHarmonicLoadFluxImportOptions._Cast_ElectricMachineHarmonicLoadFluxImportOptions':
        return self._Cast_ElectricMachineHarmonicLoadFluxImportOptions(self)
