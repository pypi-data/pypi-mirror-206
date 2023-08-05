"""_265.py

Material
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.materials import _254, _270
from mastapy.utility.databases import _1816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIAL = python_net_import('SMT.MastaAPI.Materials', 'Material')


__docformat__ = 'restructuredtext en'
__all__ = ('Material',)


class Material(_1816.NamedDatabaseItem):
    """Material

    This is a mastapy class.
    """

    TYPE = _MATERIAL

    class _Cast_Material:
        """Special nested class for casting Material to subclasses."""

        def __init__(self, parent: 'Material'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def shaft_material(self):
            from mastapy.shafts import _24
            
            return self._parent._cast(_24.ShaftMaterial)

        @property
        def bearing_material(self):
            from mastapy.materials import _241
            
            return self._parent._cast(_241.BearingMaterial)

        @property
        def agma_cylindrical_gear_material(self):
            from mastapy.gears.materials import _578
            
            return self._parent._cast(_578.AGMACylindricalGearMaterial)

        @property
        def bevel_gear_iso_material(self):
            from mastapy.gears.materials import _580
            
            return self._parent._cast(_580.BevelGearISOMaterial)

        @property
        def bevel_gear_material(self):
            from mastapy.gears.materials import _582
            
            return self._parent._cast(_582.BevelGearMaterial)

        @property
        def cylindrical_gear_material(self):
            from mastapy.gears.materials import _586
            
            return self._parent._cast(_586.CylindricalGearMaterial)

        @property
        def gear_material(self):
            from mastapy.gears.materials import _589
            
            return self._parent._cast(_589.GearMaterial)

        @property
        def iso_cylindrical_gear_material(self):
            from mastapy.gears.materials import _592
            
            return self._parent._cast(_592.ISOCylindricalGearMaterial)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_material(self):
            from mastapy.gears.materials import _596
            
            return self._parent._cast(_596.KlingelnbergCycloPalloidConicalGearMaterial)

        @property
        def plastic_cylindrical_gear_material(self):
            from mastapy.gears.materials import _598
            
            return self._parent._cast(_598.PlasticCylindricalGearMaterial)

        @property
        def magnet_material(self):
            from mastapy.electric_machines import _1273
            
            return self._parent._cast(_1273.MagnetMaterial)

        @property
        def stator_rotor_material(self):
            from mastapy.electric_machines import _1291
            
            return self._parent._cast(_1291.StatorRotorMaterial)

        @property
        def winding_material(self):
            from mastapy.electric_machines import _1303
            
            return self._parent._cast(_1303.WindingMaterial)

        @property
        def spline_material(self):
            from mastapy.detailed_rigid_connectors.splines import _1404
            
            return self._parent._cast(_1404.SplineMaterial)

        @property
        def cycloidal_disc_material(self):
            from mastapy.cycloidal import _1444
            
            return self._parent._cast(_1444.CycloidalDiscMaterial)

        @property
        def ring_pins_material(self):
            from mastapy.cycloidal import _1451
            
            return self._parent._cast(_1451.RingPinsMaterial)

        @property
        def bolted_joint_material(self):
            from mastapy.bolts import _1454
            
            return self._parent._cast(_1454.BoltedJointMaterial)

        @property
        def bolt_material(self):
            from mastapy.bolts import _1458
            
            return self._parent._cast(_1458.BoltMaterial)

        @property
        def material(self) -> 'Material':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Material.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_of_thermal_expansion(self) -> 'float':
        """float: 'CoefficientOfThermalExpansion' is the original name of this property."""

        temp = self.wrapped.CoefficientOfThermalExpansion

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_thermal_expansion.setter
    def coefficient_of_thermal_expansion(self, value: 'float'):
        self.wrapped.CoefficientOfThermalExpansion = float(value) if value else 0.0

    @property
    def cost_per_unit_mass(self) -> 'float':
        """float: 'CostPerUnitMass' is the original name of this property."""

        temp = self.wrapped.CostPerUnitMass

        if temp is None:
            return 0.0

        return temp

    @cost_per_unit_mass.setter
    def cost_per_unit_mass(self, value: 'float'):
        self.wrapped.CostPerUnitMass = float(value) if value else 0.0

    @property
    def density(self) -> 'float':
        """float: 'Density' is the original name of this property."""

        temp = self.wrapped.Density

        if temp is None:
            return 0.0

        return temp

    @density.setter
    def density(self, value: 'float'):
        self.wrapped.Density = float(value) if value else 0.0

    @property
    def hardness_type(self) -> '_254.HardnessType':
        """HardnessType: 'HardnessType' is the original name of this property."""

        temp = self.wrapped.HardnessType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _254.HardnessType)
        return constructor.new_from_mastapy_type(_254.HardnessType)(value) if value is not None else None

    @hardness_type.setter
    def hardness_type(self, value: '_254.HardnessType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _254.HardnessType.type_())
        self.wrapped.HardnessType = value

    @property
    def material_name(self) -> 'str':
        """str: 'MaterialName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaterialName

        if temp is None:
            return ''

        return temp

    @property
    def maximum_allowable_temperature(self) -> 'float':
        """float: 'MaximumAllowableTemperature' is the original name of this property."""

        temp = self.wrapped.MaximumAllowableTemperature

        if temp is None:
            return 0.0

        return temp

    @maximum_allowable_temperature.setter
    def maximum_allowable_temperature(self, value: 'float'):
        self.wrapped.MaximumAllowableTemperature = float(value) if value else 0.0

    @property
    def modulus_of_elasticity(self) -> 'float':
        """float: 'ModulusOfElasticity' is the original name of this property."""

        temp = self.wrapped.ModulusOfElasticity

        if temp is None:
            return 0.0

        return temp

    @modulus_of_elasticity.setter
    def modulus_of_elasticity(self, value: 'float'):
        self.wrapped.ModulusOfElasticity = float(value) if value else 0.0

    @property
    def plane_strain_modulus(self) -> 'float':
        """float: 'PlaneStrainModulus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlaneStrainModulus

        if temp is None:
            return 0.0

        return temp

    @property
    def poissons_ratio(self) -> 'float':
        """float: 'PoissonsRatio' is the original name of this property."""

        temp = self.wrapped.PoissonsRatio

        if temp is None:
            return 0.0

        return temp

    @poissons_ratio.setter
    def poissons_ratio(self, value: 'float'):
        self.wrapped.PoissonsRatio = float(value) if value else 0.0

    @property
    def shear_fatigue_strength(self) -> 'float':
        """float: 'ShearFatigueStrength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShearFatigueStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def shear_modulus(self) -> 'float':
        """float: 'ShearModulus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShearModulus

        if temp is None:
            return 0.0

        return temp

    @property
    def shear_yield_stress(self) -> 'float':
        """float: 'ShearYieldStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShearYieldStress

        if temp is None:
            return 0.0

        return temp

    @property
    def standard(self) -> '_270.MaterialStandards':
        """MaterialStandards: 'Standard' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Standard

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _270.MaterialStandards)
        return constructor.new_from_mastapy_type(_270.MaterialStandards)(value) if value is not None else None

    @property
    def surface_hardness(self) -> 'float':
        """float: 'SurfaceHardness' is the original name of this property."""

        temp = self.wrapped.SurfaceHardness

        if temp is None:
            return 0.0

        return temp

    @surface_hardness.setter
    def surface_hardness(self, value: 'float'):
        self.wrapped.SurfaceHardness = float(value) if value else 0.0

    @property
    def surface_hardness_range_max_in_hb(self) -> 'float':
        """float: 'SurfaceHardnessRangeMaxInHB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceHardnessRangeMaxInHB

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_max_in_hrc(self) -> 'float':
        """float: 'SurfaceHardnessRangeMaxInHRC' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceHardnessRangeMaxInHRC

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_max_in_hv(self) -> 'float':
        """float: 'SurfaceHardnessRangeMaxInHV' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceHardnessRangeMaxInHV

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_min_in_hb(self) -> 'float':
        """float: 'SurfaceHardnessRangeMinInHB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceHardnessRangeMinInHB

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_min_in_hrc(self) -> 'float':
        """float: 'SurfaceHardnessRangeMinInHRC' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceHardnessRangeMinInHRC

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_min_in_hv(self) -> 'float':
        """float: 'SurfaceHardnessRangeMinInHV' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceHardnessRangeMinInHV

        if temp is None:
            return 0.0

        return temp

    @property
    def tensile_yield_strength(self) -> 'float':
        """float: 'TensileYieldStrength' is the original name of this property."""

        temp = self.wrapped.TensileYieldStrength

        if temp is None:
            return 0.0

        return temp

    @tensile_yield_strength.setter
    def tensile_yield_strength(self, value: 'float'):
        self.wrapped.TensileYieldStrength = float(value) if value else 0.0

    @property
    def ultimate_tensile_strength(self) -> 'float':
        """float: 'UltimateTensileStrength' is the original name of this property."""

        temp = self.wrapped.UltimateTensileStrength

        if temp is None:
            return 0.0

        return temp

    @ultimate_tensile_strength.setter
    def ultimate_tensile_strength(self, value: 'float'):
        self.wrapped.UltimateTensileStrength = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'Material._Cast_Material':
        return self._Cast_Material(self)
