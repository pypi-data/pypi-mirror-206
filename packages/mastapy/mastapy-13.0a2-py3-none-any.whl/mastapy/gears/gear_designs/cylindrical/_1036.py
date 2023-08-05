"""_1036.py

CylindricalPlanetGearDesign
"""
from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.geometry.two_d import _308
from mastapy.gears import _336
from mastapy.gears.gear_designs.cylindrical import _1058, _1059, _1007
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalPlanetGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGearDesign',)


class CylindricalPlanetGearDesign(_1007.CylindricalGearDesign):
    """CylindricalPlanetGearDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_DESIGN

    class _Cast_CylindricalPlanetGearDesign:
        """Special nested class for casting CylindricalPlanetGearDesign to subclasses."""

        def __init__(self, parent: 'CylindricalPlanetGearDesign'):
            self._parent = parent

        @property
        def cylindrical_gear_design(self):
            return self._parent._cast(_1007.CylindricalGearDesign)

        @property
        def gear_design(self):
            from mastapy.gears.gear_designs import _942
            
            return self._parent._cast(_942.GearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def cylindrical_planet_gear_design(self) -> 'CylindricalPlanetGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_factorising_annulus(self) -> 'bool':
        """bool: 'HasFactorisingAnnulus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasFactorisingAnnulus

        if temp is None:
            return False

        return temp

    @property
    def has_factorising_sun(self) -> 'bool':
        """bool: 'HasFactorisingSun' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasFactorisingSun

        if temp is None:
            return False

        return temp

    @property
    def internal_external(self) -> '_308.InternalExternalType':
        """InternalExternalType: 'InternalExternal' is the original name of this property."""

        temp = self.wrapped.InternalExternal

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _308.InternalExternalType)
        return constructor.new_from_mastapy_type(_308.InternalExternalType)(value) if value is not None else None

    @internal_external.setter
    def internal_external(self, value: '_308.InternalExternalType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _308.InternalExternalType.type_())
        self.wrapped.InternalExternal = value

    @property
    def planetary_details(self) -> '_336.PlanetaryDetail':
        """PlanetaryDetail: 'PlanetaryDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetaryDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planet_assembly_indices(self) -> 'List[_1058.NamedPlanetAssemblyIndex]':
        """List[NamedPlanetAssemblyIndex]: 'PlanetAssemblyIndices' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetAssemblyIndices

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetary_sidebands_amplitude_factors(self) -> 'List[_1059.NamedPlanetSideBandAmplitudeFactor]':
        """List[NamedPlanetSideBandAmplitudeFactor]: 'PlanetarySidebandsAmplitudeFactors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetarySidebandsAmplitudeFactors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalPlanetGearDesign._Cast_CylindricalPlanetGearDesign':
        return self._Cast_CylindricalPlanetGearDesign(self)
