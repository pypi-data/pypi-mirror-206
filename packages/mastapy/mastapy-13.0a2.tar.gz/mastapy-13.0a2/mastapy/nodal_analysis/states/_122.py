"""_122.py

NodeScalarState
"""
from mastapy.nodal_analysis.states import _123
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODE_SCALAR_STATE = python_net_import('SMT.MastaAPI.NodalAnalysis.States', 'NodeScalarState')


__docformat__ = 'restructuredtext en'
__all__ = ('NodeScalarState',)


class NodeScalarState(_123.NodeVectorState):
    """NodeScalarState

    This is a mastapy class.
    """

    TYPE = _NODE_SCALAR_STATE

    class _Cast_NodeScalarState:
        """Special nested class for casting NodeScalarState to subclasses."""

        def __init__(self, parent: 'NodeScalarState'):
            self._parent = parent

        @property
        def node_vector_state(self):
            return self._parent._cast(_123.NodeVectorState)

        @property
        def entity_vector_state(self):
            from mastapy.nodal_analysis.states import _121
            
            return self._parent._cast(_121.EntityVectorState)

        @property
        def node_scalar_state(self) -> 'NodeScalarState':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NodeScalarState.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'NodeScalarState._Cast_NodeScalarState':
        return self._Cast_NodeScalarState(self)
