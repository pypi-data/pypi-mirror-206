"""_918.py

ParetoConicalRatingOptimisationStrategyDatabase
"""
from mastapy.math_utility.optimisation import _1541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_CONICAL_RATING_OPTIMISATION_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'ParetoConicalRatingOptimisationStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoConicalRatingOptimisationStrategyDatabase',)


class ParetoConicalRatingOptimisationStrategyDatabase(_1541.ParetoOptimisationStrategyDatabase):
    """ParetoConicalRatingOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_CONICAL_RATING_OPTIMISATION_STRATEGY_DATABASE

    class _Cast_ParetoConicalRatingOptimisationStrategyDatabase:
        """Special nested class for casting ParetoConicalRatingOptimisationStrategyDatabase to subclasses."""

        def __init__(self, parent: 'ParetoConicalRatingOptimisationStrategyDatabase'):
            self._parent = parent

        @property
        def pareto_optimisation_strategy_database(self):
            return self._parent._cast(_1541.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(self):
            from mastapy.math_utility.optimisation import _1528
            
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
        def pareto_conical_rating_optimisation_strategy_database(self) -> 'ParetoConicalRatingOptimisationStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoConicalRatingOptimisationStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ParetoConicalRatingOptimisationStrategyDatabase._Cast_ParetoConicalRatingOptimisationStrategyDatabase':
        return self._Cast_ParetoConicalRatingOptimisationStrategyDatabase(self)
