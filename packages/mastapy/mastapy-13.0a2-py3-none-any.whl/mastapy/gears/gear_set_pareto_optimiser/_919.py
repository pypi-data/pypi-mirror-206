"""_919.py

ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
"""
from mastapy.gears.gear_set_pareto_optimiser import _921
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_CYLINDRICAL_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase',)


class ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase(_921.ParetoCylindricalRatingOptimisationStrategyDatabase):
    """ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_CYLINDRICAL_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE

    class _Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase:
        """Special nested class for casting ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase to subclasses."""

        def __init__(self, parent: 'ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase'):
            self._parent = parent

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(self):
            return self._parent._cast(_921.ParetoCylindricalRatingOptimisationStrategyDatabase)

        @property
        def pareto_optimisation_strategy_database(self):
            from mastapy.math_utility.optimisation import _1541
            
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
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(self) -> 'ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase':
        return self._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase(self)
