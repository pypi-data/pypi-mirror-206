"""_2070.py

FrictionSources
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FRICTION_SOURCES = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'FrictionSources')


__docformat__ = 'restructuredtext en'
__all__ = ('FrictionSources',)


class FrictionSources(_0.APIBase):
    """FrictionSources

    This is a mastapy class.
    """

    TYPE = _FRICTION_SOURCES

    class _Cast_FrictionSources:
        """Special nested class for casting FrictionSources to subclasses."""

        def __init__(self, parent: 'FrictionSources'):
            self._parent = parent

        @property
        def friction_sources(self) -> 'FrictionSources':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FrictionSources.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def drag_loss(self) -> 'float':
        """float: 'DragLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DragLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling(self) -> 'float':
        """float: 'Rolling' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rolling

        if temp is None:
            return 0.0

        return temp

    @property
    def seals(self) -> 'float':
        """float: 'Seals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Seals

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding(self) -> 'float':
        """float: 'Sliding' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Sliding

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'FrictionSources._Cast_FrictionSources':
        return self._Cast_FrictionSources(self)
