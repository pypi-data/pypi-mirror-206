"""_2404.py

MultiNodeConnectorFELink
"""
from mastapy.system_model.fe.links import _2405
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_NODE_CONNECTOR_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'MultiNodeConnectorFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('MultiNodeConnectorFELink',)


class MultiNodeConnectorFELink(_2405.MultiNodeFELink):
    """MultiNodeConnectorFELink

    This is a mastapy class.
    """

    TYPE = _MULTI_NODE_CONNECTOR_FE_LINK

    class _Cast_MultiNodeConnectorFELink:
        """Special nested class for casting MultiNodeConnectorFELink to subclasses."""

        def __init__(self, parent: 'MultiNodeConnectorFELink'):
            self._parent = parent

        @property
        def multi_node_fe_link(self):
            return self._parent._cast(_2405.MultiNodeFELink)

        @property
        def fe_link(self):
            from mastapy.system_model.fe.links import _2398
            
            return self._parent._cast(_2398.FELink)

        @property
        def shaft_hub_connection_fe_link(self):
            from mastapy.system_model.fe.links import _2411
            
            return self._parent._cast(_2411.ShaftHubConnectionFELink)

        @property
        def multi_node_connector_fe_link(self) -> 'MultiNodeConnectorFELink':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MultiNodeConnectorFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MultiNodeConnectorFELink._Cast_MultiNodeConnectorFELink':
        return self._Cast_MultiNodeConnectorFELink(self)
