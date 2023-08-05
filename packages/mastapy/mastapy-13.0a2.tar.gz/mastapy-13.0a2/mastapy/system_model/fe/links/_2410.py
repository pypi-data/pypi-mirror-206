"""_2410.py

RollingRingConnectionFELink
"""
from mastapy.system_model.fe.links import _2403
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'RollingRingConnectionFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingConnectionFELink',)


class RollingRingConnectionFELink(_2403.MultiAngleConnectionFELink):
    """RollingRingConnectionFELink

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_FE_LINK

    class _Cast_RollingRingConnectionFELink:
        """Special nested class for casting RollingRingConnectionFELink to subclasses."""

        def __init__(self, parent: 'RollingRingConnectionFELink'):
            self._parent = parent

        @property
        def multi_angle_connection_fe_link(self):
            return self._parent._cast(_2403.MultiAngleConnectionFELink)

        @property
        def multi_node_fe_link(self):
            from mastapy.system_model.fe.links import _2405
            
            return self._parent._cast(_2405.MultiNodeFELink)

        @property
        def fe_link(self):
            from mastapy.system_model.fe.links import _2398
            
            return self._parent._cast(_2398.FELink)

        @property
        def rolling_ring_connection_fe_link(self) -> 'RollingRingConnectionFELink':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingRingConnectionFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RollingRingConnectionFELink._Cast_RollingRingConnectionFELink':
        return self._Cast_RollingRingConnectionFELink(self)
