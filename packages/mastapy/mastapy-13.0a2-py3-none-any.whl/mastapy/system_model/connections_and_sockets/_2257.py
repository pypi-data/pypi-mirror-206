"""_2257.py

CylindricalSocket
"""
from mastapy.system_model.connections_and_sockets import _2277
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'CylindricalSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalSocket',)


class CylindricalSocket(_2277.Socket):
    """CylindricalSocket

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_SOCKET

    class _Cast_CylindricalSocket:
        """Special nested class for casting CylindricalSocket to subclasses."""

        def __init__(self, parent: 'CylindricalSocket'):
            self._parent = parent

        @property
        def socket(self):
            return self._parent._cast(_2277.Socket)

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
        def cylindrical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2291
            
            return self._parent._cast(_2291.CylindricalGearTeethSocket)

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
        def cylindrical_socket(self) -> 'CylindricalSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalSocket._Cast_CylindricalSocket':
        return self._Cast_CylindricalSocket(self)
