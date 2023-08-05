"""_1273.py

MagnetMaterial
"""
from mastapy._internal import constructor
from mastapy.materials import _265
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNET_MATERIAL = python_net_import('SMT.MastaAPI.ElectricMachines', 'MagnetMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('MagnetMaterial',)


class MagnetMaterial(_265.Material):
    """MagnetMaterial

    This is a mastapy class.
    """

    TYPE = _MAGNET_MATERIAL

    class _Cast_MagnetMaterial:
        """Special nested class for casting MagnetMaterial to subclasses."""

        def __init__(self, parent: 'MagnetMaterial'):
            self._parent = parent

        @property
        def material(self):
            return self._parent._cast(_265.Material)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def magnet_material(self) -> 'MagnetMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MagnetMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def country(self) -> 'str':
        """str: 'Country' is the original name of this property."""

        temp = self.wrapped.Country

        if temp is None:
            return ''

        return temp

    @country.setter
    def country(self, value: 'str'):
        self.wrapped.Country = str(value) if value else ''

    @property
    def electrical_resistivity(self) -> 'float':
        """float: 'ElectricalResistivity' is the original name of this property."""

        temp = self.wrapped.ElectricalResistivity

        if temp is None:
            return 0.0

        return temp

    @electrical_resistivity.setter
    def electrical_resistivity(self, value: 'float'):
        self.wrapped.ElectricalResistivity = float(value) if value else 0.0

    @property
    def grade(self) -> 'str':
        """str: 'Grade' is the original name of this property."""

        temp = self.wrapped.Grade

        if temp is None:
            return ''

        return temp

    @grade.setter
    def grade(self, value: 'str'):
        self.wrapped.Grade = str(value) if value else ''

    @property
    def manufacturer(self) -> 'str':
        """str: 'Manufacturer' is the original name of this property."""

        temp = self.wrapped.Manufacturer

        if temp is None:
            return ''

        return temp

    @manufacturer.setter
    def manufacturer(self, value: 'str'):
        self.wrapped.Manufacturer = str(value) if value else ''

    @property
    def material_category(self) -> 'str':
        """str: 'MaterialCategory' is the original name of this property."""

        temp = self.wrapped.MaterialCategory

        if temp is None:
            return ''

        return temp

    @material_category.setter
    def material_category(self, value: 'str'):
        self.wrapped.MaterialCategory = str(value) if value else ''

    @property
    def relative_permeability(self) -> 'float':
        """float: 'RelativePermeability' is the original name of this property."""

        temp = self.wrapped.RelativePermeability

        if temp is None:
            return 0.0

        return temp

    @relative_permeability.setter
    def relative_permeability(self, value: 'float'):
        self.wrapped.RelativePermeability = float(value) if value else 0.0

    @property
    def remanence_at_20_degrees_c(self) -> 'float':
        """float: 'RemanenceAt20DegreesC' is the original name of this property."""

        temp = self.wrapped.RemanenceAt20DegreesC

        if temp is None:
            return 0.0

        return temp

    @remanence_at_20_degrees_c.setter
    def remanence_at_20_degrees_c(self, value: 'float'):
        self.wrapped.RemanenceAt20DegreesC = float(value) if value else 0.0

    @property
    def temperature_coefficient_for_remanence(self) -> 'float':
        """float: 'TemperatureCoefficientForRemanence' is the original name of this property."""

        temp = self.wrapped.TemperatureCoefficientForRemanence

        if temp is None:
            return 0.0

        return temp

    @temperature_coefficient_for_remanence.setter
    def temperature_coefficient_for_remanence(self, value: 'float'):
        self.wrapped.TemperatureCoefficientForRemanence = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'MagnetMaterial._Cast_MagnetMaterial':
        return self._Cast_MagnetMaterial(self)
