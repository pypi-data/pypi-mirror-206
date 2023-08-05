"""_2595.py

BearingDetailSelection
"""
from typing import List

from mastapy.bearings.bearing_results import _1945
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.system_model.part_model import _2421, _2419
from mastapy.system_model.part_model.configurations import _2597
from mastapy.bearings.bearing_designs import _2115
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DETAIL_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'BearingDetailSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDetailSelection',)


class BearingDetailSelection(_2597.PartDetailSelection['_2419.Bearing', '_2115.BearingDesign']):
    """BearingDetailSelection

    This is a mastapy class.
    """

    TYPE = _BEARING_DETAIL_SELECTION

    class _Cast_BearingDetailSelection:
        """Special nested class for casting BearingDetailSelection to subclasses."""

        def __init__(self, parent: 'BearingDetailSelection'):
            self._parent = parent

        @property
        def part_detail_selection(self):
            return self._parent._cast(_2597.PartDetailSelection)

        @property
        def bearing_detail_selection(self) -> 'BearingDetailSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingDetailSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orientation(self) -> '_1945.Orientations':
        """Orientations: 'Orientation' is the original name of this property."""

        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1945.Orientations)
        return constructor.new_from_mastapy_type(_1945.Orientations)(value) if value is not None else None

    @orientation.setter
    def orientation(self, value: '_1945.Orientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1945.Orientations.type_())
        self.wrapped.Orientation = value

    @property
    def mounting(self) -> 'List[_2421.BearingRaceMountingOptions]':
        """List[BearingRaceMountingOptions]: 'Mounting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mounting

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BearingDetailSelection._Cast_BearingDetailSelection':
        return self._Cast_BearingDetailSelection(self)
