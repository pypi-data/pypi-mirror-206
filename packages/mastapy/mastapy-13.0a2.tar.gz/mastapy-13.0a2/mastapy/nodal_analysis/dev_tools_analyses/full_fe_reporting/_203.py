"""_203.py

ElasticModulusOrthotropicComponents
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELASTIC_MODULUS_ORTHOTROPIC_COMPONENTS = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'ElasticModulusOrthotropicComponents')


__docformat__ = 'restructuredtext en'
__all__ = ('ElasticModulusOrthotropicComponents',)


class ElasticModulusOrthotropicComponents(_0.APIBase):
    """ElasticModulusOrthotropicComponents

    This is a mastapy class.
    """

    TYPE = _ELASTIC_MODULUS_ORTHOTROPIC_COMPONENTS

    class _Cast_ElasticModulusOrthotropicComponents:
        """Special nested class for casting ElasticModulusOrthotropicComponents to subclasses."""

        def __init__(self, parent: 'ElasticModulusOrthotropicComponents'):
            self._parent = parent

        @property
        def elastic_modulus_orthotropic_components(self) -> 'ElasticModulusOrthotropicComponents':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElasticModulusOrthotropicComponents.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ex(self) -> 'float':
        """float: 'EX' is the original name of this property."""

        temp = self.wrapped.EX

        if temp is None:
            return 0.0

        return temp

    @ex.setter
    def ex(self, value: 'float'):
        self.wrapped.EX = float(value) if value else 0.0

    @property
    def ey(self) -> 'float':
        """float: 'EY' is the original name of this property."""

        temp = self.wrapped.EY

        if temp is None:
            return 0.0

        return temp

    @ey.setter
    def ey(self, value: 'float'):
        self.wrapped.EY = float(value) if value else 0.0

    @property
    def ez(self) -> 'float':
        """float: 'EZ' is the original name of this property."""

        temp = self.wrapped.EZ

        if temp is None:
            return 0.0

        return temp

    @ez.setter
    def ez(self, value: 'float'):
        self.wrapped.EZ = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'ElasticModulusOrthotropicComponents._Cast_ElasticModulusOrthotropicComponents':
        return self._Cast_ElasticModulusOrthotropicComponents(self)
