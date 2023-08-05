"""_2465.py

SpecifiedParallelPartGroupDrawingOrder
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.projections import _2464
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIFIED_PARALLEL_PART_GROUP_DRAWING_ORDER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Projections', 'SpecifiedParallelPartGroupDrawingOrder')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecifiedParallelPartGroupDrawingOrder',)


class SpecifiedParallelPartGroupDrawingOrder(_0.APIBase):
    """SpecifiedParallelPartGroupDrawingOrder

    This is a mastapy class.
    """

    TYPE = _SPECIFIED_PARALLEL_PART_GROUP_DRAWING_ORDER

    class _Cast_SpecifiedParallelPartGroupDrawingOrder:
        """Special nested class for casting SpecifiedParallelPartGroupDrawingOrder to subclasses."""

        def __init__(self, parent: 'SpecifiedParallelPartGroupDrawingOrder'):
            self._parent = parent

        @property
        def specified_parallel_part_group_drawing_order(self) -> 'SpecifiedParallelPartGroupDrawingOrder':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecifiedParallelPartGroupDrawingOrder.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def specified_groups(self) -> 'List[_2464.SpecifiedConcentricPartGroupDrawingOrder]':
        """List[SpecifiedConcentricPartGroupDrawingOrder]: 'SpecifiedGroups' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecifiedGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpecifiedParallelPartGroupDrawingOrder._Cast_SpecifiedParallelPartGroupDrawingOrder':
        return self._Cast_SpecifiedParallelPartGroupDrawingOrder(self)
