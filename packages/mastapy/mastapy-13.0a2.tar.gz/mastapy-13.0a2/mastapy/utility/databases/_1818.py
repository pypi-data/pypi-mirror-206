"""_1818.py

SQLDatabase
"""
from typing import TypeVar

from mastapy._internal import constructor
from mastapy.utility.databases import _1811, _1813
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SQL_DATABASE = python_net_import('SMT.MastaAPI.Utility.Databases', 'SQLDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('SQLDatabase',)


TKey = TypeVar('TKey', bound='_1813.DatabaseKey')
TValue = TypeVar('TValue', bound='_0.APIBase')


class SQLDatabase(_1811.Database[TKey, TValue]):
    """SQLDatabase

    This is a mastapy class.

    Generic Types:
        TKey
        TValue
    """

    TYPE = _SQL_DATABASE

    class _Cast_SQLDatabase:
        """Special nested class for casting SQLDatabase to subclasses."""

        def __init__(self, parent: 'SQLDatabase'):
            self._parent = parent

        @property
        def database(self):
            return self._parent._cast(_1811.Database)

        @property
        def shaft_material_database(self):
            from mastapy.shafts import _25
            
            return self._parent._cast(_25.ShaftMaterialDatabase)

        @property
        def shaft_settings_database(self):
            from mastapy.shafts import _39
            
            return self._parent._cast(_39.ShaftSettingsDatabase)

        @property
        def analysis_settings_database(self):
            from mastapy.nodal_analysis import _49
            
            return self._parent._cast(_49.AnalysisSettingsDatabase)

        @property
        def bearing_material_database(self):
            from mastapy.materials import _242
            
            return self._parent._cast(_242.BearingMaterialDatabase)

        @property
        def component_material_database(self):
            from mastapy.materials import _245
            
            return self._parent._cast(_245.ComponentMaterialDatabase)

        @property
        def lubrication_detail_database(self):
            from mastapy.materials import _264
            
            return self._parent._cast(_264.LubricationDetailDatabase)

        @property
        def material_database(self):
            from mastapy.materials import _266
            
            return self._parent._cast(_266.MaterialDatabase)

        @property
        def materials_settings_database(self):
            from mastapy.materials import _268
            
            return self._parent._cast(_268.MaterialsSettingsDatabase)

        @property
        def pocketing_power_loss_coefficients_database(self):
            from mastapy.gears import _339
            
            return self._parent._cast(_339.PocketingPowerLossCoefficientsDatabase)

        @property
        def cylindrical_gear_design_and_rating_settings_database(self):
            from mastapy.gears.rating.cylindrical import _449
            
            return self._parent._cast(_449.CylindricalGearDesignAndRatingSettingsDatabase)

        @property
        def cylindrical_plastic_gear_rating_settings_database(self):
            from mastapy.gears.rating.cylindrical import _465
            
            return self._parent._cast(_465.CylindricalPlasticGearRatingSettingsDatabase)

        @property
        def bevel_gear_abstract_material_database(self):
            from mastapy.gears.materials import _579
            
            return self._parent._cast(_579.BevelGearAbstractMaterialDatabase)

        @property
        def bevel_gear_iso_material_database(self):
            from mastapy.gears.materials import _581
            
            return self._parent._cast(_581.BevelGearIsoMaterialDatabase)

        @property
        def bevel_gear_material_database(self):
            from mastapy.gears.materials import _583
            
            return self._parent._cast(_583.BevelGearMaterialDatabase)

        @property
        def cylindrical_gear_agma_material_database(self):
            from mastapy.gears.materials import _584
            
            return self._parent._cast(_584.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(self):
            from mastapy.gears.materials import _585
            
            return self._parent._cast(_585.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_material_database(self):
            from mastapy.gears.materials import _587
            
            return self._parent._cast(_587.CylindricalGearMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(self):
            from mastapy.gears.materials import _588
            
            return self._parent._cast(_588.CylindricalGearPlasticMaterialDatabase)

        @property
        def gear_material_database(self):
            from mastapy.gears.materials import _590
            
            return self._parent._cast(_590.GearMaterialDatabase)

        @property
        def isotr1417912001_coefficient_of_friction_constants_database(self):
            from mastapy.gears.materials import _594
            
            return self._parent._cast(_594.ISOTR1417912001CoefficientOfFrictionConstantsDatabase)

        @property
        def klingelnberg_conical_gear_material_database(self):
            from mastapy.gears.materials import _595
            
            return self._parent._cast(_595.KlingelnbergConicalGearMaterialDatabase)

        @property
        def raw_material_database(self):
            from mastapy.gears.materials import _602
            
            return self._parent._cast(_602.RawMaterialDatabase)

        @property
        def cylindrical_cutter_database(self):
            from mastapy.gears.manufacturing.cylindrical import _605
            
            return self._parent._cast(_605.CylindricalCutterDatabase)

        @property
        def cylindrical_hob_database(self):
            from mastapy.gears.manufacturing.cylindrical import _610
            
            return self._parent._cast(_610.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(self):
            from mastapy.gears.manufacturing.cylindrical import _621
            
            return self._parent._cast(_621.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _700
            
            return self._parent._cast(_700.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _706
            
            return self._parent._cast(_706.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _711
            
            return self._parent._cast(_711.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _712
            
            return self._parent._cast(_712.CylindricalWormGrinderDatabase)

        @property
        def manufacturing_machine_database(self):
            from mastapy.gears.manufacturing.bevel import _795
            
            return self._parent._cast(_795.ManufacturingMachineDatabase)

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _915
            
            return self._parent._cast(_915.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase)

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _916
            
            return self._parent._cast(_916.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase)

        @property
        def pareto_conical_rating_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _918
            
            return self._parent._cast(_918.ParetoConicalRatingOptimisationStrategyDatabase)

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _919
            
            return self._parent._cast(_919.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase)

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _920
            
            return self._parent._cast(_920.ParetoCylindricalGearSetOptimisationStrategyDatabase)

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _921
            
            return self._parent._cast(_921.ParetoCylindricalRatingOptimisationStrategyDatabase)

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _922
            
            return self._parent._cast(_922.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase)

        @property
        def pareto_face_gear_set_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _923
            
            return self._parent._cast(_923.ParetoFaceGearSetOptimisationStrategyDatabase)

        @property
        def pareto_face_rating_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _924
            
            return self._parent._cast(_924.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _925
            
            return self._parent._cast(_925.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _926
            
            return self._parent._cast(_926.ParetoHypoidGearSetOptimisationStrategyDatabase)

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _928
            
            return self._parent._cast(_928.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase)

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _929
            
            return self._parent._cast(_929.ParetoSpiralBevelGearSetOptimisationStrategyDatabase)

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _930
            
            return self._parent._cast(_930.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase)

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _931
            
            return self._parent._cast(_931.ParetoStraightBevelGearSetOptimisationStrategyDatabase)

        @property
        def bevel_hypoid_gear_design_settings_database(self):
            from mastapy.gears.gear_designs import _935
            
            return self._parent._cast(_935.BevelHypoidGearDesignSettingsDatabase)

        @property
        def bevel_hypoid_gear_rating_settings_database(self):
            from mastapy.gears.gear_designs import _937
            
            return self._parent._cast(_937.BevelHypoidGearRatingSettingsDatabase)

        @property
        def design_constraint_collection_database(self):
            from mastapy.gears.gear_designs import _940
            
            return self._parent._cast(_940.DesignConstraintCollectionDatabase)

        @property
        def cylindrical_gear_design_constraints_database(self):
            from mastapy.gears.gear_designs.cylindrical import _1010
            
            return self._parent._cast(_1010.CylindricalGearDesignConstraintsDatabase)

        @property
        def cylindrical_gear_micro_geometry_settings_database(self):
            from mastapy.gears.gear_designs.cylindrical import _1016
            
            return self._parent._cast(_1016.CylindricalGearMicroGeometrySettingsDatabase)

        @property
        def magnet_material_database(self):
            from mastapy.electric_machines import _1274
            
            return self._parent._cast(_1274.MagnetMaterialDatabase)

        @property
        def stator_rotor_material_database(self):
            from mastapy.electric_machines import _1292
            
            return self._parent._cast(_1292.StatorRotorMaterialDatabase)

        @property
        def winding_material_database(self):
            from mastapy.electric_machines import _1304
            
            return self._parent._cast(_1304.WindingMaterialDatabase)

        @property
        def cycloidal_disc_material_database(self):
            from mastapy.cycloidal import _1445
            
            return self._parent._cast(_1445.CycloidalDiscMaterialDatabase)

        @property
        def ring_pins_material_database(self):
            from mastapy.cycloidal import _1452
            
            return self._parent._cast(_1452.RingPinsMaterialDatabase)

        @property
        def bolted_joint_material_database(self):
            from mastapy.bolts import _1455
            
            return self._parent._cast(_1455.BoltedJointMaterialDatabase)

        @property
        def bolt_geometry_database(self):
            from mastapy.bolts import _1457
            
            return self._parent._cast(_1457.BoltGeometryDatabase)

        @property
        def bolt_material_database(self):
            from mastapy.bolts import _1459
            
            return self._parent._cast(_1459.BoltMaterialDatabase)

        @property
        def clamped_section_material_database(self):
            from mastapy.bolts import _1464
            
            return self._parent._cast(_1464.ClampedSectionMaterialDatabase)

        @property
        def design_space_search_strategy_database(self):
            from mastapy.math_utility.optimisation import _1528
            
            return self._parent._cast(_1528.DesignSpaceSearchStrategyDatabase)

        @property
        def micro_geometry_design_space_search_strategy_database(self):
            from mastapy.math_utility.optimisation import _1530
            
            return self._parent._cast(_1530.MicroGeometryDesignSpaceSearchStrategyDatabase)

        @property
        def pareto_optimisation_strategy_database(self):
            from mastapy.math_utility.optimisation import _1541
            
            return self._parent._cast(_1541.ParetoOptimisationStrategyDatabase)

        @property
        def named_database(self):
            from mastapy.utility.databases import _1815
            
            return self._parent._cast(_1815.NamedDatabase)

        @property
        def bearing_settings_database(self):
            from mastapy.bearings import _1865
            
            return self._parent._cast(_1865.BearingSettingsDatabase)

        @property
        def rolling_bearing_database(self):
            from mastapy.bearings import _1878
            
            return self._parent._cast(_1878.RollingBearingDatabase)

        @property
        def iso14179_settings_database(self):
            from mastapy.bearings.bearing_results.rolling import _1960
            
            return self._parent._cast(_1960.ISO14179SettingsDatabase)

        @property
        def conical_gear_optimization_strategy_database(self):
            from mastapy.system_model.optimization import _2213
            
            return self._parent._cast(_2213.ConicalGearOptimizationStrategyDatabase)

        @property
        def optimization_strategy_database(self):
            from mastapy.system_model.optimization import _2222
            
            return self._parent._cast(_2222.OptimizationStrategyDatabase)

        @property
        def supercharger_rotor_set_database(self):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2543
            
            return self._parent._cast(_2543.SuperchargerRotorSetDatabase)

        @property
        def sql_database(self) -> 'SQLDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SQLDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allow_network_database(self) -> 'bool':
        """bool: 'AllowNetworkDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowNetworkDatabase

        if temp is None:
            return False

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def uses_database(self) -> 'bool':
        """bool: 'UsesDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UsesDatabase

        if temp is None:
            return False

        return temp

    def delete(self, key: 'TKey'):
        """ 'Delete' is the original name of this method.

        Args:
            key (TKey)
        """

        self.wrapped.Delete(key)

    def reload(self):
        """ 'Reload' is the original name of this method."""

        self.wrapped.Reload()

    def save(self, item: 'TValue'):
        """ 'Save' is the original name of this method.

        Args:
            item (TValue)
        """

        self.wrapped.Save(item)

    @property
    def cast_to(self) -> 'SQLDatabase._Cast_SQLDatabase':
        return self._Cast_SQLDatabase(self)
