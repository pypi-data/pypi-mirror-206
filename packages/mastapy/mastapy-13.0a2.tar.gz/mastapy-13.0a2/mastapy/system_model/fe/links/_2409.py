"""_2409.py

PointLoadFELink
"""
from mastapy.system_model.fe.links import _2405
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'PointLoadFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadFELink',)


class PointLoadFELink(_2405.MultiNodeFELink):
    """PointLoadFELink

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_FE_LINK

    class _Cast_PointLoadFELink:
        """Special nested class for casting PointLoadFELink to subclasses."""

        def __init__(self, parent: 'PointLoadFELink'):
            self._parent = parent

        @property
        def multi_node_fe_link(self):
            return self._parent._cast(_2405.MultiNodeFELink)

        @property
        def fe_link(self):
            from mastapy.system_model.fe.links import _2398
            
            return self._parent._cast(_2398.FELink)

        @property
        def point_load_fe_link(self) -> 'PointLoadFELink':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PointLoadFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PointLoadFELink._Cast_PointLoadFELink':
        return self._Cast_PointLoadFELink(self)
