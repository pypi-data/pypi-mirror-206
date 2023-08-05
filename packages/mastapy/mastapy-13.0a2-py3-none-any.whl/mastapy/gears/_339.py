"""_339.py

PocketingPowerLossCoefficientsDatabase
"""
from mastapy.utility.databases import _1815
from mastapy.gears import _338
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POCKETING_POWER_LOSS_COEFFICIENTS_DATABASE = python_net_import('SMT.MastaAPI.Gears', 'PocketingPowerLossCoefficientsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('PocketingPowerLossCoefficientsDatabase',)


class PocketingPowerLossCoefficientsDatabase(_1815.NamedDatabase['_338.PocketingPowerLossCoefficients']):
    """PocketingPowerLossCoefficientsDatabase

    This is a mastapy class.
    """

    TYPE = _POCKETING_POWER_LOSS_COEFFICIENTS_DATABASE

    class _Cast_PocketingPowerLossCoefficientsDatabase:
        """Special nested class for casting PocketingPowerLossCoefficientsDatabase to subclasses."""

        def __init__(self, parent: 'PocketingPowerLossCoefficientsDatabase'):
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
        def pocketing_power_loss_coefficients_database(self) -> 'PocketingPowerLossCoefficientsDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PocketingPowerLossCoefficientsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PocketingPowerLossCoefficientsDatabase._Cast_PocketingPowerLossCoefficientsDatabase':
        return self._Cast_PocketingPowerLossCoefficientsDatabase(self)
