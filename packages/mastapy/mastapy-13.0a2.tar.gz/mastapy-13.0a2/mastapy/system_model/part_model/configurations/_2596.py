"""_2596.py

PartDetailConfiguration
"""
from typing import List, TypeVar, Generic

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy.system_model.part_model import _2448
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_DETAIL_CONFIGURATION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'PartDetailConfiguration')


__docformat__ = 'restructuredtext en'
__all__ = ('PartDetailConfiguration',)


TPartDetailSelection = TypeVar('TPartDetailSelection')
TPart = TypeVar('TPart', bound='_2448.Part')
TSelectableItem = TypeVar('TSelectableItem')


class PartDetailConfiguration(_0.APIBase, Generic[TPartDetailSelection, TPart, TSelectableItem]):
    """PartDetailConfiguration

    This is a mastapy class.

    Generic Types:
        TPartDetailSelection
        TPart
        TSelectableItem
    """

    TYPE = _PART_DETAIL_CONFIGURATION

    class _Cast_PartDetailConfiguration:
        """Special nested class for casting PartDetailConfiguration to subclasses."""

        def __init__(self, parent: 'PartDetailConfiguration'):
            self._parent = parent

        @property
        def active_gear_set_design_selection_group(self):
            from mastapy.system_model.part_model.gears import _2491
            
            return self._parent._cast(_2491.ActiveGearSetDesignSelectionGroup)

        @property
        def active_fe_substructure_selection_group(self):
            from mastapy.system_model.part_model.configurations import _2591
            
            return self._parent._cast(_2591.ActiveFESubstructureSelectionGroup)

        @property
        def active_shaft_design_selection_group(self):
            from mastapy.system_model.part_model.configurations import _2593
            
            return self._parent._cast(_2593.ActiveShaftDesignSelectionGroup)

        @property
        def bearing_detail_configuration(self):
            from mastapy.system_model.part_model.configurations import _2594
            
            return self._parent._cast(_2594.BearingDetailConfiguration)

        @property
        def part_detail_configuration(self) -> 'PartDetailConfiguration':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartDetailConfiguration.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def selections(self) -> 'List[TPartDetailSelection]':
        """List[TPartDetailSelection]: 'Selections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Selections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def delete_configuration(self):
        """ 'DeleteConfiguration' is the original name of this method."""

        self.wrapped.DeleteConfiguration()

    def select_configuration(self):
        """ 'SelectConfiguration' is the original name of this method."""

        self.wrapped.SelectConfiguration()

    @property
    def cast_to(self) -> 'PartDetailConfiguration._Cast_PartDetailConfiguration':
        return self._Cast_PartDetailConfiguration(self)
