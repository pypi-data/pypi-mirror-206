"""_1289.py

Stator
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines import _1290, _1296, _1237
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'Stator')


__docformat__ = 'restructuredtext en'
__all__ = ('Stator',)


class Stator(_1237.AbstractStator):
    """Stator

    This is a mastapy class.
    """

    TYPE = _STATOR

    class _Cast_Stator:
        """Special nested class for casting Stator to subclasses."""

        def __init__(self, parent: 'Stator'):
            self._parent = parent

        @property
        def abstract_stator(self):
            return self._parent._cast(_1237.AbstractStator)

        @property
        def stator(self) -> 'Stator':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Stator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_stator_cut_out_specifications(self) -> 'int':
        """int: 'NumberOfStatorCutOutSpecifications' is the original name of this property."""

        temp = self.wrapped.NumberOfStatorCutOutSpecifications

        if temp is None:
            return 0

        return temp

    @number_of_stator_cut_out_specifications.setter
    def number_of_stator_cut_out_specifications(self, value: 'int'):
        self.wrapped.NumberOfStatorCutOutSpecifications = int(value) if value else 0

    @property
    def radius_at_mid_coil_height(self) -> 'float':
        """float: 'RadiusAtMidCoilHeight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadiusAtMidCoilHeight

        if temp is None:
            return 0.0

        return temp

    @property
    def stator_cut_out_specifications(self) -> 'List[_1290.StatorCutOutSpecification]':
        """List[StatorCutOutSpecification]: 'StatorCutOutSpecifications' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorCutOutSpecifications

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def tooth_and_slot(self) -> '_1296.ToothAndSlot':
        """ToothAndSlot: 'ToothAndSlot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothAndSlot

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'Stator._Cast_Stator':
        return self._Cast_Stator(self)
