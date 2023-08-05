"""_2402.py

GearWithDuplicatedMeshesFELink
"""
from mastapy.system_model.fe.links import _2407
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_WITH_DUPLICATED_MESHES_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'GearWithDuplicatedMeshesFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('GearWithDuplicatedMeshesFELink',)


class GearWithDuplicatedMeshesFELink(_2407.PlanetBasedFELink):
    """GearWithDuplicatedMeshesFELink

    This is a mastapy class.
    """

    TYPE = _GEAR_WITH_DUPLICATED_MESHES_FE_LINK

    class _Cast_GearWithDuplicatedMeshesFELink:
        """Special nested class for casting GearWithDuplicatedMeshesFELink to subclasses."""

        def __init__(self, parent: 'GearWithDuplicatedMeshesFELink'):
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
        def gear_with_duplicated_meshes_fe_link(self) -> 'GearWithDuplicatedMeshesFELink':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearWithDuplicatedMeshesFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearWithDuplicatedMeshesFELink._Cast_GearWithDuplicatedMeshesFELink':
        return self._Cast_GearWithDuplicatedMeshesFELink(self)
