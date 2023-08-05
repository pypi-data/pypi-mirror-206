"""_2310.py

WormGearMesh
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.worm import _953
from mastapy.system_model.connections_and_sockets.gears import _2294
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'WormGearMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearMesh',)


class WormGearMesh(_2294.GearMesh):
    """WormGearMesh

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH

    class _Cast_WormGearMesh:
        """Special nested class for casting WormGearMesh to subclasses."""

        def __init__(self, parent: 'WormGearMesh'):
            self._parent = parent

        @property
        def gear_mesh(self):
            return self._parent._cast(_2294.GearMesh)

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
        def worm_gear_mesh(self) -> 'WormGearMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def meshing_angle(self) -> 'float':
        """float: 'MeshingAngle' is the original name of this property."""

        temp = self.wrapped.MeshingAngle

        if temp is None:
            return 0.0

        return temp

    @meshing_angle.setter
    def meshing_angle(self, value: 'float'):
        self.wrapped.MeshingAngle = float(value) if value else 0.0

    @property
    def active_gear_mesh_design(self) -> '_953.WormGearMeshDesign':
        """WormGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_gear_mesh_design(self) -> '_953.WormGearMeshDesign':
        """WormGearMeshDesign: 'WormGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'WormGearMesh._Cast_WormGearMesh':
        return self._Cast_WormGearMesh(self)
