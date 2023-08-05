"""_133.py

ConcentricConnectionNodalComponent
"""
from mastapy.nodal_analysis.nodal_entities import _150
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCENTRIC_CONNECTION_NODAL_COMPONENT = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'ConcentricConnectionNodalComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('ConcentricConnectionNodalComponent',)


class ConcentricConnectionNodalComponent(_150.TwoBodyConnectionNodalComponent):
    """ConcentricConnectionNodalComponent

    This is a mastapy class.
    """

    TYPE = _CONCENTRIC_CONNECTION_NODAL_COMPONENT

    class _Cast_ConcentricConnectionNodalComponent:
        """Special nested class for casting ConcentricConnectionNodalComponent to subclasses."""

        def __init__(self, parent: 'ConcentricConnectionNodalComponent'):
            self._parent = parent

        @property
        def two_body_connection_nodal_component(self):
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
        def torsional_friction_node_pair(self):
            from mastapy.nodal_analysis.nodal_entities import _148
            
            return self._parent._cast(_148.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(self):
            from mastapy.nodal_analysis.nodal_entities import _149
            
            return self._parent._cast(_149.TorsionalFrictionNodePairSimpleLockedStiffness)

        @property
        def concentric_connection_nodal_component(self) -> 'ConcentricConnectionNodalComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConcentricConnectionNodalComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent':
        return self._Cast_ConcentricConnectionNodalComponent(self)
