"""_2411.py

ShaftHubConnectionFELink
"""
from mastapy.system_model.fe.links import _2404
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'ShaftHubConnectionFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionFELink',)


class ShaftHubConnectionFELink(_2404.MultiNodeConnectorFELink):
    """ShaftHubConnectionFELink

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_FE_LINK

    class _Cast_ShaftHubConnectionFELink:
        """Special nested class for casting ShaftHubConnectionFELink to subclasses."""

        def __init__(self, parent: 'ShaftHubConnectionFELink'):
            self._parent = parent

        @property
        def multi_node_connector_fe_link(self):
            return self._parent._cast(_2404.MultiNodeConnectorFELink)

        @property
        def multi_node_fe_link(self):
            from mastapy.system_model.fe.links import _2405
            
            return self._parent._cast(_2405.MultiNodeFELink)

        @property
        def fe_link(self):
            from mastapy.system_model.fe.links import _2398
            
            return self._parent._cast(_2398.FELink)

        @property
        def shaft_hub_connection_fe_link(self) -> 'ShaftHubConnectionFELink':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ShaftHubConnectionFELink._Cast_ShaftHubConnectionFELink':
        return self._Cast_ShaftHubConnectionFELink(self)
