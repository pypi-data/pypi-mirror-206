"""_594.py

ISOTR1417912001CoefficientOfFrictionConstantsDatabase
"""
from mastapy.utility.databases import _1815
from mastapy.gears.materials import _593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISOTR1417912001_COEFFICIENT_OF_FRICTION_CONSTANTS_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'ISOTR1417912001CoefficientOfFrictionConstantsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ISOTR1417912001CoefficientOfFrictionConstantsDatabase',)


class ISOTR1417912001CoefficientOfFrictionConstantsDatabase(_1815.NamedDatabase['_593.ISOTR1417912001CoefficientOfFrictionConstants']):
    """ISOTR1417912001CoefficientOfFrictionConstantsDatabase

    This is a mastapy class.
    """

    TYPE = _ISOTR1417912001_COEFFICIENT_OF_FRICTION_CONSTANTS_DATABASE

    class _Cast_ISOTR1417912001CoefficientOfFrictionConstantsDatabase:
        """Special nested class for casting ISOTR1417912001CoefficientOfFrictionConstantsDatabase to subclasses."""

        def __init__(self, parent: 'ISOTR1417912001CoefficientOfFrictionConstantsDatabase'):
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
        def isotr1417912001_coefficient_of_friction_constants_database(self) -> 'ISOTR1417912001CoefficientOfFrictionConstantsDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISOTR1417912001CoefficientOfFrictionConstantsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ISOTR1417912001CoefficientOfFrictionConstantsDatabase._Cast_ISOTR1417912001CoefficientOfFrictionConstantsDatabase':
        return self._Cast_ISOTR1417912001CoefficientOfFrictionConstantsDatabase(self)
