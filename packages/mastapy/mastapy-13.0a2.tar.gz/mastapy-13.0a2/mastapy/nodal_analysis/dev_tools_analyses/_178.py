"""_178.py

ElementGroup
"""
from mastapy.nodal_analysis.dev_tools_analyses import _180
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_GROUP = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'ElementGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementGroup',)


class ElementGroup(_180.FEEntityGroupInt):
    """ElementGroup

    This is a mastapy class.
    """

    TYPE = _ELEMENT_GROUP

    class _Cast_ElementGroup:
        """Special nested class for casting ElementGroup to subclasses."""

        def __init__(self, parent: 'ElementGroup'):
            self._parent = parent

        @property
        def fe_entity_group_int(self):
            return self._parent._cast(_180.FEEntityGroupInt)

        @property
        def fe_entity_group(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _179
            
            return self._parent._cast(_179.FEEntityGroup)

        @property
        def element_group(self) -> 'ElementGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElementGroup._Cast_ElementGroup':
        return self._Cast_ElementGroup(self)
