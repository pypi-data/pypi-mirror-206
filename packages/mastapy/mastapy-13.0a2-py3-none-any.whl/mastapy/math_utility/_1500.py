"""_1500.py

FacetedSurface
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACETED_SURFACE = python_net_import('SMT.MastaAPI.MathUtility', 'FacetedSurface')


__docformat__ = 'restructuredtext en'
__all__ = ('FacetedSurface',)


class FacetedSurface(_0.APIBase):
    """FacetedSurface

    This is a mastapy class.
    """

    TYPE = _FACETED_SURFACE

    class _Cast_FacetedSurface:
        """Special nested class for casting FacetedSurface to subclasses."""

        def __init__(self, parent: 'FacetedSurface'):
            self._parent = parent

        @property
        def faceted_surface(self) -> 'FacetedSurface':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FacetedSurface.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def facets(self) -> 'List[List[int]]':
        """List[List[int]]: 'Facets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Facets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)
        return value

    @property
    def normals(self) -> 'List[List[float]]':
        """List[List[float]]: 'Normals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Normals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def vertices(self) -> 'List[List[float]]':
        """List[List[float]]: 'Vertices' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Vertices

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def cast_to(self) -> 'FacetedSurface._Cast_FacetedSurface':
        return self._Cast_FacetedSurface(self)
