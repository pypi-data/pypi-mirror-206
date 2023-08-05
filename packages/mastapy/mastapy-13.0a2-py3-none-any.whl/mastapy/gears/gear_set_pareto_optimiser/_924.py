"""_924.py

ParetoFaceRatingOptimisationStrategyDatabase
"""
from mastapy.math_utility.optimisation import _1541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_FACE_RATING_OPTIMISATION_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'ParetoFaceRatingOptimisationStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoFaceRatingOptimisationStrategyDatabase',)


class ParetoFaceRatingOptimisationStrategyDatabase(_1541.ParetoOptimisationStrategyDatabase):
    """ParetoFaceRatingOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_FACE_RATING_OPTIMISATION_STRATEGY_DATABASE

    class _Cast_ParetoFaceRatingOptimisationStrategyDatabase:
        """Special nested class for casting ParetoFaceRatingOptimisationStrategyDatabase to subclasses."""

        def __init__(self, parent: 'ParetoFaceRatingOptimisationStrategyDatabase'):
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
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _922
            
            return self._parent._cast(_922.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase)

        @property
        def pareto_face_gear_set_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _923
            
            return self._parent._cast(_923.ParetoFaceGearSetOptimisationStrategyDatabase)

        @property
        def pareto_face_rating_optimisation_strategy_database(self) -> 'ParetoFaceRatingOptimisationStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoFaceRatingOptimisationStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase':
        return self._Cast_ParetoFaceRatingOptimisationStrategyDatabase(self)
