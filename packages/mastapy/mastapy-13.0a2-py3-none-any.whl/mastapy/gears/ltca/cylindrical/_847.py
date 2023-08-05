"""_847.py

CylindricalGearBendingStiffnessNode
"""
from mastapy.gears.ltca import _829
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_BENDING_STIFFNESS_NODE = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalGearBendingStiffnessNode')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearBendingStiffnessNode',)


class CylindricalGearBendingStiffnessNode(_829.GearBendingStiffnessNode):
    """CylindricalGearBendingStiffnessNode

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_BENDING_STIFFNESS_NODE

    class _Cast_CylindricalGearBendingStiffnessNode:
        """Special nested class for casting CylindricalGearBendingStiffnessNode to subclasses."""

        def __init__(self, parent: 'CylindricalGearBendingStiffnessNode'):
            self._parent = parent

        @property
        def gear_bending_stiffness_node(self):
            return self._parent._cast(_829.GearBendingStiffnessNode)

        @property
        def gear_stiffness_node(self):
            from mastapy.gears.ltca import _843
            
            return self._parent._cast(_843.GearStiffnessNode)

        @property
        def fe_stiffness_node(self):
            from mastapy.nodal_analysis import _67
            
            return self._parent._cast(_67.FEStiffnessNode)

        @property
        def cylindrical_gear_bending_stiffness_node(self) -> 'CylindricalGearBendingStiffnessNode':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearBendingStiffnessNode.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearBendingStiffnessNode._Cast_CylindricalGearBendingStiffnessNode':
        return self._Cast_CylindricalGearBendingStiffnessNode(self)
