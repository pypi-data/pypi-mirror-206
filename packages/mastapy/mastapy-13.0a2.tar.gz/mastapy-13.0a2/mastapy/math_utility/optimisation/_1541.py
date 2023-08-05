"""_1541.py

ParetoOptimisationStrategyDatabase
"""
from mastapy.math_utility.optimisation import _1528
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'ParetoOptimisationStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoOptimisationStrategyDatabase',)


class ParetoOptimisationStrategyDatabase(_1528.DesignSpaceSearchStrategyDatabase):
    """ParetoOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_STRATEGY_DATABASE

    class _Cast_ParetoOptimisationStrategyDatabase:
        """Special nested class for casting ParetoOptimisationStrategyDatabase to subclasses."""

        def __init__(self, parent: 'ParetoOptimisationStrategyDatabase'):
            self._parent = parent

        @property
        def design_space_search_strategy_database(self):
            return self._parent._cast(_1528.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(self):
            from mastapy.utility.databases import _1815
            from mastapy.math_utility.optimisation import _1538
            
            return self._parent._cast(_1815.NamedDatabase)

        @property
        def sql_database(self):
            from mastapy.utility.databases import _1818, _1817
            from mastapy.math_utility.optimisation import _1538
            
            return self._parent._cast(_1818.SQLDatabase)

        @property
        def database(self):
            from mastapy.utility.databases import _1811, _1817
            from mastapy.math_utility.optimisation import _1538
            
            return self._parent._cast(_1811.Database)

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
        def pareto_optimisation_strategy_database(self) -> 'ParetoOptimisationStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoOptimisationStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ParetoOptimisationStrategyDatabase._Cast_ParetoOptimisationStrategyDatabase':
        return self._Cast_ParetoOptimisationStrategyDatabase(self)
