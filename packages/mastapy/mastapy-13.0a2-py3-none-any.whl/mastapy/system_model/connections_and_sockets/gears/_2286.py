"""_2286.py

ConceptGearMesh
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.concept import _1171
from mastapy.system_model.connections_and_sockets.gears import _2294
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ConceptGearMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearMesh',)


class ConceptGearMesh(_2294.GearMesh):
    """ConceptGearMesh

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH

    class _Cast_ConceptGearMesh:
        """Special nested class for casting ConceptGearMesh to subclasses."""

        def __init__(self, parent: 'ConceptGearMesh'):
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
        def concept_gear_mesh(self) -> 'ConceptGearMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_drop_angle(self) -> 'float':
        """float: 'PinionDropAngle' is the original name of this property."""

        temp = self.wrapped.PinionDropAngle

        if temp is None:
            return 0.0

        return temp

    @pinion_drop_angle.setter
    def pinion_drop_angle(self, value: 'float'):
        self.wrapped.PinionDropAngle = float(value) if value else 0.0

    @property
    def wheel_drop_angle(self) -> 'float':
        """float: 'WheelDropAngle' is the original name of this property."""

        temp = self.wrapped.WheelDropAngle

        if temp is None:
            return 0.0

        return temp

    @wheel_drop_angle.setter
    def wheel_drop_angle(self, value: 'float'):
        self.wrapped.WheelDropAngle = float(value) if value else 0.0

    @property
    def active_gear_mesh_design(self) -> '_1171.ConceptGearMeshDesign':
        """ConceptGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gear_mesh_design(self) -> '_1171.ConceptGearMeshDesign':
        """ConceptGearMeshDesign: 'ConceptGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConceptGearMesh._Cast_ConceptGearMesh':
        return self._Cast_ConceptGearMesh(self)
