"""_197.py

NodeGroup
"""
from mastapy.nodal_analysis.dev_tools_analyses import _180
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODE_GROUP = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'NodeGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('NodeGroup',)


class NodeGroup(_180.FEEntityGroupInt):
    """NodeGroup

    This is a mastapy class.
    """

    TYPE = _NODE_GROUP

    class _Cast_NodeGroup:
        """Special nested class for casting NodeGroup to subclasses."""

        def __init__(self, parent: 'NodeGroup'):
            self._parent = parent

        @property
        def fe_entity_group_int(self):
            return self._parent._cast(_180.FEEntityGroupInt)

        @property
        def fe_entity_group(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _179
            
            return self._parent._cast(_179.FEEntityGroup)

        @property
        def cms_node_group(self):
            from mastapy.nodal_analysis.component_mode_synthesis import _224
            
            return self._parent._cast(_224.CMSNodeGroup)

        @property
        def node_group(self) -> 'NodeGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NodeGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'NodeGroup._Cast_NodeGroup':
        return self._Cast_NodeGroup(self)
