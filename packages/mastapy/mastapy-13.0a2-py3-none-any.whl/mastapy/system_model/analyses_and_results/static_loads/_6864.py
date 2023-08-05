"""_6864.py

HarmonicLoadDataFluxImport
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6874, _6862, _6843
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_FLUX_IMPORT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HarmonicLoadDataFluxImport')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicLoadDataFluxImport',)


class HarmonicLoadDataFluxImport(_6862.HarmonicLoadDataCSVImport['_6843.ElectricMachineHarmonicLoadFluxImportOptions']):
    """HarmonicLoadDataFluxImport

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_FLUX_IMPORT

    class _Cast_HarmonicLoadDataFluxImport:
        """Special nested class for casting HarmonicLoadDataFluxImport to subclasses."""

        def __init__(self, parent: 'HarmonicLoadDataFluxImport'):
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
        def harmonic_load_data_flux_import(self) -> 'HarmonicLoadDataFluxImport':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicLoadDataFluxImport.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter_of_node_ring_from_flux_file(self) -> 'float':
        """float: 'DiameterOfNodeRingFromFluxFile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiameterOfNodeRingFromFluxFile

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_diameter_reference(self) -> '_6874.InnerDiameterReference':
        """InnerDiameterReference: 'InnerDiameterReference' is the original name of this property."""

        temp = self.wrapped.InnerDiameterReference

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _6874.InnerDiameterReference)
        return constructor.new_from_mastapy_type(_6874.InnerDiameterReference)(value) if value is not None else None

    @inner_diameter_reference.setter
    def inner_diameter_reference(self, value: '_6874.InnerDiameterReference'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _6874.InnerDiameterReference.type_())
        self.wrapped.InnerDiameterReference = value

    def select_flux_file(self):
        """ 'SelectFluxFile' is the original name of this method."""

        self.wrapped.SelectFluxFile()

    @property
    def cast_to(self) -> 'HarmonicLoadDataFluxImport._Cast_HarmonicLoadDataFluxImport':
        return self._Cast_HarmonicLoadDataFluxImport(self)
