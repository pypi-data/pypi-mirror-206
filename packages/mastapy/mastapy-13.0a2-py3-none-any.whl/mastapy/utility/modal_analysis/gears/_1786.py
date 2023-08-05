"""_1786.py

GearMeshForTE
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.utility.modal_analysis.gears import _1787, _1791
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_FOR_TE = python_net_import('SMT.MastaAPI.Utility.ModalAnalysis.Gears', 'GearMeshForTE')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshForTE',)


class GearMeshForTE(_1791.OrderForTE):
    """GearMeshForTE

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_FOR_TE

    class _Cast_GearMeshForTE:
        """Special nested class for casting GearMeshForTE to subclasses."""

        def __init__(self, parent: 'GearMeshForTE'):
            self._parent = parent

        @property
        def order_for_te(self):
            return self._parent._cast(_1791.OrderForTE)

        @property
        def gear_mesh_for_te(self) -> 'GearMeshForTE':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshForTE.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_teeth(self) -> 'str':
        """str: 'NumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return ''

        return temp

    @number_of_teeth.setter
    def number_of_teeth(self, value: 'str'):
        self.wrapped.NumberOfTeeth = str(value) if value else ''

    @property
    def attached_gears(self) -> 'List[_1787.GearOrderForTE]':
        """List[GearOrderForTE]: 'AttachedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AttachedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshForTE._Cast_GearMeshForTE':
        return self._Cast_GearMeshForTE(self)
