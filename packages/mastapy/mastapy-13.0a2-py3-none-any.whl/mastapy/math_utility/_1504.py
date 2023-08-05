"""_1504.py

HarmonicValue
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_VALUE = python_net_import('SMT.MastaAPI.MathUtility', 'HarmonicValue')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicValue',)


class HarmonicValue(_0.APIBase):
    """HarmonicValue

    This is a mastapy class.
    """

    TYPE = _HARMONIC_VALUE

    class _Cast_HarmonicValue:
        """Special nested class for casting HarmonicValue to subclasses."""

        def __init__(self, parent: 'HarmonicValue'):
            self._parent = parent

        @property
        def harmonic_value(self) -> 'HarmonicValue':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicValue.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def amplitude(self) -> 'float':
        """float: 'Amplitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Amplitude

        if temp is None:
            return 0.0

        return temp

    @property
    def harmonic_index(self) -> 'int':
        """int: 'HarmonicIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicIndex

        if temp is None:
            return 0

        return temp

    @property
    def phase(self) -> 'float':
        """float: 'Phase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Phase

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'HarmonicValue._Cast_HarmonicValue':
        return self._Cast_HarmonicValue(self)
