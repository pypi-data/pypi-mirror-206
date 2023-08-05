"""_2370.py

FESubstructureWithSelection
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.fe import (
    _2363, _2356, _2381, _2341
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE', 'FESubstructureWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('FESubstructureWithSelection',)


class FESubstructureWithSelection(_2341.BaseFEWithSelection):
    """FESubstructureWithSelection

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_WITH_SELECTION

    class _Cast_FESubstructureWithSelection:
        """Special nested class for casting FESubstructureWithSelection to subclasses."""

        def __init__(self, parent: 'FESubstructureWithSelection'):
            self._parent = parent

        @property
        def base_fe_with_selection(self):
            return self._parent._cast(_2341.BaseFEWithSelection)

        @property
        def fe_substructure_with_selection_components(self):
            from mastapy.system_model.fe import _2371
            
            return self._parent._cast(_2371.FESubstructureWithSelectionComponents)

        @property
        def fe_substructure_with_selection_for_harmonic_analysis(self):
            from mastapy.system_model.fe import _2372
            
            return self._parent._cast(_2372.FESubstructureWithSelectionForHarmonicAnalysis)

        @property
        def fe_substructure_with_selection_for_modal_analysis(self):
            from mastapy.system_model.fe import _2373
            
            return self._parent._cast(_2373.FESubstructureWithSelectionForModalAnalysis)

        @property
        def fe_substructure_with_selection_for_static_analysis(self):
            from mastapy.system_model.fe import _2374
            
            return self._parent._cast(_2374.FESubstructureWithSelectionForStaticAnalysis)

        @property
        def fe_substructure_with_selection(self) -> 'FESubstructureWithSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FESubstructureWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def selected_nodes(self) -> 'str':
        """str: 'SelectedNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedNodes

        if temp is None:
            return ''

        return temp

    @property
    def fe_substructure(self) -> '_2363.FESubstructure':
        """FESubstructure: 'FESubstructure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FESubstructure

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def element_face_groups(self) -> 'List[_2356.ElementFaceGroupWithSelection]':
        """List[ElementFaceGroupWithSelection]: 'ElementFaceGroups' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementFaceGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def node_groups(self) -> 'List[_2381.NodeGroupWithSelection]':
        """List[NodeGroupWithSelection]: 'NodeGroups' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def create_condensation_node_connected_to_current_selection(self):
        """ 'CreateCondensationNodeConnectedToCurrentSelection' is the original name of this method."""

        self.wrapped.CreateCondensationNodeConnectedToCurrentSelection()

    def create_element_face_group(self):
        """ 'CreateElementFaceGroup' is the original name of this method."""

        self.wrapped.CreateElementFaceGroup()

    def create_node_group(self):
        """ 'CreateNodeGroup' is the original name of this method."""

        self.wrapped.CreateNodeGroup()

    def ground_selected_faces(self):
        """ 'GroundSelectedFaces' is the original name of this method."""

        self.wrapped.GroundSelectedFaces()

    def remove_grounding_on_selected_faces(self):
        """ 'RemoveGroundingOnSelectedFaces' is the original name of this method."""

        self.wrapped.RemoveGroundingOnSelectedFaces()

    @property
    def cast_to(self) -> 'FESubstructureWithSelection._Cast_FESubstructureWithSelection':
        return self._Cast_FESubstructureWithSelection(self)
