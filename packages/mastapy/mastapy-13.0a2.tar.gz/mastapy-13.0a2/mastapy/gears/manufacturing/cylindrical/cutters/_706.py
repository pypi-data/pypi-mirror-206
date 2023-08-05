"""_706.py

CylindricalGearPlungeShaverDatabase
"""
from mastapy.gears.manufacturing.cylindrical import _605
from mastapy.gears.manufacturing.cylindrical.cutters import _705
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PLUNGE_SHAVER_DATABASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearPlungeShaverDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearPlungeShaverDatabase',)


class CylindricalGearPlungeShaverDatabase(_605.CylindricalCutterDatabase['_705.CylindricalGearPlungeShaver']):
    """CylindricalGearPlungeShaverDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PLUNGE_SHAVER_DATABASE

    class _Cast_CylindricalGearPlungeShaverDatabase:
        """Special nested class for casting CylindricalGearPlungeShaverDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalGearPlungeShaverDatabase'):
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
        def cylindrical_gear_plunge_shaver_database(self) -> 'CylindricalGearPlungeShaverDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearPlungeShaverDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearPlungeShaverDatabase._Cast_CylindricalGearPlungeShaverDatabase':
        return self._Cast_CylindricalGearPlungeShaverDatabase(self)
