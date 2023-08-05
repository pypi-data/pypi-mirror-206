"""_67.py

FEStiffnessNode
"""
from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_STIFFNESS_NODE = python_net_import('SMT.MastaAPI.NodalAnalysis', 'FEStiffnessNode')


__docformat__ = 'restructuredtext en'
__all__ = ('FEStiffnessNode',)


class FEStiffnessNode(_0.APIBase):
    """FEStiffnessNode

    This is a mastapy class.
    """

    TYPE = _FE_STIFFNESS_NODE

    class _Cast_FEStiffnessNode:
        """Special nested class for casting FEStiffnessNode to subclasses."""

        def __init__(self, parent: 'FEStiffnessNode'):
            self._parent = parent

        @property
        def gear_bending_stiffness_node(self):
            from mastapy.gears.ltca import _829
            
            return self._parent._cast(_829.GearBendingStiffnessNode)

        @property
        def gear_contact_stiffness_node(self):
            from mastapy.gears.ltca import _831
            
            return self._parent._cast(_831.GearContactStiffnessNode)

        @property
        def gear_stiffness_node(self):
            from mastapy.gears.ltca import _843
            
            return self._parent._cast(_843.GearStiffnessNode)

        @property
        def cylindrical_gear_bending_stiffness_node(self):
            from mastapy.gears.ltca.cylindrical import _847
            
            return self._parent._cast(_847.CylindricalGearBendingStiffnessNode)

        @property
        def cylindrical_gear_contact_stiffness_node(self):
            from mastapy.gears.ltca.cylindrical import _849
            
            return self._parent._cast(_849.CylindricalGearContactStiffnessNode)

        @property
        def conical_gear_bending_stiffness_node(self):
            from mastapy.gears.ltca.conical import _859
            
            return self._parent._cast(_859.ConicalGearBendingStiffnessNode)

        @property
        def conical_gear_contact_stiffness_node(self):
            from mastapy.gears.ltca.conical import _861
            
            return self._parent._cast(_861.ConicalGearContactStiffnessNode)

        @property
        def fe_substructure_node(self):
            from mastapy.system_model.fe import _2365
            
            return self._parent._cast(_2365.FESubstructureNode)

        @property
        def fe_stiffness_node(self) -> 'FEStiffnessNode':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEStiffnessNode.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_degrees_of_freedom(self) -> 'int':
        """int: 'NumberOfDegreesOfFreedom' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def position_in_local_coordinate_system(self) -> 'Vector3D':
        """Vector3D: 'PositionInLocalCoordinateSystem' is the original name of this property."""

        temp = self.wrapped.PositionInLocalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @position_in_local_coordinate_system.setter
    def position_in_local_coordinate_system(self, value: 'Vector3D'):
        value = value if value else None
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.PositionInLocalCoordinateSystem = value

    @property
    def node_index(self) -> 'int':
        """int: 'NodeIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeIndex

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self) -> 'FEStiffnessNode._Cast_FEStiffnessNode':
        return self._Cast_FEStiffnessNode(self)
