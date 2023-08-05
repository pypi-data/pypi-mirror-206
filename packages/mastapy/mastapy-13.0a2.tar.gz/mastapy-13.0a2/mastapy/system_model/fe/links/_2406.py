"""_2406.py

PlanetaryConnectorMultiNodeFELink
"""
from mastapy.system_model.fe.links import _2407
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTOR_MULTI_NODE_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'PlanetaryConnectorMultiNodeFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryConnectorMultiNodeFELink',)


class PlanetaryConnectorMultiNodeFELink(_2407.PlanetBasedFELink):
    """PlanetaryConnectorMultiNodeFELink

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTOR_MULTI_NODE_FE_LINK

    class _Cast_PlanetaryConnectorMultiNodeFELink:
        """Special nested class for casting PlanetaryConnectorMultiNodeFELink to subclasses."""

        def __init__(self, parent: 'PlanetaryConnectorMultiNodeFELink'):
            self._parent = parent

        @property
        def planet_based_fe_link(self):
            return self._parent._cast(_2407.PlanetBasedFELink)

        @property
        def multi_node_fe_link(self):
            from mastapy.system_model.fe.links import _2405
            
            return self._parent._cast(_2405.MultiNodeFELink)

        @property
        def fe_link(self):
            from mastapy.system_model.fe.links import _2398
            
            return self._parent._cast(_2398.FELink)

        @property
        def planetary_connector_multi_node_fe_link(self) -> 'PlanetaryConnectorMultiNodeFELink':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryConnectorMultiNodeFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PlanetaryConnectorMultiNodeFELink._Cast_PlanetaryConnectorMultiNodeFELink':
        return self._Cast_PlanetaryConnectorMultiNodeFELink(self)
