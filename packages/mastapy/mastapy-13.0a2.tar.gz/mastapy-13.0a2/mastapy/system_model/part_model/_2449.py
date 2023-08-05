"""_2449.py

PlanetCarrier
"""
from typing import List, Optional

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2441, _2444
from mastapy.system_model.connections_and_sockets import _2269
from mastapy.system_model.part_model.shaft_model import _2462
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PlanetCarrier')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrier',)


class PlanetCarrier(_2444.MountableComponent):
    """PlanetCarrier

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER

    class _Cast_PlanetCarrier:
        """Special nested class for casting PlanetCarrier to subclasses."""

        def __init__(self, parent: 'PlanetCarrier'):
            self._parent = parent

        @property
        def mountable_component(self):
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
        def planet_carrier(self) -> 'PlanetCarrier':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetCarrier.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def number_of_planetary_sockets(self) -> 'int':
        """int: 'NumberOfPlanetarySockets' is the original name of this property."""

        temp = self.wrapped.NumberOfPlanetarySockets

        if temp is None:
            return 0

        return temp

    @number_of_planetary_sockets.setter
    def number_of_planetary_sockets(self, value: 'int'):
        self.wrapped.NumberOfPlanetarySockets = int(value) if value else 0

    @property
    def load_sharing_settings(self) -> '_2441.LoadSharingSettings':
        """LoadSharingSettings: 'LoadSharingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadSharingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetary_sockets(self) -> 'List[_2269.PlanetarySocket]':
        """List[PlanetarySocket]: 'PlanetarySockets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetarySockets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def attach_carrier_shaft(self, shaft: '_2462.Shaft', offset: Optional['float'] = float('nan')):
        """ 'AttachCarrierShaft' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.shaft_model.Shaft)
            offset (float, optional)
        """

        offset = float(offset)
        self.wrapped.AttachCarrierShaft(shaft.wrapped if shaft else None, offset if offset else 0.0)

    def attach_pin_shaft(self, shaft: '_2462.Shaft', offset: Optional['float'] = float('nan')):
        """ 'AttachPinShaft' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.shaft_model.Shaft)
            offset (float, optional)
        """

        offset = float(offset)
        self.wrapped.AttachPinShaft(shaft.wrapped if shaft else None, offset if offset else 0.0)

    @property
    def cast_to(self) -> 'PlanetCarrier._Cast_PlanetCarrier':
        return self._Cast_PlanetCarrier(self)
