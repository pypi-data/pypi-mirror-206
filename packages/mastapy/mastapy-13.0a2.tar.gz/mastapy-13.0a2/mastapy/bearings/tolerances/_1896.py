"""_1896.py

MountingSleeveDiameterDetail
"""
from mastapy.bearings.tolerances import _1893
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTING_SLEEVE_DIAMETER_DETAIL = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'MountingSleeveDiameterDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('MountingSleeveDiameterDetail',)


class MountingSleeveDiameterDetail(_1893.InterferenceDetail):
    """MountingSleeveDiameterDetail

    This is a mastapy class.
    """

    TYPE = _MOUNTING_SLEEVE_DIAMETER_DETAIL

    class _Cast_MountingSleeveDiameterDetail:
        """Special nested class for casting MountingSleeveDiameterDetail to subclasses."""

        def __init__(self, parent: 'MountingSleeveDiameterDetail'):
            self._parent = parent

        @property
        def interference_detail(self):
            return self._parent._cast(_1893.InterferenceDetail)

        @property
        def bearing_connection_component(self):
            from mastapy.bearings.tolerances import _1886
            
            return self._parent._cast(_1886.BearingConnectionComponent)

        @property
        def mounting_sleeve_diameter_detail(self) -> 'MountingSleeveDiameterDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountingSleeveDiameterDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MountingSleeveDiameterDetail._Cast_MountingSleeveDiameterDetail':
        return self._Cast_MountingSleeveDiameterDetail(self)
