"""_2253.py

Connection
"""
from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model import _2424
from mastapy.system_model.connections_and_sockets import _2277
from mastapy._internal.python_net import python_net_import
from mastapy.system_model import _2188
from mastapy._internal.cast_exception import CastException

_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Component')
_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'Socket')
_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'Connection')


__docformat__ = 'restructuredtext en'
__all__ = ('Connection',)


class Connection(_2188.DesignEntity):
    """Connection

    This is a mastapy class.
    """

    TYPE = _CONNECTION

    class _Cast_Connection:
        """Special nested class for casting Connection to subclasses."""

        def __init__(self, parent: 'Connection'):
            self._parent = parent

        @property
        def design_entity(self):
            return self._parent._cast(_2188.DesignEntity)

        @property
        def abstract_shaft_to_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2246
            
            return self._parent._cast(_2246.AbstractShaftToMountableComponentConnection)

        @property
        def belt_connection(self):
            from mastapy.system_model.connections_and_sockets import _2249
            
            return self._parent._cast(_2249.BeltConnection)

        @property
        def coaxial_connection(self):
            from mastapy.system_model.connections_and_sockets import _2250
            
            return self._parent._cast(_2250.CoaxialConnection)

        @property
        def cvt_belt_connection(self):
            from mastapy.system_model.connections_and_sockets import _2254
            
            return self._parent._cast(_2254.CVTBeltConnection)

        @property
        def inter_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2262
            
            return self._parent._cast(_2262.InterMountableComponentConnection)

        @property
        def planetary_connection(self):
            from mastapy.system_model.connections_and_sockets import _2268
            
            return self._parent._cast(_2268.PlanetaryConnection)

        @property
        def rolling_ring_connection(self):
            from mastapy.system_model.connections_and_sockets import _2273
            
            return self._parent._cast(_2273.RollingRingConnection)

        @property
        def shaft_to_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2276
            
            return self._parent._cast(_2276.ShaftToMountableComponentConnection)

        @property
        def agma_gleason_conical_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2280
            
            return self._parent._cast(_2280.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2282
            
            return self._parent._cast(_2282.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2284
            
            return self._parent._cast(_2284.BevelGearMesh)

        @property
        def concept_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2286
            
            return self._parent._cast(_2286.ConceptGearMesh)

        @property
        def conical_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2288
            
            return self._parent._cast(_2288.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2290
            
            return self._parent._cast(_2290.CylindricalGearMesh)

        @property
        def face_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2292
            
            return self._parent._cast(_2292.FaceGearMesh)

        @property
        def gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2294
            
            return self._parent._cast(_2294.GearMesh)

        @property
        def hypoid_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2296
            
            return self._parent._cast(_2296.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2299
            
            return self._parent._cast(_2299.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2300
            
            return self._parent._cast(_2300.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2301
            
            return self._parent._cast(_2301.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2304
            
            return self._parent._cast(_2304.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2306
            
            return self._parent._cast(_2306.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2308
            
            return self._parent._cast(_2308.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2310
            
            return self._parent._cast(_2310.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2312
            
            return self._parent._cast(_2312.ZerolBevelGearMesh)

        @property
        def cycloidal_disc_central_bearing_connection(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2316
            
            return self._parent._cast(_2316.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2319
            
            return self._parent._cast(_2319.CycloidalDiscPlanetaryBearingConnection)

        @property
        def ring_pins_to_disc_connection(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2322
            
            return self._parent._cast(_2322.RingPinsToDiscConnection)

        @property
        def clutch_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2323
            
            return self._parent._cast(_2323.ClutchConnection)

        @property
        def concept_coupling_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2325
            
            return self._parent._cast(_2325.ConceptCouplingConnection)

        @property
        def coupling_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2327
            
            return self._parent._cast(_2327.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2329
            
            return self._parent._cast(_2329.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2331
            
            return self._parent._cast(_2331.SpringDamperConnection)

        @property
        def torque_converter_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2333
            
            return self._parent._cast(_2333.TorqueConverterConnection)

        @property
        def connection(self) -> 'Connection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Connection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_id(self) -> 'str':
        """str: 'ConnectionID' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionID

        if temp is None:
            return ''

        return temp

    @property
    def drawing_position(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'DrawingPosition' is the original name of this property."""

        temp = self.wrapped.DrawingPosition

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @drawing_position.setter
    def drawing_position(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.DrawingPosition = value

    @property
    def speed_ratio_from_a_to_b(self) -> 'float':
        """float: 'SpeedRatioFromAToB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedRatioFromAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ratio_from_a_to_b(self) -> 'float':
        """float: 'TorqueRatioFromAToB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueRatioFromAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def unique_name(self) -> 'str':
        """str: 'UniqueName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UniqueName

        if temp is None:
            return ''

        return temp

    @property
    def owner_a(self) -> '_2424.Component':
        """Component: 'OwnerA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OwnerA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_b(self) -> '_2424.Component':
        """Component: 'OwnerB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OwnerB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a(self) -> '_2277.Socket':
        """Socket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b(self) -> '_2277.Socket':
        """Socket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def other_owner(self, component: '_2424.Component') -> '_2424.Component':
        """ 'OtherOwner' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.part_model.Component
        """

        method_result = self.wrapped.OtherOwner(component.wrapped if component else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def other_socket_for_component(self, component: '_2424.Component') -> '_2277.Socket':
        """ 'OtherSocket' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.connections_and_sockets.Socket
        """

        method_result = self.wrapped.OtherSocket.Overloads[_COMPONENT](component.wrapped if component else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def other_socket(self, socket: '_2277.Socket') -> '_2277.Socket':
        """ 'OtherSocket' is the original name of this method.

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)

        Returns:
            mastapy.system_model.connections_and_sockets.Socket
        """

        method_result = self.wrapped.OtherSocket.Overloads[_SOCKET](socket.wrapped if socket else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def socket_for(self, component: '_2424.Component') -> '_2277.Socket':
        """ 'SocketFor' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.connections_and_sockets.Socket
        """

        method_result = self.wrapped.SocketFor(component.wrapped if component else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'Connection._Cast_Connection':
        return self._Cast_Connection(self)
