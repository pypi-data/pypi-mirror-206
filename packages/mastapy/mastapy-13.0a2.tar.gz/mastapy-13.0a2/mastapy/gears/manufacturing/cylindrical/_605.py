"""_605.py

CylindricalCutterDatabase
"""
from typing import TypeVar

from mastapy.utility.databases import _1815
from mastapy.gears.manufacturing.cylindrical.cutters import _708
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_CUTTER_DATABASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalCutterDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalCutterDatabase',)


T = TypeVar('T', bound='_708.CylindricalGearRealCutterDesign')


class CylindricalCutterDatabase(_1815.NamedDatabase[T]):
    """CylindricalCutterDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _CYLINDRICAL_CUTTER_DATABASE

    class _Cast_CylindricalCutterDatabase:
        """Special nested class for casting CylindricalCutterDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalCutterDatabase'):
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
        def cylindrical_hob_database(self):
            from mastapy.gears.manufacturing.cylindrical import _610
            
            return self._parent._cast(_610.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(self):
            from mastapy.gears.manufacturing.cylindrical import _621
            
            return self._parent._cast(_621.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _700
            
            return self._parent._cast(_700.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _706
            
            return self._parent._cast(_706.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _711
            
            return self._parent._cast(_711.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _712
            
            return self._parent._cast(_712.CylindricalWormGrinderDatabase)

        @property
        def cylindrical_cutter_database(self) -> 'CylindricalCutterDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalCutterDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalCutterDatabase._Cast_CylindricalCutterDatabase':
        return self._Cast_CylindricalCutterDatabase(self)
