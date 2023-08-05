"""_2251.py

ComponentConnection
"""
from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2424
from mastapy.system_model.connections_and_sockets import _2252
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'ComponentConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentConnection',)


class ComponentConnection(_2252.ComponentMeasurer):
    """ComponentConnection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_CONNECTION

    class _Cast_ComponentConnection:
        """Special nested class for casting ComponentConnection to subclasses."""

        def __init__(self, parent: 'ComponentConnection'):
            self._parent = parent

        @property
        def component_measurer(self):
            return self._parent._cast(_2252.ComponentMeasurer)

        @property
        def cylindrical_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2256
            
            return self._parent._cast(_2256.CylindricalComponentConnection)

        @property
        def component_connection(self) -> 'ComponentConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_view(self) -> 'Image':
        """Image: 'AssemblyView' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def connected_components_socket(self) -> 'str':
        """str: 'ConnectedComponentsSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectedComponentsSocket

        if temp is None:
            return ''

        return temp

    @property
    def detail_view(self) -> 'Image':
        """Image: 'DetailView' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DetailView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def socket(self) -> 'str':
        """str: 'Socket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Socket

        if temp is None:
            return ''

        return temp

    @property
    def connected_component(self) -> '_2424.Component':
        """Component: 'ConnectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectedComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def delete(self):
        """ 'Delete' is the original name of this method."""

        self.wrapped.Delete()

    def swap(self):
        """ 'Swap' is the original name of this method."""

        self.wrapped.Swap()

    @property
    def cast_to(self) -> 'ComponentConnection._Cast_ComponentConnection':
        return self._Cast_ComponentConnection(self)
