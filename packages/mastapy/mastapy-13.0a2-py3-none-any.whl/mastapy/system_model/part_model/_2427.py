"""_2427.py

Connector
"""
from typing import Optional

from mastapy.system_model.part_model import (
    _2415, _2424, _2425, _2444
)
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2253, _2257
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Connector')


__docformat__ = 'restructuredtext en'
__all__ = ('Connector',)


class Connector(_2444.MountableComponent):
    """Connector

    This is a mastapy class.
    """

    TYPE = _CONNECTOR

    class _Cast_Connector:
        """Special nested class for casting Connector to subclasses."""

        def __init__(self, parent: 'Connector'):
            self._parent = parent

        @property
        def mountable_component(self):
            return self._parent._cast(_2444.MountableComponent)

        @property
        def component(self):
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
        def bearing(self):
            from mastapy.system_model.part_model import _2419
            
            return self._parent._cast(_2419.Bearing)

        @property
        def oil_seal(self):
            from mastapy.system_model.part_model import _2446
            
            return self._parent._cast(_2446.OilSeal)

        @property
        def shaft_hub_connection(self):
            from mastapy.system_model.part_model.couplings import _2577
            
            return self._parent._cast(_2577.ShaftHubConnection)

        @property
        def connector(self) -> 'Connector':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Connector.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def outer_component(self) -> '_2415.AbstractShaft':
        """AbstractShaft: 'OuterComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_connection(self) -> '_2253.Connection':
        """Connection: 'OuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_socket(self) -> '_2257.CylindricalSocket':
        """CylindricalSocket: 'OuterSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def house_in(self, shaft: '_2415.AbstractShaft', offset: Optional['float'] = float('nan')) -> '_2253.Connection':
        """ 'HouseIn' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.connections_and_sockets.Connection
        """

        offset = float(offset)
        method_result = self.wrapped.HouseIn(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def other_component(self, component: '_2424.Component') -> '_2415.AbstractShaft':
        """ 'OtherComponent' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.part_model.AbstractShaft
        """

        method_result = self.wrapped.OtherComponent(component.wrapped if component else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def try_house_in(self, shaft: '_2415.AbstractShaft', offset: Optional['float'] = float('nan')) -> '_2425.ComponentsConnectedResult':
        """ 'TryHouseIn' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        offset = float(offset)
        method_result = self.wrapped.TryHouseIn(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'Connector._Cast_Connector':
        return self._Cast_Connector(self)
