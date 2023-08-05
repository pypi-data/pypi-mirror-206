"""_601.py

RawMaterial
"""
from mastapy._internal import constructor
from mastapy.utility.databases import _1816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RAW_MATERIAL = python_net_import('SMT.MastaAPI.Gears.Materials', 'RawMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('RawMaterial',)


class RawMaterial(_1816.NamedDatabaseItem):
    """RawMaterial

    This is a mastapy class.
    """

    TYPE = _RAW_MATERIAL

    class _Cast_RawMaterial:
        """Special nested class for casting RawMaterial to subclasses."""

        def __init__(self, parent: 'RawMaterial'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def raw_material(self) -> 'RawMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RawMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cost_per_kilogram(self) -> 'float':
        """float: 'CostPerKilogram' is the original name of this property."""

        temp = self.wrapped.CostPerKilogram

        if temp is None:
            return 0.0

        return temp

    @cost_per_kilogram.setter
    def cost_per_kilogram(self, value: 'float'):
        self.wrapped.CostPerKilogram = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'RawMaterial._Cast_RawMaterial':
        return self._Cast_RawMaterial(self)
