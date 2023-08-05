"""_1244.py

CADToothAndSlot
"""
from typing import List

from mastapy.electric_machines import _1266, _1301, _1238
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_TOOTH_AND_SLOT = python_net_import('SMT.MastaAPI.ElectricMachines', 'CADToothAndSlot')


__docformat__ = 'restructuredtext en'
__all__ = ('CADToothAndSlot',)


class CADToothAndSlot(_1238.AbstractToothAndSlot):
    """CADToothAndSlot

    This is a mastapy class.
    """

    TYPE = _CAD_TOOTH_AND_SLOT

    class _Cast_CADToothAndSlot:
        """Special nested class for casting CADToothAndSlot to subclasses."""

        def __init__(self, parent: 'CADToothAndSlot'):
            self._parent = parent

        @property
        def abstract_tooth_and_slot(self):
            return self._parent._cast(_1238.AbstractToothAndSlot)

        @property
        def cad_tooth_and_slot(self) -> 'CADToothAndSlot':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CADToothAndSlot.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def individual_conductor_specification_source(self) -> '_1266.IndividualConductorSpecificationSource':
        """IndividualConductorSpecificationSource: 'IndividualConductorSpecificationSource' is the original name of this property."""

        temp = self.wrapped.IndividualConductorSpecificationSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1266.IndividualConductorSpecificationSource)
        return constructor.new_from_mastapy_type(_1266.IndividualConductorSpecificationSource)(value) if value is not None else None

    @individual_conductor_specification_source.setter
    def individual_conductor_specification_source(self, value: '_1266.IndividualConductorSpecificationSource'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1266.IndividualConductorSpecificationSource.type_())
        self.wrapped.IndividualConductorSpecificationSource = value

    @property
    def conductors(self) -> 'List[_1301.WindingConductor]':
        """List[WindingConductor]: 'Conductors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Conductors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CADToothAndSlot._Cast_CADToothAndSlot':
        return self._Cast_CADToothAndSlot(self)
