"""_711.py

CylindricalGearShaverDatabase
"""
from mastapy.gears.manufacturing.cylindrical import _605
from mastapy.gears.manufacturing.cylindrical.cutters import _710
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SHAVER_DATABASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearShaverDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearShaverDatabase',)


class CylindricalGearShaverDatabase(_605.CylindricalCutterDatabase['_710.CylindricalGearShaver']):
    """CylindricalGearShaverDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SHAVER_DATABASE

    class _Cast_CylindricalGearShaverDatabase:
        """Special nested class for casting CylindricalGearShaverDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalGearShaverDatabase'):
            self._parent = parent

        @property
        def cylindrical_cutter_database(self):
            return self._parent._cast(_605.CylindricalCutterDatabase)

        @property
        def named_database(self):
            from mastapy.utility.databases import _1815
            
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
        def cylindrical_gear_shaver_database(self) -> 'CylindricalGearShaverDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearShaverDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearShaverDatabase._Cast_CylindricalGearShaverDatabase':
        return self._Cast_CylindricalGearShaverDatabase(self)
