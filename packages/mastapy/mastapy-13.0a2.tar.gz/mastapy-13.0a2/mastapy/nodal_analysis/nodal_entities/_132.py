"""_132.py

ComponentNodalComposite
"""
from mastapy.nodal_analysis.nodal_entities import _142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_NODAL_COMPOSITE = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'ComponentNodalComposite')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentNodalComposite',)


class ComponentNodalComposite(_142.NodalComposite):
    """ComponentNodalComposite

    This is a mastapy class.
    """

    TYPE = _COMPONENT_NODAL_COMPOSITE

    class _Cast_ComponentNodalComposite:
        """Special nested class for casting ComponentNodalComposite to subclasses."""

        def __init__(self, parent: 'ComponentNodalComposite'):
            self._parent = parent

        @property
        def nodal_composite(self):
            return self._parent._cast(_142.NodalComposite)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _143
            
            return self._parent._cast(_143.NodalEntity)

        @property
        def bar_elastic_mbd(self):
            from mastapy.nodal_analysis.nodal_entities import _126
            
            return self._parent._cast(_126.BarElasticMBD)

        @property
        def bar_mbd(self):
            from mastapy.nodal_analysis.nodal_entities import _127
            
            return self._parent._cast(_127.BarMBD)

        @property
        def bar_rigid_mbd(self):
            from mastapy.nodal_analysis.nodal_entities import _128
            
            return self._parent._cast(_128.BarRigidMBD)

        @property
        def concentric_connection_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _133
            
            return self._parent._cast(_133.ConcentricConnectionNodalComponent)

        @property
        def gear_mesh_point_on_flank_contact(self):
            from mastapy.nodal_analysis.nodal_entities import _138
            
            return self._parent._cast(_138.GearMeshPointOnFlankContact)

        @property
        def simple_bar(self):
            from mastapy.nodal_analysis.nodal_entities import _146
            
            return self._parent._cast(_146.SimpleBar)

        @property
        def torsional_friction_node_pair(self):
            from mastapy.nodal_analysis.nodal_entities import _148
            
            return self._parent._cast(_148.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(self):
            from mastapy.nodal_analysis.nodal_entities import _149
            
            return self._parent._cast(_149.TorsionalFrictionNodePairSimpleLockedStiffness)

        @property
        def two_body_connection_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _150
            
            return self._parent._cast(_150.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(self) -> 'ComponentNodalComposite':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentNodalComposite.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ComponentNodalComposite._Cast_ComponentNodalComposite':
        return self._Cast_ComponentNodalComposite(self)
