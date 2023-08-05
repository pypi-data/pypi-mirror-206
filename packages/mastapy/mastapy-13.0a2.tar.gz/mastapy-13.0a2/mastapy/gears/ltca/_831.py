"""_831.py

GearContactStiffnessNode
"""
from mastapy.gears.ltca import _843
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_CONTACT_STIFFNESS_NODE = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearContactStiffnessNode')


__docformat__ = 'restructuredtext en'
__all__ = ('GearContactStiffnessNode',)


class GearContactStiffnessNode(_843.GearStiffnessNode):
    """GearContactStiffnessNode

    This is a mastapy class.
    """

    TYPE = _GEAR_CONTACT_STIFFNESS_NODE

    class _Cast_GearContactStiffnessNode:
        """Special nested class for casting GearContactStiffnessNode to subclasses."""

        def __init__(self, parent: 'GearContactStiffnessNode'):
            self._parent = parent

        @property
        def gear_stiffness_node(self):
            return self._parent._cast(_843.GearStiffnessNode)

        @property
        def fe_stiffness_node(self):
            from mastapy.nodal_analysis import _67
            
            return self._parent._cast(_67.FEStiffnessNode)

        @property
        def cylindrical_gear_contact_stiffness_node(self):
            from mastapy.gears.ltca.cylindrical import _849
            
            return self._parent._cast(_849.CylindricalGearContactStiffnessNode)

        @property
        def conical_gear_contact_stiffness_node(self):
            from mastapy.gears.ltca.conical import _861
            
            return self._parent._cast(_861.ConicalGearContactStiffnessNode)

        @property
        def gear_contact_stiffness_node(self) -> 'GearContactStiffnessNode':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearContactStiffnessNode.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearContactStiffnessNode._Cast_GearContactStiffnessNode':
        return self._Cast_GearContactStiffnessNode(self)
