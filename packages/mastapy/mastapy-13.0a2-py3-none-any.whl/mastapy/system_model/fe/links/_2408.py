"""_2408.py

PlanetCarrierFELink
"""
from mastapy.system_model.fe.links import _2407
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'PlanetCarrierFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierFELink',)


class PlanetCarrierFELink(_2407.PlanetBasedFELink):
    """PlanetCarrierFELink

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_FE_LINK

    class _Cast_PlanetCarrierFELink:
        """Special nested class for casting PlanetCarrierFELink to subclasses."""

        def __init__(self, parent: 'PlanetCarrierFELink'):
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
        def planet_carrier_fe_link(self) -> 'PlanetCarrierFELink':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetCarrierFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PlanetCarrierFELink._Cast_PlanetCarrierFELink':
        return self._Cast_PlanetCarrierFELink(self)
