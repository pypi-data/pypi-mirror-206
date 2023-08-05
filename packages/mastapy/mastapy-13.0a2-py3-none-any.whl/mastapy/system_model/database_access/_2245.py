"""_2245.py

Databases
"""
from mastapy.materials import _242, _245, _264
from mastapy._internal import constructor
from mastapy.gears.materials import (
    _581, _583, _584, _585,
    _588, _595, _602
)
from mastapy.bolts import _1457, _1459, _1464
from mastapy.system_model.optimization import _2213, _2222
from mastapy.gears.manufacturing.cylindrical.cutters import (
    _700, _706, _711, _712
)
from mastapy.gears.manufacturing.cylindrical import _610, _621
from mastapy.electric_machines import _1274, _1292, _1304
from mastapy.gears.manufacturing.bevel import _795
from mastapy.gears.gear_set_pareto_optimiser import (
    _915, _916, _919, _920,
    _925, _926, _928, _929,
    _930, _931
)
from mastapy.bearings import _1878
from mastapy.shafts import _25
from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2543
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATABASES = python_net_import('SMT.MastaAPI.SystemModel.DatabaseAccess', 'Databases')


__docformat__ = 'restructuredtext en'
__all__ = ('Databases',)


class Databases(_0.APIBase):
    """Databases

    This is a mastapy class.
    """

    TYPE = _DATABASES

    class _Cast_Databases:
        """Special nested class for casting Databases to subclasses."""

        def __init__(self, parent: 'Databases'):
            self._parent = parent

        @property
        def databases(self) -> 'Databases':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Databases.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bearing_material_database(self) -> '_242.BearingMaterialDatabase':
        """BearingMaterialDatabase: 'BearingMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_iso_material_database(self) -> '_581.BevelGearIsoMaterialDatabase':
        """BevelGearIsoMaterialDatabase: 'BevelGearIsoMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearIsoMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_material_database(self) -> '_583.BevelGearMaterialDatabase':
        """BevelGearMaterialDatabase: 'BevelGearMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bolt_geometry_database(self) -> '_1457.BoltGeometryDatabase':
        """BoltGeometryDatabase: 'BoltGeometryDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltGeometryDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bolt_material_database(self) -> '_1459.BoltMaterialDatabase':
        """BoltMaterialDatabase: 'BoltMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def clamped_section_material_database(self) -> '_1464.ClampedSectionMaterialDatabase':
        """ClampedSectionMaterialDatabase: 'ClampedSectionMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClampedSectionMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_material_database(self) -> '_245.ComponentMaterialDatabase':
        """ComponentMaterialDatabase: 'ComponentMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_optimization_strategy_database(self) -> '_2213.ConicalGearOptimizationStrategyDatabase':
        """ConicalGearOptimizationStrategyDatabase: 'ConicalGearOptimizationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearOptimizationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_formed_wheel_grinder_database(self) -> '_700.CylindricalFormedWheelGrinderDatabase':
        """CylindricalFormedWheelGrinderDatabase: 'CylindricalFormedWheelGrinderDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalFormedWheelGrinderDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_agma_material_database(self) -> '_584.CylindricalGearAGMAMaterialDatabase':
        """CylindricalGearAGMAMaterialDatabase: 'CylindricalGearAGMAMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearAGMAMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_iso_material_database(self) -> '_585.CylindricalGearISOMaterialDatabase':
        """CylindricalGearISOMaterialDatabase: 'CylindricalGearISOMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearISOMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_plastic_material_database(self) -> '_588.CylindricalGearPlasticMaterialDatabase':
        """CylindricalGearPlasticMaterialDatabase: 'CylindricalGearPlasticMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearPlasticMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_plunge_shaver_database(self) -> '_706.CylindricalGearPlungeShaverDatabase':
        """CylindricalGearPlungeShaverDatabase: 'CylindricalGearPlungeShaverDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearPlungeShaverDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_shaver_database(self) -> '_711.CylindricalGearShaverDatabase':
        """CylindricalGearShaverDatabase: 'CylindricalGearShaverDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearShaverDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_hob_database(self) -> '_610.CylindricalHobDatabase':
        """CylindricalHobDatabase: 'CylindricalHobDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalHobDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_shaper_database(self) -> '_621.CylindricalShaperDatabase':
        """CylindricalShaperDatabase: 'CylindricalShaperDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalShaperDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_worm_grinder_database(self) -> '_712.CylindricalWormGrinderDatabase':
        """CylindricalWormGrinderDatabase: 'CylindricalWormGrinderDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalWormGrinderDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_conical_gear_material_database(self) -> '_595.KlingelnbergConicalGearMaterialDatabase':
        """KlingelnbergConicalGearMaterialDatabase: 'KlingelnbergConicalGearMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergConicalGearMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lubrication_detail_database(self) -> '_264.LubricationDetailDatabase':
        """LubricationDetailDatabase: 'LubricationDetailDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricationDetailDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def magnet_material_database(self) -> '_1274.MagnetMaterialDatabase':
        """MagnetMaterialDatabase: 'MagnetMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MagnetMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def manufacturing_machine_database(self) -> '_795.ManufacturingMachineDatabase':
        """ManufacturingMachineDatabase: 'ManufacturingMachineDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingMachineDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry_gear_set_design_space_search_strategy_database(self) -> '_915.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase':
        """MicroGeometryGearSetDesignSpaceSearchStrategyDatabase: 'MicroGeometryGearSetDesignSpaceSearchStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(self) -> '_916.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase':
        """MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase: 'MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def optimization_strategy_database(self) -> '_2222.OptimizationStrategyDatabase':
        """OptimizationStrategyDatabase: 'OptimizationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OptimizationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_919.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_cylindrical_gear_set_optimisation_strategy_database(self) -> '_920.ParetoCylindricalGearSetOptimisationStrategyDatabase':
        """ParetoCylindricalGearSetOptimisationStrategyDatabase: 'ParetoCylindricalGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoCylindricalGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_925.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_hypoid_gear_set_optimisation_strategy_database(self) -> '_926.ParetoHypoidGearSetOptimisationStrategyDatabase':
        """ParetoHypoidGearSetOptimisationStrategyDatabase: 'ParetoHypoidGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoHypoidGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_928.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_spiral_bevel_gear_set_optimisation_strategy_database(self) -> '_929.ParetoSpiralBevelGearSetOptimisationStrategyDatabase':
        """ParetoSpiralBevelGearSetOptimisationStrategyDatabase: 'ParetoSpiralBevelGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoSpiralBevelGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_930.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_straight_bevel_gear_set_optimisation_strategy_database(self) -> '_931.ParetoStraightBevelGearSetOptimisationStrategyDatabase':
        """ParetoStraightBevelGearSetOptimisationStrategyDatabase: 'ParetoStraightBevelGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoStraightBevelGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def raw_material_database(self) -> '_602.RawMaterialDatabase':
        """RawMaterialDatabase: 'RawMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RawMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rolling_bearing_database(self) -> '_1878.RollingBearingDatabase':
        """RollingBearingDatabase: 'RollingBearingDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingBearingDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_material_database(self) -> '_25.ShaftMaterialDatabase':
        """ShaftMaterialDatabase: 'ShaftMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_and_rotor_material_database(self) -> '_1292.StatorRotorMaterialDatabase':
        """StatorRotorMaterialDatabase: 'StatorAndRotorMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorAndRotorMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def supercharger_rotor_set_database(self) -> '_2543.SuperchargerRotorSetDatabase':
        """SuperchargerRotorSetDatabase: 'SuperchargerRotorSetDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SuperchargerRotorSetDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def winding_material_database(self) -> '_1304.WindingMaterialDatabase':
        """WindingMaterialDatabase: 'WindingMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'Databases._Cast_Databases':
        return self._Cast_Databases(self)
