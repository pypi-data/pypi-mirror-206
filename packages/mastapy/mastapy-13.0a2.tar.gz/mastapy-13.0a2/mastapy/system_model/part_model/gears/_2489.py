"""_2489.py

ActiveCylindricalGearSetDesignSelection
"""
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2490
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_CYLINDRICAL_GEAR_SET_DESIGN_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ActiveCylindricalGearSetDesignSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveCylindricalGearSetDesignSelection',)


class ActiveCylindricalGearSetDesignSelection(_2490.ActiveGearSetDesignSelection):
    """ActiveCylindricalGearSetDesignSelection

    This is a mastapy class.
    """

    TYPE = _ACTIVE_CYLINDRICAL_GEAR_SET_DESIGN_SELECTION

    class _Cast_ActiveCylindricalGearSetDesignSelection:
        """Special nested class for casting ActiveCylindricalGearSetDesignSelection to subclasses."""

        def __init__(self, parent: 'ActiveCylindricalGearSetDesignSelection'):
            self._parent = parent

        @property
        def active_gear_set_design_selection(self):
            return self._parent._cast(_2490.ActiveGearSetDesignSelection)

        @property
        def part_detail_selection(self):
            from mastapy.system_model.part_model.configurations import _2597
            from mastapy.system_model.part_model.gears import _2511
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_2597.PartDetailSelection)

        @property
        def active_cylindrical_gear_set_design_selection(self) -> 'ActiveCylindricalGearSetDesignSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ActiveCylindricalGearSetDesignSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def micro_geometry_selection(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'MicroGeometrySelection' is the original name of this property."""

        temp = self.wrapped.MicroGeometrySelection

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @micro_geometry_selection.setter
    def micro_geometry_selection(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.MicroGeometrySelection = value

    @property
    def cast_to(self) -> 'ActiveCylindricalGearSetDesignSelection._Cast_ActiveCylindricalGearSetDesignSelection':
        return self._Cast_ActiveCylindricalGearSetDesignSelection(self)
