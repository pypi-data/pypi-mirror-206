"""_1243.py

CADStator
"""
from mastapy._internal import constructor
from mastapy.electric_machines import _1244, _1237
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_STATOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'CADStator')


__docformat__ = 'restructuredtext en'
__all__ = ('CADStator',)


class CADStator(_1237.AbstractStator):
    """CADStator

    This is a mastapy class.
    """

    TYPE = _CAD_STATOR

    class _Cast_CADStator:
        """Special nested class for casting CADStator to subclasses."""

        def __init__(self, parent: 'CADStator'):
            self._parent = parent

        @property
        def abstract_stator(self):
            return self._parent._cast(_1237.AbstractStator)

        @property
        def cad_stator(self) -> 'CADStator':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CADStator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_slots_for_imported_sector(self) -> 'int':
        """int: 'NumberOfSlotsForImportedSector' is the original name of this property."""

        temp = self.wrapped.NumberOfSlotsForImportedSector

        if temp is None:
            return 0

        return temp

    @number_of_slots_for_imported_sector.setter
    def number_of_slots_for_imported_sector(self, value: 'int'):
        self.wrapped.NumberOfSlotsForImportedSector = int(value) if value else 0

    @property
    def tooth_and_slot(self) -> '_1244.CADToothAndSlot':
        """CADToothAndSlot: 'ToothAndSlot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothAndSlot

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CADStator._Cast_CADStator':
        return self._Cast_CADStator(self)
