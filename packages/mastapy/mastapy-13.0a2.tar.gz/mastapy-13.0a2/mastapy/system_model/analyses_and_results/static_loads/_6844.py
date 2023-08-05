"""_6844.py

ElectricMachineHarmonicLoadImportOptionsBase
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_IMPORT_OPTIONS_BASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadImportOptionsBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadImportOptionsBase',)


class ElectricMachineHarmonicLoadImportOptionsBase(_0.APIBase):
    """ElectricMachineHarmonicLoadImportOptionsBase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_IMPORT_OPTIONS_BASE

    class _Cast_ElectricMachineHarmonicLoadImportOptionsBase:
        """Special nested class for casting ElectricMachineHarmonicLoadImportOptionsBase to subclasses."""

        def __init__(self, parent: 'ElectricMachineHarmonicLoadImportOptionsBase'):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_excel_import_options(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6842
            
            return self._parent._cast(_6842.ElectricMachineHarmonicLoadExcelImportOptions)

        @property
        def electric_machine_harmonic_load_flux_import_options(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6843
            
            return self._parent._cast(_6843.ElectricMachineHarmonicLoadFluxImportOptions)

        @property
        def electric_machine_harmonic_load_jmag_import_options(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6845
            
            return self._parent._cast(_6845.ElectricMachineHarmonicLoadJMAGImportOptions)

        @property
        def electric_machine_harmonic_load_motor_cad_import_options(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6846
            
            return self._parent._cast(_6846.ElectricMachineHarmonicLoadMotorCADImportOptions)

        @property
        def electric_machine_harmonic_load_import_options_base(self) -> 'ElectricMachineHarmonicLoadImportOptionsBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadImportOptionsBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineHarmonicLoadImportOptionsBase._Cast_ElectricMachineHarmonicLoadImportOptionsBase':
        return self._Cast_ElectricMachineHarmonicLoadImportOptionsBase(self)
