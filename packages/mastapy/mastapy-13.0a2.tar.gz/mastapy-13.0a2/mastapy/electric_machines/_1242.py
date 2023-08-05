"""_1242.py

CADRotor
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.electric_machines import _1241, _1283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_ROTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'CADRotor')


__docformat__ = 'restructuredtext en'
__all__ = ('CADRotor',)


class CADRotor(_1283.Rotor):
    """CADRotor

    This is a mastapy class.
    """

    TYPE = _CAD_ROTOR

    class _Cast_CADRotor:
        """Special nested class for casting CADRotor to subclasses."""

        def __init__(self, parent: 'CADRotor'):
            self._parent = parent

        @property
        def rotor(self):
            return self._parent._cast(_1283.Rotor)

        @property
        def cad_rotor(self) -> 'CADRotor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CADRotor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_magnet_layers(self) -> 'int':
        """int: 'NumberOfMagnetLayers' is the original name of this property."""

        temp = self.wrapped.NumberOfMagnetLayers

        if temp is None:
            return 0

        return temp

    @number_of_magnet_layers.setter
    def number_of_magnet_layers(self, value: 'int'):
        self.wrapped.NumberOfMagnetLayers = int(value) if value else 0

    @property
    def offset_of_additional_line_used_for_estimating_kair(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OffsetOfAdditionalLineUsedForEstimatingKair' is the original name of this property."""

        temp = self.wrapped.OffsetOfAdditionalLineUsedForEstimatingKair

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @offset_of_additional_line_used_for_estimating_kair.setter
    def offset_of_additional_line_used_for_estimating_kair(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OffsetOfAdditionalLineUsedForEstimatingKair = value

    @property
    def magnet_layers(self) -> 'List[_1241.CADMagnetsForLayer]':
        """List[CADMagnetsForLayer]: 'MagnetLayers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MagnetLayers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CADRotor._Cast_CADRotor':
        return self._Cast_CADRotor(self)
