"""_2401.py

GearMeshFELink
"""
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.fe import _2365
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.fe.links import _2403
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'GearMeshFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshFELink',)


class GearMeshFELink(_2403.MultiAngleConnectionFELink):
    """GearMeshFELink

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_FE_LINK

    class _Cast_GearMeshFELink:
        """Special nested class for casting GearMeshFELink to subclasses."""

        def __init__(self, parent: 'GearMeshFELink'):
            self._parent = parent

        @property
        def multi_angle_connection_fe_link(self):
            return self._parent._cast(_2403.MultiAngleConnectionFELink)

        @property
        def multi_node_fe_link(self):
            from mastapy.system_model.fe.links import _2405
            
            return self._parent._cast(_2405.MultiNodeFELink)

        @property
        def fe_link(self):
            from mastapy.system_model.fe.links import _2398
            
            return self._parent._cast(_2398.FELink)

        @property
        def gear_mesh_fe_link(self) -> 'GearMeshFELink':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def reference_fe_substructure_node_for_misalignments(self) -> 'list_with_selected_item.ListWithSelectedItem_FESubstructureNode':
        """list_with_selected_item.ListWithSelectedItem_FESubstructureNode: 'ReferenceFESubstructureNodeForMisalignments' is the original name of this property."""

        temp = self.wrapped.ReferenceFESubstructureNodeForMisalignments

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_FESubstructureNode)(temp) if temp is not None else None

    @reference_fe_substructure_node_for_misalignments.setter
    def reference_fe_substructure_node_for_misalignments(self, value: 'list_with_selected_item.ListWithSelectedItem_FESubstructureNode.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_FESubstructureNode.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_FESubstructureNode.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.ReferenceFESubstructureNodeForMisalignments = value

    @property
    def use_active_mesh_node_for_reference_fe_substructure_node_for_misalignments(self) -> 'bool':
        """bool: 'UseActiveMeshNodeForReferenceFESubstructureNodeForMisalignments' is the original name of this property."""

        temp = self.wrapped.UseActiveMeshNodeForReferenceFESubstructureNodeForMisalignments

        if temp is None:
            return False

        return temp

    @use_active_mesh_node_for_reference_fe_substructure_node_for_misalignments.setter
    def use_active_mesh_node_for_reference_fe_substructure_node_for_misalignments(self, value: 'bool'):
        self.wrapped.UseActiveMeshNodeForReferenceFESubstructureNodeForMisalignments = bool(value) if value else False

    @property
    def cast_to(self) -> 'GearMeshFELink._Cast_GearMeshFELink':
        return self._Cast_GearMeshFELink(self)
