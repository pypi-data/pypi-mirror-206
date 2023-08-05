﻿"""_224.py

CMSNodeGroup
"""
from mastapy._internal import constructor
from mastapy.nodal_analysis.dev_tools_analyses import _197
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CMS_NODE_GROUP = python_net_import('SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis', 'CMSNodeGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('CMSNodeGroup',)


class CMSNodeGroup(_197.NodeGroup):
    """CMSNodeGroup

    This is a mastapy class.
    """

    TYPE = _CMS_NODE_GROUP

    class _Cast_CMSNodeGroup:
        """Special nested class for casting CMSNodeGroup to subclasses."""

        def __init__(self, parent: 'CMSNodeGroup'):
            self._parent = parent

        @property
        def node_group(self):
            return self._parent._cast(_197.NodeGroup)

        @property
        def fe_entity_group_int(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _180
            
            return self._parent._cast(_180.FEEntityGroupInt)

        @property
        def fe_entity_group(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _179
            
            return self._parent._cast(_179.FEEntityGroup)

        @property
        def cms_node_group(self) -> 'CMSNodeGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CMSNodeGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_nvh_results_at_these_nodes(self) -> 'bool':
        """bool: 'ShowNVHResultsAtTheseNodes' is the original name of this property."""

        temp = self.wrapped.ShowNVHResultsAtTheseNodes

        if temp is None:
            return False

        return temp

    @show_nvh_results_at_these_nodes.setter
    def show_nvh_results_at_these_nodes(self, value: 'bool'):
        self.wrapped.ShowNVHResultsAtTheseNodes = bool(value) if value else False

    def create_element_face_group(self):
        """ 'CreateElementFaceGroup' is the original name of this method."""

        self.wrapped.CreateElementFaceGroup()

    @property
    def cast_to(self) -> 'CMSNodeGroup._Cast_CMSNodeGroup':
        return self._Cast_CMSNodeGroup(self)
