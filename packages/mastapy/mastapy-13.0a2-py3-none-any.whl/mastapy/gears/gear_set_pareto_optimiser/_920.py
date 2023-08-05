"""_920.py

ParetoCylindricalGearSetOptimisationStrategyDatabase
"""
from mastapy.gears.gear_set_pareto_optimiser import _921
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_CYLINDRICAL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'ParetoCylindricalGearSetOptimisationStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoCylindricalGearSetOptimisationStrategyDatabase',)


class ParetoCylindricalGearSetOptimisationStrategyDatabase(_921.ParetoCylindricalRatingOptimisationStrategyDatabase):
    """ParetoCylindricalGearSetOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_CYLINDRICAL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE

    class _Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase:
        """Special nested class for casting ParetoCylindricalGearSetOptimisationStrategyDatabase to subclasses."""

        def __init__(self, parent: 'ParetoCylindricalGearSetOptimisationStrategyDatabase'):
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
        def pareto_cylindrical_gear_set_optimisation_strategy_database(self) -> 'ParetoCylindricalGearSetOptimisationStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoCylindricalGearSetOptimisationStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase':
        return self._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase(self)
