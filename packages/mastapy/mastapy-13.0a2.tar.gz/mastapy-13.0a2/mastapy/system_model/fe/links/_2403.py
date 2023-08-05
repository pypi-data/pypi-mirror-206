"""_2403.py

MultiAngleConnectionFELink
"""
from mastapy.system_model.fe.links import _2405
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_ANGLE_CONNECTION_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'MultiAngleConnectionFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('MultiAngleConnectionFELink',)


class MultiAngleConnectionFELink(_2405.MultiNodeFELink):
    """MultiAngleConnectionFELink

    This is a mastapy class.
    """

    TYPE = _MULTI_ANGLE_CONNECTION_FE_LINK

    class _Cast_MultiAngleConnectionFELink:
        """Special nested class for casting MultiAngleConnectionFELink to subclasses."""

        def __init__(self, parent: 'MultiAngleConnectionFELink'):
            self._parent = parent

        @property
        def multi_node_fe_link(self):
            return self._parent._cast(_2405.MultiNodeFELink)

        @property
        def fe_link(self):
            from mastapy.system_model.fe.links import _2398
            
            return self._parent._cast(_2398.FELink)

        @property
        def gear_mesh_fe_link(self):
            from mastapy.system_model.fe.links import _2401
            
            return self._parent._cast(_2401.GearMeshFELink)

        @property
        def rolling_ring_connection_fe_link(self):
            from mastapy.system_model.fe.links import _2410
            
            return self._parent._cast(_2410.RollingRingConnectionFELink)

        @property
        def multi_angle_connection_fe_link(self) -> 'MultiAngleConnectionFELink':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MultiAngleConnectionFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink':
        return self._Cast_MultiAngleConnectionFELink(self)
