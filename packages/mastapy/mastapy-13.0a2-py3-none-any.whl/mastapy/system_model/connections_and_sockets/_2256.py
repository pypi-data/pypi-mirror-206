"""_2256.py

CylindricalComponentConnection
"""
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2251
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'CylindricalComponentConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalComponentConnection',)


class CylindricalComponentConnection(_2251.ComponentConnection):
    """CylindricalComponentConnection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_COMPONENT_CONNECTION

    class _Cast_CylindricalComponentConnection:
        """Special nested class for casting CylindricalComponentConnection to subclasses."""

        def __init__(self, parent: 'CylindricalComponentConnection'):
            self._parent = parent

        @property
        def component_connection(self):
            return self._parent._cast(_2251.ComponentConnection)

        @property
        def component_measurer(self):
            from mastapy.system_model.connections_and_sockets import _2252
            
            return self._parent._cast(_2252.ComponentMeasurer)

        @property
        def cylindrical_component_connection(self) -> 'CylindricalComponentConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalComponentConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measuring_position_for_component(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'MeasuringPositionForComponent' is the original name of this property."""

        temp = self.wrapped.MeasuringPositionForComponent

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @measuring_position_for_component.setter
    def measuring_position_for_component(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.MeasuringPositionForComponent = value

    @property
    def measuring_position_for_connected_component(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'MeasuringPositionForConnectedComponent' is the original name of this property."""

        temp = self.wrapped.MeasuringPositionForConnectedComponent

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @measuring_position_for_connected_component.setter
    def measuring_position_for_connected_component(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.MeasuringPositionForConnectedComponent = value

    @property
    def cast_to(self) -> 'CylindricalComponentConnection._Cast_CylindricalComponentConnection':
        return self._Cast_CylindricalComponentConnection(self)
