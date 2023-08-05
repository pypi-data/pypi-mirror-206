"""_142.py

NodalComposite
"""
from mastapy.nodal_analysis.nodal_entities import _143
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_COMPOSITE = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'NodalComposite')


__docformat__ = 'restructuredtext en'
__all__ = ('NodalComposite',)


class NodalComposite(_143.NodalEntity):
    """NodalComposite

    This is a mastapy class.
    """

    TYPE = _NODAL_COMPOSITE

    class _Cast_NodalComposite:
        """Special nested class for casting NodalComposite to subclasses."""

        def __init__(self, parent: 'NodalComposite'):
            self._parent = parent

        @property
        def nodal_entity(self):
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
        def component_nodal_composite(self):
            from mastapy.nodal_analysis.nodal_entities import _132
            
            return self._parent._cast(_132.ComponentNodalComposite)

        @property
        def concentric_connection_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _133
            
            return self._parent._cast(_133.ConcentricConnectionNodalComponent)

        @property
        def gear_mesh_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _136
            
            return self._parent._cast(_136.GearMeshNodalComponent)

        @property
        def gear_mesh_point_on_flank_contact(self):
            from mastapy.nodal_analysis.nodal_entities import _138
            
            return self._parent._cast(_138.GearMeshPointOnFlankContact)

        @property
        def gear_mesh_single_flank_contact(self):
            from mastapy.nodal_analysis.nodal_entities import _139
            
            return self._parent._cast(_139.GearMeshSingleFlankContact)

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
        def nodal_composite(self) -> 'NodalComposite':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NodalComposite.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'NodalComposite._Cast_NodalComposite':
        return self._Cast_NodalComposite(self)
