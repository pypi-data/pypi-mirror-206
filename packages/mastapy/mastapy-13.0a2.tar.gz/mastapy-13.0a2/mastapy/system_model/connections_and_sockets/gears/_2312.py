"""_2312.py

ZerolBevelGearMesh
"""
from mastapy.gears.gear_designs.zerol_bevel import _948
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2284
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ZerolBevelGearMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMesh',)


class ZerolBevelGearMesh(_2284.BevelGearMesh):
    """ZerolBevelGearMesh

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH

    class _Cast_ZerolBevelGearMesh:
        """Special nested class for casting ZerolBevelGearMesh to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearMesh'):
            self._parent = parent

        @property
        def bevel_gear_mesh(self):
            return self._parent._cast(_2284.BevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2280
            
            return self._parent._cast(_2280.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2288
            
            return self._parent._cast(_2288.ConicalGearMesh)

        @property
        def gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2294
            
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
        def zerol_bevel_gear_mesh(self) -> 'ZerolBevelGearMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_mesh_design(self) -> '_948.ZerolBevelGearMeshDesign':
        """ZerolBevelGearMeshDesign: 'BevelGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gear_mesh_design(self) -> '_948.ZerolBevelGearMeshDesign':
        """ZerolBevelGearMeshDesign: 'ZerolBevelGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ZerolBevelGearMesh._Cast_ZerolBevelGearMesh':
        return self._Cast_ZerolBevelGearMesh(self)
