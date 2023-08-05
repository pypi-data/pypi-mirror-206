"""_2262.py

InterMountableComponentConnection
"""
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2253
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'InterMountableComponentConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnection',)


class InterMountableComponentConnection(_2253.Connection):
    """InterMountableComponentConnection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION

    class _Cast_InterMountableComponentConnection:
        """Special nested class for casting InterMountableComponentConnection to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnection'):
            self._parent = parent

        @property
        def connection(self):
            return self._parent._cast(_2253.Connection)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def belt_connection(self):
            from mastapy.system_model.connections_and_sockets import _2249
            
            return self._parent._cast(_2249.BeltConnection)

        @property
        def cvt_belt_connection(self):
            from mastapy.system_model.connections_and_sockets import _2254
            
            return self._parent._cast(_2254.CVTBeltConnection)

        @property
        def rolling_ring_connection(self):
            from mastapy.system_model.connections_and_sockets import _2273
            
            return self._parent._cast(_2273.RollingRingConnection)

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
        def inter_mountable_component_connection(self) -> 'InterMountableComponentConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self) -> 'float':
        """float: 'AdditionalModalDampingRatio' is the original name of this property."""

        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return temp

    @additional_modal_damping_ratio.setter
    def additional_modal_damping_ratio(self, value: 'float'):
        self.wrapped.AdditionalModalDampingRatio = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'InterMountableComponentConnection._Cast_InterMountableComponentConnection':
        return self._Cast_InterMountableComponentConnection(self)
