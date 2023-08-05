"""_1454.py

BoltedJointMaterial
"""
from mastapy._internal import constructor
from mastapy.math_utility import _1523
from mastapy.materials import _265
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_MATERIAL = python_net_import('SMT.MastaAPI.Bolts', 'BoltedJointMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointMaterial',)


class BoltedJointMaterial(_265.Material):
    """BoltedJointMaterial

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_MATERIAL

    class _Cast_BoltedJointMaterial:
        """Special nested class for casting BoltedJointMaterial to subclasses."""

        def __init__(self, parent: 'BoltedJointMaterial'):
            self._parent = parent

        @property
        def material(self):
            return self._parent._cast(_265.Material)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def bolt_material(self):
            from mastapy.bolts import _1458
            
            return self._parent._cast(_1458.BoltMaterial)

        @property
        def bolted_joint_material(self) -> 'BoltedJointMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoltedJointMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_of_thermal_expansion_at_20c(self) -> 'float':
        """float: 'CoefficientOfThermalExpansionAt20C' is the original name of this property."""

        temp = self.wrapped.CoefficientOfThermalExpansionAt20C

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_thermal_expansion_at_20c.setter
    def coefficient_of_thermal_expansion_at_20c(self, value: 'float'):
        self.wrapped.CoefficientOfThermalExpansionAt20C = float(value) if value else 0.0

    @property
    def limiting_surface_pressure(self) -> 'float':
        """float: 'LimitingSurfacePressure' is the original name of this property."""

        temp = self.wrapped.LimitingSurfacePressure

        if temp is None:
            return 0.0

        return temp

    @limiting_surface_pressure.setter
    def limiting_surface_pressure(self, value: 'float'):
        self.wrapped.LimitingSurfacePressure = float(value) if value else 0.0

    @property
    def minimum_tensile_strength(self) -> 'float':
        """float: 'MinimumTensileStrength' is the original name of this property."""

        temp = self.wrapped.MinimumTensileStrength

        if temp is None:
            return 0.0

        return temp

    @minimum_tensile_strength.setter
    def minimum_tensile_strength(self, value: 'float'):
        self.wrapped.MinimumTensileStrength = float(value) if value else 0.0

    @property
    def modulus_of_elasticity_at_20c(self) -> 'float':
        """float: 'ModulusOfElasticityAt20C' is the original name of this property."""

        temp = self.wrapped.ModulusOfElasticityAt20C

        if temp is None:
            return 0.0

        return temp

    @modulus_of_elasticity_at_20c.setter
    def modulus_of_elasticity_at_20c(self, value: 'float'):
        self.wrapped.ModulusOfElasticityAt20C = float(value) if value else 0.0

    @property
    def proof_stress(self) -> 'float':
        """float: 'ProofStress' is the original name of this property."""

        temp = self.wrapped.ProofStress

        if temp is None:
            return 0.0

        return temp

    @proof_stress.setter
    def proof_stress(self, value: 'float'):
        self.wrapped.ProofStress = float(value) if value else 0.0

    @property
    def shearing_strength(self) -> 'float':
        """float: 'ShearingStrength' is the original name of this property."""

        temp = self.wrapped.ShearingStrength

        if temp is None:
            return 0.0

        return temp

    @shearing_strength.setter
    def shearing_strength(self, value: 'float'):
        self.wrapped.ShearingStrength = float(value) if value else 0.0

    @property
    def stress_endurance_limit(self) -> 'float':
        """float: 'StressEnduranceLimit' is the original name of this property."""

        temp = self.wrapped.StressEnduranceLimit

        if temp is None:
            return 0.0

        return temp

    @stress_endurance_limit.setter
    def stress_endurance_limit(self, value: 'float'):
        self.wrapped.StressEnduranceLimit = float(value) if value else 0.0

    @property
    def temperature_dependent_coefficient_of_thermal_expansion(self) -> '_1523.Vector2DListAccessor':
        """Vector2DListAccessor: 'TemperatureDependentCoefficientOfThermalExpansion' is the original name of this property."""

        temp = self.wrapped.TemperatureDependentCoefficientOfThermalExpansion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @temperature_dependent_coefficient_of_thermal_expansion.setter
    def temperature_dependent_coefficient_of_thermal_expansion(self, value: '_1523.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.TemperatureDependentCoefficientOfThermalExpansion = value

    @property
    def temperature_dependent_youngs_moduli(self) -> '_1523.Vector2DListAccessor':
        """Vector2DListAccessor: 'TemperatureDependentYoungsModuli' is the original name of this property."""

        temp = self.wrapped.TemperatureDependentYoungsModuli

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @temperature_dependent_youngs_moduli.setter
    def temperature_dependent_youngs_moduli(self, value: '_1523.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.TemperatureDependentYoungsModuli = value

    @property
    def cast_to(self) -> 'BoltedJointMaterial._Cast_BoltedJointMaterial':
        return self._Cast_BoltedJointMaterial(self)
