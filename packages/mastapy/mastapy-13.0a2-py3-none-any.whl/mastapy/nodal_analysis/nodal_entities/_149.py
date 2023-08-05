"""_149.py

TorsionalFrictionNodePairSimpleLockedStiffness
"""
from mastapy.nodal_analysis.nodal_entities import _148
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORSIONAL_FRICTION_NODE_PAIR_SIMPLE_LOCKED_STIFFNESS = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'TorsionalFrictionNodePairSimpleLockedStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('TorsionalFrictionNodePairSimpleLockedStiffness',)


class TorsionalFrictionNodePairSimpleLockedStiffness(_148.TorsionalFrictionNodePair):
    """TorsionalFrictionNodePairSimpleLockedStiffness

    This is a mastapy class.
    """

    TYPE = _TORSIONAL_FRICTION_NODE_PAIR_SIMPLE_LOCKED_STIFFNESS

    class _Cast_TorsionalFrictionNodePairSimpleLockedStiffness:
        """Special nested class for casting TorsionalFrictionNodePairSimpleLockedStiffness to subclasses."""

        def __init__(self, parent: 'TorsionalFrictionNodePairSimpleLockedStiffness'):
            self._parent = parent

        @property
        def torsional_friction_node_pair(self):
            return self._parent._cast(_148.TorsionalFrictionNodePair)

        @property
        def concentric_connection_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _133
            
            return self._parent._cast(_133.ConcentricConnectionNodalComponent)

        @property
        def two_body_connection_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _150
            
            return self._parent._cast(_150.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(self):
            from mastapy.nodal_analysis.nodal_entities import _132
            
            return self._parent._cast(_132.ComponentNodalComposite)

        @property
        def nodal_composite(self):
            from mastapy.nodal_analysis.nodal_entities import _142
            
            return self._parent._cast(_142.NodalComposite)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _143
            
            return self._parent._cast(_143.NodalEntity)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(self) -> 'TorsionalFrictionNodePairSimpleLockedStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorsionalFrictionNodePairSimpleLockedStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TorsionalFrictionNodePairSimpleLockedStiffness._Cast_TorsionalFrictionNodePairSimpleLockedStiffness':
        return self._Cast_TorsionalFrictionNodePairSimpleLockedStiffness(self)
