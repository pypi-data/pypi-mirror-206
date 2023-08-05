"""_2543.py

SuperchargerRotorSetDatabase
"""
from mastapy.utility.databases import _1815
from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SUPERCHARGER_ROTOR_SET_DATABASE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'SuperchargerRotorSetDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('SuperchargerRotorSetDatabase',)


class SuperchargerRotorSetDatabase(_1815.NamedDatabase['_2542.SuperchargerRotorSet']):
    """SuperchargerRotorSetDatabase

    This is a mastapy class.
    """

    TYPE = _SUPERCHARGER_ROTOR_SET_DATABASE

    class _Cast_SuperchargerRotorSetDatabase:
        """Special nested class for casting SuperchargerRotorSetDatabase to subclasses."""

        def __init__(self, parent: 'SuperchargerRotorSetDatabase'):
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
        def supercharger_rotor_set_database(self) -> 'SuperchargerRotorSetDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SuperchargerRotorSetDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SuperchargerRotorSetDatabase._Cast_SuperchargerRotorSetDatabase':
        return self._Cast_SuperchargerRotorSetDatabase(self)
