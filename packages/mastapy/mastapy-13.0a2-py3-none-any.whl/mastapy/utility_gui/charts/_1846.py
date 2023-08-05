"""_1846.py

PointsForSurface
"""
from typing import List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINTS_FOR_SURFACE = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'PointsForSurface')


__docformat__ = 'restructuredtext en'
__all__ = ('PointsForSurface',)


class PointsForSurface(_0.APIBase):
    """PointsForSurface

    This is a mastapy class.
    """

    TYPE = _POINTS_FOR_SURFACE

    class _Cast_PointsForSurface:
        """Special nested class for casting PointsForSurface to subclasses."""

        def __init__(self, parent: 'PointsForSurface'):
            self._parent = parent

        @property
        def points_for_surface(self) -> 'PointsForSurface':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PointsForSurface.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def points(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'Points' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Points

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PointsForSurface._Cast_PointsForSurface':
        return self._Cast_PointsForSurface(self)
