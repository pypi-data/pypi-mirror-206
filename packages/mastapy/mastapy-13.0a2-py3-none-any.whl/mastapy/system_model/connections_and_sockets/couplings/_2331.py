"""_2331.py

SpringDamperConnection
"""
from mastapy.system_model import _2186
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.nodal_analysis import _72
from mastapy.system_model.connections_and_sockets.couplings import _2327
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'SpringDamperConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnection',)


class SpringDamperConnection(_2327.CouplingConnection):
    """SpringDamperConnection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION

    class _Cast_SpringDamperConnection:
        """Special nested class for casting SpringDamperConnection to subclasses."""

        def __init__(self, parent: 'SpringDamperConnection'):
            self._parent = parent

        @property
        def coupling_connection(self):
            return self._parent._cast(_2327.CouplingConnection)

        @property
        def inter_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2262
            
            return self._parent._cast(_2262.InterMountableComponentConnection)

        @property
        def connection(self):
            from mastapy.system_model.connections_and_sockets import _2253
            
            return self._parent._cast(_2253.Connection)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def spring_damper_connection(self) -> 'SpringDamperConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpringDamperConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def damping_option(self) -> '_2186.ComponentDampingOption':
        """ComponentDampingOption: 'DampingOption' is the original name of this property."""

        temp = self.wrapped.DampingOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _2186.ComponentDampingOption)
        return constructor.new_from_mastapy_type(_2186.ComponentDampingOption)(value) if value is not None else None

    @damping_option.setter
    def damping_option(self, value: '_2186.ComponentDampingOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _2186.ComponentDampingOption.type_())
        self.wrapped.DampingOption = value

    @property
    def damping(self) -> '_72.LinearDampingConnectionProperties':
        """LinearDampingConnectionProperties: 'Damping' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Damping

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SpringDamperConnection._Cast_SpringDamperConnection':
        return self._Cast_SpringDamperConnection(self)
