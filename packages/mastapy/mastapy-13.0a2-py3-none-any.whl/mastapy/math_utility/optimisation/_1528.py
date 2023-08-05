"""_1528.py

DesignSpaceSearchStrategyDatabase
"""
from mastapy.utility.databases import _1815
from mastapy.math_utility.optimisation import _1538
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'DesignSpaceSearchStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('DesignSpaceSearchStrategyDatabase',)


class DesignSpaceSearchStrategyDatabase(_1815.NamedDatabase['_1538.ParetoOptimisationStrategy']):
    """DesignSpaceSearchStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _DESIGN_SPACE_SEARCH_STRATEGY_DATABASE

    class _Cast_DesignSpaceSearchStrategyDatabase:
        """Special nested class for casting DesignSpaceSearchStrategyDatabase to subclasses."""

        def __init__(self, parent: 'DesignSpaceSearchStrategyDatabase'):
            self._parent = parent

        @property
        def named_database(self):
            return self._parent._cast(_1815.NamedDatabase)

        @property
        def sql_database(self):
            from mastapy.utility.databases import _1818, _1817
            
            return self._parent._cast(_1818.SQLDatabase)

        @property
        def database(self):
            from mastapy.utility.databases import _1811, _1817
            
            return self._parent._cast(_1811.Database)

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
        def micro_geometry_design_space_search_strategy_database(self):
            from mastapy.math_utility.optimisation import _1530
            
            return self._parent._cast(_1530.MicroGeometryDesignSpaceSearchStrategyDatabase)

        @property
        def pareto_optimisation_strategy_database(self):
            from mastapy.math_utility.optimisation import _1541
            
            return self._parent._cast(_1541.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(self) -> 'DesignSpaceSearchStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DesignSpaceSearchStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DesignSpaceSearchStrategyDatabase._Cast_DesignSpaceSearchStrategyDatabase':
        return self._Cast_DesignSpaceSearchStrategyDatabase(self)
