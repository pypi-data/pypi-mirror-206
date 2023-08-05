﻿"""_6858.py

GearSetHarmonicLoadData
"""
from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6857
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.math_utility import _1501
from mastapy.electric_machines.harmonic_load_data import _1368
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_HARMONIC_LOAD_DATA = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'GearSetHarmonicLoadData')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetHarmonicLoadData',)


class GearSetHarmonicLoadData(_1368.HarmonicLoadDataBase):
    """GearSetHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_HARMONIC_LOAD_DATA

    class _Cast_GearSetHarmonicLoadData:
        """Special nested class for casting GearSetHarmonicLoadData to subclasses."""

        def __init__(self, parent: 'GearSetHarmonicLoadData'):
            self._parent = parent

        @property
        def harmonic_load_data_base(self):
            return self._parent._cast(_1368.HarmonicLoadDataBase)

        @property
        def conical_gear_set_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6811
            
            return self._parent._cast(_6811.ConicalGearSetHarmonicLoadData)

        @property
        def cylindrical_gear_set_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6828
            
            return self._parent._cast(_6828.CylindricalGearSetHarmonicLoadData)

        @property
        def gear_set_harmonic_load_data(self) -> 'GearSetHarmonicLoadData':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetHarmonicLoadData.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_order_as_rotational_order_of_shaft(self) -> 'float':
        """float: 'ExcitationOrderAsRotationalOrderOfShaft' is the original name of this property."""

        temp = self.wrapped.ExcitationOrderAsRotationalOrderOfShaft

        if temp is None:
            return 0.0

        return temp

    @excitation_order_as_rotational_order_of_shaft.setter
    def excitation_order_as_rotational_order_of_shaft(self, value: 'float'):
        self.wrapped.ExcitationOrderAsRotationalOrderOfShaft = float(value) if value else 0.0

    @property
    def gear_mesh_te_order_type(self) -> '_6857.GearMeshTEOrderType':
        """GearMeshTEOrderType: 'GearMeshTEOrderType' is the original name of this property."""

        temp = self.wrapped.GearMeshTEOrderType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _6857.GearMeshTEOrderType)
        return constructor.new_from_mastapy_type(_6857.GearMeshTEOrderType)(value) if value is not None else None

    @gear_mesh_te_order_type.setter
    def gear_mesh_te_order_type(self, value: '_6857.GearMeshTEOrderType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _6857.GearMeshTEOrderType.type_())
        self.wrapped.GearMeshTEOrderType = value

    @property
    def reference_shaft(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'ReferenceShaft' is the original name of this property."""

        temp = self.wrapped.ReferenceShaft

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @reference_shaft.setter
    def reference_shaft(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.ReferenceShaft = value

    @property
    def excitations(self) -> 'List[_1501.FourierSeries]':
        """List[FourierSeries]: 'Excitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def copy_data_to_duplicate_planetary_meshes(self):
        """ 'CopyDataToDuplicatePlanetaryMeshes' is the original name of this method."""

        self.wrapped.CopyDataToDuplicatePlanetaryMeshes()

    @property
    def cast_to(self) -> 'GearSetHarmonicLoadData._Cast_GearSetHarmonicLoadData':
        return self._Cast_GearSetHarmonicLoadData(self)
