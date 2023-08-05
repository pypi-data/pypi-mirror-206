"""_1058.py

NamedPlanetAssemblyIndex
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_PLANET_ASSEMBLY_INDEX = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'NamedPlanetAssemblyIndex')


__docformat__ = 'restructuredtext en'
__all__ = ('NamedPlanetAssemblyIndex',)


class NamedPlanetAssemblyIndex(_0.APIBase):
    """NamedPlanetAssemblyIndex

    This is a mastapy class.
    """

    TYPE = _NAMED_PLANET_ASSEMBLY_INDEX

    class _Cast_NamedPlanetAssemblyIndex:
        """Special nested class for casting NamedPlanetAssemblyIndex to subclasses."""

        def __init__(self, parent: 'NamedPlanetAssemblyIndex'):
            self._parent = parent

        @property
        def named_planet_assembly_index(self) -> 'NamedPlanetAssemblyIndex':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NamedPlanetAssemblyIndex.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planet_assembly_index(self) -> 'float':
        """float: 'PlanetAssemblyIndex' is the original name of this property."""

        temp = self.wrapped.PlanetAssemblyIndex

        if temp is None:
            return 0.0

        return temp

    @planet_assembly_index.setter
    def planet_assembly_index(self, value: 'float'):
        self.wrapped.PlanetAssemblyIndex = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'NamedPlanetAssemblyIndex._Cast_NamedPlanetAssemblyIndex':
        return self._Cast_NamedPlanetAssemblyIndex(self)
