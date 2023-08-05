"""_180.py

FEEntityGroupInt
"""
from mastapy.nodal_analysis.dev_tools_analyses import _179
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_ENTITY_GROUP_INT = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'FEEntityGroupInt')


__docformat__ = 'restructuredtext en'
__all__ = ('FEEntityGroupInt',)


class FEEntityGroupInt(_179.FEEntityGroup[int]):
    """FEEntityGroupInt

    This is a mastapy class.
    """

    TYPE = _FE_ENTITY_GROUP_INT

    class _Cast_FEEntityGroupInt:
        """Special nested class for casting FEEntityGroupInt to subclasses."""

        def __init__(self, parent: 'FEEntityGroupInt'):
            self._parent = parent

        @property
        def fe_entity_group(self):
            return self._parent._cast(_179.FEEntityGroup)

        @property
        def element_group(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _178
            
            return self._parent._cast(_178.ElementGroup)

        @property
        def node_group(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _197
            
            return self._parent._cast(_197.NodeGroup)

        @property
        def cms_node_group(self):
            from mastapy.nodal_analysis.component_mode_synthesis import _224
            
            return self._parent._cast(_224.CMSNodeGroup)

        @property
        def fe_entity_group_int(self) -> 'FEEntityGroupInt':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEEntityGroupInt.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FEEntityGroupInt._Cast_FEEntityGroupInt':
        return self._Cast_FEEntityGroupInt(self)
