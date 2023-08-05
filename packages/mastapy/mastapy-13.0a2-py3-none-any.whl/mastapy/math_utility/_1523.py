"""_1523.py

Vector2DListAccessor
"""
from typing import List

from mastapy._math.vector_2d import Vector2D
from mastapy._internal import conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VECTOR_2D_LIST_ACCESSOR = python_net_import('SMT.MastaAPI.MathUtility', 'Vector2DListAccessor')


__docformat__ = 'restructuredtext en'
__all__ = ('Vector2DListAccessor',)


class Vector2DListAccessor(_0.APIBase):
    """Vector2DListAccessor

    This is a mastapy class.
    """

    TYPE = _VECTOR_2D_LIST_ACCESSOR

    class _Cast_Vector2DListAccessor:
        """Special nested class for casting Vector2DListAccessor to subclasses."""

        def __init__(self, parent: 'Vector2DListAccessor'):
            self._parent = parent

        @property
        def vector_2d_list_accessor(self) -> 'Vector2DListAccessor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Vector2DListAccessor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def create_new_from_vector_list(self, list: 'List[Vector2D]') -> 'Vector2DListAccessor':
        """ 'CreateNewFromVectorList' is the original name of this method.

        Args:
            list (List[Vector2D])

        Returns:
            mastapy.math_utility.Vector2DListAccessor
        """

        list = conversion.mp_to_pn_objects_in_list(list)
        method_result = self.wrapped.CreateNewFromVectorList(list)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_vector_list(self) -> 'List[Vector2D]':
        """ 'GetVectorList' is the original name of this method.

        Returns:
            List[Vector2D]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetVectorList())

    @property
    def cast_to(self) -> 'Vector2DListAccessor._Cast_Vector2DListAccessor':
        return self._Cast_Vector2DListAccessor(self)
