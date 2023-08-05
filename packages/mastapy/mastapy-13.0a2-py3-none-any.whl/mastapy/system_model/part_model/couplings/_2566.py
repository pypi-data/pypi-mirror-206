"""_2566.py

CVTPulley
"""
from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model.couplings import _2577, _2569
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CVTPulley')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulley',)


class CVTPulley(_2569.Pulley):
    """CVTPulley

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY

    class _Cast_CVTPulley:
        """Special nested class for casting CVTPulley to subclasses."""

        def __init__(self, parent: 'CVTPulley'):
            self._parent = parent

        @property
        def pulley(self):
            return self._parent._cast(_2569.Pulley)

        @property
        def coupling_half(self):
            from mastapy.system_model.part_model.couplings import _2563
            
            return self._parent._cast(_2563.CouplingHalf)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2444
            
            return self._parent._cast(_2444.MountableComponent)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2424
            
            return self._parent._cast(_2424.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def cvt_pulley(self) -> 'CVTPulley':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTPulley.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_moving_sheave_on_the_left(self) -> 'bool':
        """bool: 'IsMovingSheaveOnTheLeft' is the original name of this property."""

        temp = self.wrapped.IsMovingSheaveOnTheLeft

        if temp is None:
            return False

        return temp

    @is_moving_sheave_on_the_left.setter
    def is_moving_sheave_on_the_left(self, value: 'bool'):
        self.wrapped.IsMovingSheaveOnTheLeft = bool(value) if value else False

    @property
    def sliding_connection(self) -> 'list_with_selected_item.ListWithSelectedItem_ShaftHubConnection':
        """list_with_selected_item.ListWithSelectedItem_ShaftHubConnection: 'SlidingConnection' is the original name of this property."""

        temp = self.wrapped.SlidingConnection

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_ShaftHubConnection)(temp) if temp is not None else None

    @sliding_connection.setter
    def sliding_connection(self, value: 'list_with_selected_item.ListWithSelectedItem_ShaftHubConnection.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_ShaftHubConnection.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_ShaftHubConnection.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SlidingConnection = value

    @property
    def cast_to(self) -> 'CVTPulley._Cast_CVTPulley':
        return self._Cast_CVTPulley(self)
