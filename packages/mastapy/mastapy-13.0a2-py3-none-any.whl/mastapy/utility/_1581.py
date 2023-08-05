"""_1581.py

MKLVersion
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MKL_VERSION = python_net_import('SMT.MastaAPI.Utility', 'MKLVersion')


__docformat__ = 'restructuredtext en'
__all__ = ('MKLVersion',)


class MKLVersion(_0.APIBase):
    """MKLVersion

    This is a mastapy class.
    """

    TYPE = _MKL_VERSION

    class _Cast_MKLVersion:
        """Special nested class for casting MKLVersion to subclasses."""

        def __init__(self, parent: 'MKLVersion'):
            self._parent = parent

        @property
        def mkl_version(self) -> 'MKLVersion':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MKLVersion.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def build(self) -> 'str':
        """str: 'Build' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Build

        if temp is None:
            return ''

        return temp

    @property
    def platform(self) -> 'str':
        """str: 'Platform' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Platform

        if temp is None:
            return ''

        return temp

    @property
    def processor(self) -> 'str':
        """str: 'Processor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Processor

        if temp is None:
            return ''

        return temp

    @property
    def product_status(self) -> 'str':
        """str: 'ProductStatus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProductStatus

        if temp is None:
            return ''

        return temp

    @property
    def version(self) -> 'str':
        """str: 'Version' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Version

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'MKLVersion._Cast_MKLVersion':
        return self._Cast_MKLVersion(self)
