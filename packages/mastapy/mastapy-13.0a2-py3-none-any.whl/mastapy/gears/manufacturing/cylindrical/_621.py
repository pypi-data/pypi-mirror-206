"""_621.py

CylindricalShaperDatabase
"""
from mastapy.gears.manufacturing.cylindrical import _605
from mastapy.gears.manufacturing.cylindrical.cutters import _709
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_SHAPER_DATABASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalShaperDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalShaperDatabase',)


class CylindricalShaperDatabase(_605.CylindricalCutterDatabase['_709.CylindricalGearShaper']):
    """CylindricalShaperDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_SHAPER_DATABASE

    class _Cast_CylindricalShaperDatabase:
        """Special nested class for casting CylindricalShaperDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalShaperDatabase'):
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
        def cylindrical_shaper_database(self) -> 'CylindricalShaperDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalShaperDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalShaperDatabase._Cast_CylindricalShaperDatabase':
        return self._Cast_CylindricalShaperDatabase(self)
