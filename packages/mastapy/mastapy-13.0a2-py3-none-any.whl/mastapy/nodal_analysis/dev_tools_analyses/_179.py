"""_179.py

FEEntityGroup
"""
from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_ENTITY_GROUP = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'FEEntityGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('FEEntityGroup',)


T = TypeVar('T')


class FEEntityGroup(_0.APIBase, Generic[T]):
    """FEEntityGroup

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _FE_ENTITY_GROUP

    class _Cast_FEEntityGroup:
        """Special nested class for casting FEEntityGroup to subclasses."""

        def __init__(self, parent: 'FEEntityGroup'):
            self._parent = parent

        @property
        def element_face_group(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _177
            
            return self._parent._cast(_177.ElementFaceGroup)

        @property
        def element_group(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _178
            
            return self._parent._cast(_178.ElementGroup)

        @property
        def fe_entity_group_int(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _180
            
            return self._parent._cast(_180.FEEntityGroupInt)

        @property
        def node_group(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _197
            
            return self._parent._cast(_197.NodeGroup)

        @property
        def cms_element_face_group(self):
            from mastapy.nodal_analysis.component_mode_synthesis import _221
            
            return self._parent._cast(_221.CMSElementFaceGroup)

        @property
        def cms_element_face_group_of_all_free_faces(self):
            from mastapy.nodal_analysis.component_mode_synthesis import _222
            
            return self._parent._cast(_222.CMSElementFaceGroupOfAllFreeFaces)

        @property
        def cms_node_group(self):
            from mastapy.nodal_analysis.component_mode_synthesis import _224
            
            return self._parent._cast(_224.CMSNodeGroup)

        @property
        def fe_entity_group(self) -> 'FEEntityGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEEntityGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def number_of_items(self) -> 'int':
        """int: 'NumberOfItems' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfItems

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self) -> 'FEEntityGroup._Cast_FEEntityGroup':
        return self._Cast_FEEntityGroup(self)
