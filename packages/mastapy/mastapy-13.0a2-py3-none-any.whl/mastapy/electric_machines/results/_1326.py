"""_1326.py

ElectricMachineResultsViewable
"""
from typing import List

from mastapy.electric_machines.results import _1327, _1315
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.electric_machines import _1285, _1282
from mastapy.utility.property import _1829
from mastapy.nodal_analysis.elmer import _169
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_VIEWABLE = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'ElectricMachineResultsViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineResultsViewable',)


class ElectricMachineResultsViewable(_169.ElmerResultsViewable):
    """ElectricMachineResultsViewable

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS_VIEWABLE

    class _Cast_ElectricMachineResultsViewable:
        """Special nested class for casting ElectricMachineResultsViewable to subclasses."""

        def __init__(self, parent: 'ElectricMachineResultsViewable'):
            self._parent = parent

        @property
        def elmer_results_viewable(self):
            return self._parent._cast(_169.ElmerResultsViewable)

        @property
        def electric_machine_results_viewable(self) -> 'ElectricMachineResultsViewable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineResultsViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force_view_options(self) -> '_1327.ElectricMachineForceViewOptions':
        """ElectricMachineForceViewOptions: 'ForceViewOptions' is the original name of this property."""

        temp = self.wrapped.ForceViewOptions

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1327.ElectricMachineForceViewOptions)
        return constructor.new_from_mastapy_type(_1327.ElectricMachineForceViewOptions)(value) if value is not None else None

    @force_view_options.setter
    def force_view_options(self, value: '_1327.ElectricMachineForceViewOptions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1327.ElectricMachineForceViewOptions.type_())
        self.wrapped.ForceViewOptions = value

    @property
    def number_of_lines(self) -> 'int':
        """int: 'NumberOfLines' is the original name of this property."""

        temp = self.wrapped.NumberOfLines

        if temp is None:
            return 0

        return temp

    @number_of_lines.setter
    def number_of_lines(self, value: 'int'):
        self.wrapped.NumberOfLines = int(value) if value else 0

    @property
    def results(self) -> 'list_with_selected_item.ListWithSelectedItem_ElectricMachineResults':
        """list_with_selected_item.ListWithSelectedItem_ElectricMachineResults: 'Results' is the original name of this property."""

        temp = self.wrapped.Results

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_ElectricMachineResults)(temp) if temp is not None else None

    @results.setter
    def results(self, value: 'list_with_selected_item.ListWithSelectedItem_ElectricMachineResults.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineResults.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineResults.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.Results = value

    @property
    def show_field_lines(self) -> 'bool':
        """bool: 'ShowFieldLines' is the original name of this property."""

        temp = self.wrapped.ShowFieldLines

        if temp is None:
            return False

        return temp

    @show_field_lines.setter
    def show_field_lines(self, value: 'bool'):
        self.wrapped.ShowFieldLines = bool(value) if value else False

    @property
    def slice(self) -> 'list_with_selected_item.ListWithSelectedItem_RotorSkewSlice':
        """list_with_selected_item.ListWithSelectedItem_RotorSkewSlice: 'Slice' is the original name of this property."""

        temp = self.wrapped.Slice

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_RotorSkewSlice)(temp) if temp is not None else None

    @slice.setter
    def slice(self, value: 'list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.Slice = value

    @property
    def parts_to_view(self) -> 'List[_1829.EnumWithBool[_1282.RegionID]]':
        """List[EnumWithBool[RegionID]]: 'PartsToView' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartsToView

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def deselect_all(self):
        """ 'DeselectAll' is the original name of this method."""

        self.wrapped.DeselectAll()

    def select_all(self):
        """ 'SelectAll' is the original name of this method."""

        self.wrapped.SelectAll()

    @property
    def cast_to(self) -> 'ElectricMachineResultsViewable._Cast_ElectricMachineResultsViewable':
        return self._Cast_ElectricMachineResultsViewable(self)
