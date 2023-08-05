"""_123.py

NodeVectorState
"""
from mastapy.nodal_analysis.states import _121
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODE_VECTOR_STATE = python_net_import('SMT.MastaAPI.NodalAnalysis.States', 'NodeVectorState')


__docformat__ = 'restructuredtext en'
__all__ = ('NodeVectorState',)


class NodeVectorState(_121.EntityVectorState):
    """NodeVectorState

    This is a mastapy class.
    """

    TYPE = _NODE_VECTOR_STATE

    class _Cast_NodeVectorState:
        """Special nested class for casting NodeVectorState to subclasses."""

        def __init__(self, parent: 'NodeVectorState'):
            self._parent = parent

        @property
        def entity_vector_state(self):
            return self._parent._cast(_121.EntityVectorState)

        @property
        def node_scalar_state(self):
            from mastapy.nodal_analysis.states import _122
            
            return self._parent._cast(_122.NodeScalarState)

        @property
        def node_vector_state(self) -> 'NodeVectorState':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NodeVectorState.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'NodeVectorState._Cast_NodeVectorState':
        return self._Cast_NodeVectorState(self)
