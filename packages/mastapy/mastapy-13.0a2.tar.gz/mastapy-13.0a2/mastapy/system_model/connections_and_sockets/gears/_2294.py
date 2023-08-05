"""_2294.py

GearMesh
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.gears.gear_designs import _944
from mastapy.system_model.connections_and_sockets import _2262
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'GearMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMesh',)


class GearMesh(_2262.InterMountableComponentConnection):
    """GearMesh

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH

    class _Cast_GearMesh:
        """Special nested class for casting GearMesh to subclasses."""

        def __init__(self, parent: 'GearMesh'):
            self._parent = parent

        @property
        def inter_mountable_component_connection(self):
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
        def gear_mesh(self) -> 'GearMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_efficiency(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MeshEfficiency' is the original name of this property."""

        temp = self.wrapped.MeshEfficiency

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @mesh_efficiency.setter
    def mesh_efficiency(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MeshEfficiency = value

    @property
    def use_specified_mesh_stiffness(self) -> 'bool':
        """bool: 'UseSpecifiedMeshStiffness' is the original name of this property."""

        temp = self.wrapped.UseSpecifiedMeshStiffness

        if temp is None:
            return False

        return temp

    @use_specified_mesh_stiffness.setter
    def use_specified_mesh_stiffness(self, value: 'bool'):
        self.wrapped.UseSpecifiedMeshStiffness = bool(value) if value else False

    @property
    def user_specified_mesh_stiffness(self) -> 'float':
        """float: 'UserSpecifiedMeshStiffness' is the original name of this property."""

        temp = self.wrapped.UserSpecifiedMeshStiffness

        if temp is None:
            return 0.0

        return temp

    @user_specified_mesh_stiffness.setter
    def user_specified_mesh_stiffness(self, value: 'float'):
        self.wrapped.UserSpecifiedMeshStiffness = float(value) if value else 0.0

    @property
    def active_gear_mesh_design(self) -> '_944.GearMeshDesign':
        """GearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearMesh._Cast_GearMesh':
        return self._Cast_GearMesh(self)
