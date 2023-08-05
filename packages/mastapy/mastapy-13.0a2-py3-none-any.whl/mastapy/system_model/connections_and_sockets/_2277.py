"""_2277.py

Socket
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2424, _2425
from mastapy.system_model.connections_and_sockets import _2253
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Component')
_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'Socket')


__docformat__ = 'restructuredtext en'
__all__ = ('Socket',)


class Socket(_0.APIBase):
    """Socket

    This is a mastapy class.
    """

    TYPE = _SOCKET

    class _Cast_Socket:
        """Special nested class for casting Socket to subclasses."""

        def __init__(self, parent: 'Socket'):
            self._parent = parent

        @property
        def bearing_inner_socket(self):
            from mastapy.system_model.connections_and_sockets import _2247
            
            return self._parent._cast(_2247.BearingInnerSocket)

        @property
        def bearing_outer_socket(self):
            from mastapy.system_model.connections_and_sockets import _2248
            
            return self._parent._cast(_2248.BearingOuterSocket)

        @property
        def cvt_pulley_socket(self):
            from mastapy.system_model.connections_and_sockets import _2255
            
            return self._parent._cast(_2255.CVTPulleySocket)

        @property
        def cylindrical_socket(self):
            from mastapy.system_model.connections_and_sockets import _2257
            
            return self._parent._cast(_2257.CylindricalSocket)

        @property
        def electric_machine_stator_socket(self):
            from mastapy.system_model.connections_and_sockets import _2259
            
            return self._parent._cast(_2259.ElectricMachineStatorSocket)

        @property
        def inner_shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2260
            
            return self._parent._cast(_2260.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(self):
            from mastapy.system_model.connections_and_sockets import _2261
            
            return self._parent._cast(_2261.InnerShaftSocketBase)

        @property
        def mountable_component_inner_socket(self):
            from mastapy.system_model.connections_and_sockets import _2263
            
            return self._parent._cast(_2263.MountableComponentInnerSocket)

        @property
        def mountable_component_outer_socket(self):
            from mastapy.system_model.connections_and_sockets import _2264
            
            return self._parent._cast(_2264.MountableComponentOuterSocket)

        @property
        def mountable_component_socket(self):
            from mastapy.system_model.connections_and_sockets import _2265
            
            return self._parent._cast(_2265.MountableComponentSocket)

        @property
        def outer_shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2266
            
            return self._parent._cast(_2266.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(self):
            from mastapy.system_model.connections_and_sockets import _2267
            
            return self._parent._cast(_2267.OuterShaftSocketBase)

        @property
        def planetary_socket(self):
            from mastapy.system_model.connections_and_sockets import _2269
            
            return self._parent._cast(_2269.PlanetarySocket)

        @property
        def planetary_socket_base(self):
            from mastapy.system_model.connections_and_sockets import _2270
            
            return self._parent._cast(_2270.PlanetarySocketBase)

        @property
        def pulley_socket(self):
            from mastapy.system_model.connections_and_sockets import _2271
            
            return self._parent._cast(_2271.PulleySocket)

        @property
        def rolling_ring_socket(self):
            from mastapy.system_model.connections_and_sockets import _2274
            
            return self._parent._cast(_2274.RollingRingSocket)

        @property
        def shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2275
            
            return self._parent._cast(_2275.ShaftSocket)

        @property
        def agma_gleason_conical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2281
            
            return self._parent._cast(_2281.AGMAGleasonConicalGearTeethSocket)

        @property
        def bevel_differential_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2283
            
            return self._parent._cast(_2283.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2285
            
            return self._parent._cast(_2285.BevelGearTeethSocket)

        @property
        def concept_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2287
            
            return self._parent._cast(_2287.ConceptGearTeethSocket)

        @property
        def conical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2289
            
            return self._parent._cast(_2289.ConicalGearTeethSocket)

        @property
        def cylindrical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2291
            
            return self._parent._cast(_2291.CylindricalGearTeethSocket)

        @property
        def face_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2293
            
            return self._parent._cast(_2293.FaceGearTeethSocket)

        @property
        def gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2295
            
            return self._parent._cast(_2295.GearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2297
            
            return self._parent._cast(_2297.HypoidGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2298
            
            return self._parent._cast(_2298.KlingelnbergConicalGearTeethSocket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2302
            
            return self._parent._cast(_2302.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2303
            
            return self._parent._cast(_2303.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2305
            
            return self._parent._cast(_2305.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2307
            
            return self._parent._cast(_2307.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2309
            
            return self._parent._cast(_2309.StraightBevelGearTeethSocket)

        @property
        def worm_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2311
            
            return self._parent._cast(_2311.WormGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2313
            
            return self._parent._cast(_2313.ZerolBevelGearTeethSocket)

        @property
        def cycloidal_disc_axial_left_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2314
            
            return self._parent._cast(_2314.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2315
            
            return self._parent._cast(_2315.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2317
            
            return self._parent._cast(_2317.CycloidalDiscInnerSocket)

        @property
        def cycloidal_disc_outer_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2318
            
            return self._parent._cast(_2318.CycloidalDiscOuterSocket)

        @property
        def cycloidal_disc_planetary_bearing_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2320
            
            return self._parent._cast(_2320.CycloidalDiscPlanetaryBearingSocket)

        @property
        def ring_pins_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2321
            
            return self._parent._cast(_2321.RingPinsSocket)

        @property
        def clutch_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2324
            
            return self._parent._cast(_2324.ClutchSocket)

        @property
        def concept_coupling_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2326
            
            return self._parent._cast(_2326.ConceptCouplingSocket)

        @property
        def coupling_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2328
            
            return self._parent._cast(_2328.CouplingSocket)

        @property
        def part_to_part_shear_coupling_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2330
            
            return self._parent._cast(_2330.PartToPartShearCouplingSocket)

        @property
        def spring_damper_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2332
            
            return self._parent._cast(_2332.SpringDamperSocket)

        @property
        def torque_converter_pump_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2334
            
            return self._parent._cast(_2334.TorqueConverterPumpSocket)

        @property
        def torque_converter_turbine_socket(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2335
            
            return self._parent._cast(_2335.TorqueConverterTurbineSocket)

        @property
        def socket(self) -> 'Socket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Socket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def connected_components(self) -> 'List[_2424.Component]':
        """List[Component]: 'ConnectedComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectedComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connections(self) -> 'List[_2253.Connection]':
        """List[Connection]: 'Connections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def owner(self) -> '_2424.Component':
        """Component: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def connect_to(self, component: '_2424.Component') -> '_2425.ComponentsConnectedResult':
        """ 'ConnectTo' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        method_result = self.wrapped.ConnectTo.Overloads[_COMPONENT](component.wrapped if component else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def connect_to_socket(self, socket: 'Socket') -> '_2425.ComponentsConnectedResult':
        """ 'ConnectTo' is the original name of this method.

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        method_result = self.wrapped.ConnectTo.Overloads[_SOCKET](socket.wrapped if socket else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def connection_to(self, socket: 'Socket') -> '_2253.Connection':
        """ 'ConnectionTo' is the original name of this method.

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)

        Returns:
            mastapy.system_model.connections_and_sockets.Connection
        """

        method_result = self.wrapped.ConnectionTo(socket.wrapped if socket else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_possible_sockets_to_connect_to(self, component_to_connect_to: '_2424.Component') -> 'List[Socket]':
        """ 'GetPossibleSocketsToConnectTo' is the original name of this method.

        Args:
            component_to_connect_to (mastapy.system_model.part_model.Component)

        Returns:
            List[mastapy.system_model.connections_and_sockets.Socket]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetPossibleSocketsToConnectTo(component_to_connect_to.wrapped if component_to_connect_to else None))

    @property
    def cast_to(self) -> 'Socket._Cast_Socket':
        return self._Cast_Socket(self)
