"""_219.py

ThermalExpansionOrthotropicComponents
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THERMAL_EXPANSION_ORTHOTROPIC_COMPONENTS = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'ThermalExpansionOrthotropicComponents')


__docformat__ = 'restructuredtext en'
__all__ = ('ThermalExpansionOrthotropicComponents',)


class ThermalExpansionOrthotropicComponents(_0.APIBase):
    """ThermalExpansionOrthotropicComponents

    This is a mastapy class.
    """

    TYPE = _THERMAL_EXPANSION_ORTHOTROPIC_COMPONENTS

    class _Cast_ThermalExpansionOrthotropicComponents:
        """Special nested class for casting ThermalExpansionOrthotropicComponents to subclasses."""

        def __init__(self, parent: 'ThermalExpansionOrthotropicComponents'):
            self._parent = parent

        @property
        def thermal_expansion_orthotropic_components(self) -> 'ThermalExpansionOrthotropicComponents':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ThermalExpansionOrthotropicComponents.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def x(self) -> 'float':
        """float: 'X' is the original name of this property."""

        temp = self.wrapped.X

        if temp is None:
            return 0.0

        return temp

    @x.setter
    def x(self, value: 'float'):
        self.wrapped.X = float(value) if value else 0.0

    @property
    def y(self) -> 'float':
        """float: 'Y' is the original name of this property."""

        temp = self.wrapped.Y

        if temp is None:
            return 0.0

        return temp

    @y.setter
    def y(self, value: 'float'):
        self.wrapped.Y = float(value) if value else 0.0

    @property
    def z(self) -> 'float':
        """float: 'Z' is the original name of this property."""

        temp = self.wrapped.Z

        if temp is None:
            return 0.0

        return temp

    @z.setter
    def z(self, value: 'float'):
        self.wrapped.Z = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'ThermalExpansionOrthotropicComponents._Cast_ThermalExpansionOrthotropicComponents':
        return self._Cast_ThermalExpansionOrthotropicComponents(self)
