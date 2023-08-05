"""_2376.py

IndependentMastaCreatedCondensationNode
"""
from mastapy.nodal_analysis.dev_tools_analyses import _199
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.system_model.fe import _2365
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEPENDENT_MASTA_CREATED_CONDENSATION_NODE = python_net_import('SMT.MastaAPI.SystemModel.FE', 'IndependentMastaCreatedCondensationNode')


__docformat__ = 'restructuredtext en'
__all__ = ('IndependentMastaCreatedCondensationNode',)


class IndependentMastaCreatedCondensationNode(_0.APIBase):
    """IndependentMastaCreatedCondensationNode

    This is a mastapy class.
    """

    TYPE = _INDEPENDENT_MASTA_CREATED_CONDENSATION_NODE

    class _Cast_IndependentMastaCreatedCondensationNode:
        """Special nested class for casting IndependentMastaCreatedCondensationNode to subclasses."""

        def __init__(self, parent: 'IndependentMastaCreatedCondensationNode'):
            self._parent = parent

        @property
        def independent_masta_created_condensation_node(self) -> 'IndependentMastaCreatedCondensationNode':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'IndependentMastaCreatedCondensationNode.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rigid_coupling_type(self) -> '_199.RigidCouplingType':
        """RigidCouplingType: 'RigidCouplingType' is the original name of this property."""

        temp = self.wrapped.RigidCouplingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _199.RigidCouplingType)
        return constructor.new_from_mastapy_type(_199.RigidCouplingType)(value) if value is not None else None

    @rigid_coupling_type.setter
    def rigid_coupling_type(self, value: '_199.RigidCouplingType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _199.RigidCouplingType.type_())
        self.wrapped.RigidCouplingType = value

    @property
    def fe_substructure_node(self) -> '_2365.FESubstructureNode':
        """FESubstructureNode: 'FESubstructureNode' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FESubstructureNode

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def node_position(self) -> 'Vector3D':
        """Vector3D: 'NodePosition' is the original name of this property."""

        temp = self.wrapped.NodePosition

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @node_position.setter
    def node_position(self, value: 'Vector3D'):
        value = value if value else None
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.NodePosition = value

    def delete(self):
        """ 'Delete' is the original name of this method."""

        self.wrapped.Delete()

    @property
    def cast_to(self) -> 'IndependentMastaCreatedCondensationNode._Cast_IndependentMastaCreatedCondensationNode':
        return self._Cast_IndependentMastaCreatedCondensationNode(self)
