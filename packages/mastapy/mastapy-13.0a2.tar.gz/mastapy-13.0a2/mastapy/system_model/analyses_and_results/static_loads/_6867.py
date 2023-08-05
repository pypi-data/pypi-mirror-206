"""_6867.py

HarmonicLoadDataJMAGImport
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6862, _6845
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_JMAG_IMPORT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HarmonicLoadDataJMAGImport')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicLoadDataJMAGImport',)


class HarmonicLoadDataJMAGImport(_6862.HarmonicLoadDataCSVImport['_6845.ElectricMachineHarmonicLoadJMAGImportOptions']):
    """HarmonicLoadDataJMAGImport

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_JMAG_IMPORT

    class _Cast_HarmonicLoadDataJMAGImport:
        """Special nested class for casting HarmonicLoadDataJMAGImport to subclasses."""

        def __init__(self, parent: 'HarmonicLoadDataJMAGImport'):
            self._parent = parent

        @property
        def harmonic_load_data_csv_import(self):
            return self._parent._cast(_6862.HarmonicLoadDataCSVImport)

        @property
        def harmonic_load_data_import_from_motor_packages(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6866
            
            return self._parent._cast(_6866.HarmonicLoadDataImportFromMotorPackages)

        @property
        def harmonic_load_data_import_base(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6865
            
            return self._parent._cast(_6865.HarmonicLoadDataImportBase)

        @property
        def harmonic_load_data_jmag_import(self) -> 'HarmonicLoadDataJMAGImport':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicLoadDataJMAGImport.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def select_jmag_file(self):
        """ 'SelectJMAGFile' is the original name of this method."""

        self.wrapped.SelectJMAGFile()

    @property
    def cast_to(self) -> 'HarmonicLoadDataJMAGImport._Cast_HarmonicLoadDataJMAGImport':
        return self._Cast_HarmonicLoadDataJMAGImport(self)
