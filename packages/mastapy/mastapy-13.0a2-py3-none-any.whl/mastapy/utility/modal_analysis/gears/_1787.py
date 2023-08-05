"""_1787.py

GearOrderForTE
"""
from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility.modal_analysis.gears import _1788, _1791, _1793
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_ORDER_FOR_TE = python_net_import('SMT.MastaAPI.Utility.ModalAnalysis.Gears', 'GearOrderForTE')


__docformat__ = 'restructuredtext en'
__all__ = ('GearOrderForTE',)


class GearOrderForTE(_1793.OrderWithRadius):
    """GearOrderForTE

    This is a mastapy class.
    """

    TYPE = _GEAR_ORDER_FOR_TE

    class _Cast_GearOrderForTE:
        """Special nested class for casting GearOrderForTE to subclasses."""

        def __init__(self, parent: 'GearOrderForTE'):
            self._parent = parent

        @property
        def order_with_radius(self):
            return self._parent._cast(_1793.OrderWithRadius)

        @property
        def order_for_te(self):
            return self._parent._cast(_1791.OrderForTE)

        @property
        def gear_order_for_te(self) -> 'GearOrderForTE':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearOrderForTE.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_teeth(self) -> 'int':
        """int: 'NumberOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @property
    def position(self) -> '_1788.GearPositions':
        """GearPositions: 'Position' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Position

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1788.GearPositions)
        return constructor.new_from_mastapy_type(_1788.GearPositions)(value) if value is not None else None

    @property
    def additional_orders_and_harmonics(self) -> 'List[_1791.OrderForTE]':
        """List[OrderForTE]: 'AdditionalOrdersAndHarmonics' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdditionalOrdersAndHarmonics

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearOrderForTE._Cast_GearOrderForTE':
        return self._Cast_GearOrderForTE(self)
