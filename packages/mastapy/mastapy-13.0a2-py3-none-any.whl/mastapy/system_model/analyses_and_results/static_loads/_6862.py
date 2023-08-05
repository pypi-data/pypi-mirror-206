"""_6862.py

HarmonicLoadDataCSVImport
"""
from typing import List, TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6832, _6866, _6844
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_CSV_IMPORT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HarmonicLoadDataCSVImport')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicLoadDataCSVImport',)


T = TypeVar('T', bound='_6844.ElectricMachineHarmonicLoadImportOptionsBase')


class HarmonicLoadDataCSVImport(_6866.HarmonicLoadDataImportFromMotorPackages[T]):
    """HarmonicLoadDataCSVImport

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _HARMONIC_LOAD_DATA_CSV_IMPORT

    class _Cast_HarmonicLoadDataCSVImport:
        """Special nested class for casting HarmonicLoadDataCSVImport to subclasses."""

        def __init__(self, parent: 'HarmonicLoadDataCSVImport'):
            self._parent = parent

        @property
        def harmonic_load_data_import_from_motor_packages(self):
            return self._parent._cast(_6866.HarmonicLoadDataImportFromMotorPackages)

        @property
        def harmonic_load_data_import_base(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6865
            
            return self._parent._cast(_6865.HarmonicLoadDataImportBase)

        @property
        def harmonic_load_data_flux_import(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6864
            
            return self._parent._cast(_6864.HarmonicLoadDataFluxImport)

        @property
        def harmonic_load_data_jmag_import(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6867
            
            return self._parent._cast(_6867.HarmonicLoadDataJMAGImport)

        @property
        def harmonic_load_data_csv_import(self) -> 'HarmonicLoadDataCSVImport':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicLoadDataCSVImport.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electric_machine_data_per_speed(self) -> 'List[_6832.DataFromMotorPackagePerSpeed]':
        """List[DataFromMotorPackagePerSpeed]: 'ElectricMachineDataPerSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDataPerSpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport':
        return self._Cast_HarmonicLoadDataCSVImport(self)
