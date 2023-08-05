"""_1499.py

FacetedBody
"""
from typing import List

from mastapy.math_utility import _1500
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACETED_BODY = python_net_import('SMT.MastaAPI.MathUtility', 'FacetedBody')


__docformat__ = 'restructuredtext en'
__all__ = ('FacetedBody',)


class FacetedBody(_0.APIBase):
    """FacetedBody

    This is a mastapy class.
    """

    TYPE = _FACETED_BODY

    class _Cast_FacetedBody:
        """Special nested class for casting FacetedBody to subclasses."""

        def __init__(self, parent: 'FacetedBody'):
            self._parent = parent

        @property
        def faceted_body(self) -> 'FacetedBody':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FacetedBody.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def surfaces(self) -> 'List[_1500.FacetedSurface]':
        """List[FacetedSurface]: 'Surfaces' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Surfaces

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_surface(self, vertices: 'List[List[float]]', normals: 'List[List[float]]', facets: 'List[List[int]]'):
        """ 'AddSurface' is the original name of this method.

        Args:
            vertices (List[List[float]])
            normals (List[List[float]])
            facets (List[List[int]])
        """

        vertices = conversion.mp_to_pn_objects_in_list(vertices)
        normals = conversion.mp_to_pn_objects_in_list(normals)
        facets = conversion.mp_to_pn_objects_in_list(facets)
        self.wrapped.AddSurface(vertices, normals, facets)

    @property
    def cast_to(self) -> 'FacetedBody._Cast_FacetedBody':
        return self._Cast_FacetedBody(self)
