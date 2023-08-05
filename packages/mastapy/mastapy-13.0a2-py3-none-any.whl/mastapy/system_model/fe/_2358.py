"""_2358.py

FEEntityGroupWithSelection
"""
from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_ENTITY_GROUP_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE', 'FEEntityGroupWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('FEEntityGroupWithSelection',)


TGroup = TypeVar('TGroup')
TGroupContents = TypeVar('TGroupContents')


class FEEntityGroupWithSelection(_0.APIBase, Generic[TGroup, TGroupContents]):
    """FEEntityGroupWithSelection

    This is a mastapy class.

    Generic Types:
        TGroup
        TGroupContents
    """

    TYPE = _FE_ENTITY_GROUP_WITH_SELECTION

    class _Cast_FEEntityGroupWithSelection:
        """Special nested class for casting FEEntityGroupWithSelection to subclasses."""

        def __init__(self, parent: 'FEEntityGroupWithSelection'):
            self._parent = parent

        @property
        def element_face_group_with_selection(self):
            from mastapy.system_model.fe import _2356
            
            return self._parent._cast(_2356.ElementFaceGroupWithSelection)

        @property
        def node_group_with_selection(self):
            from mastapy.system_model.fe import _2381
            
            return self._parent._cast(_2381.NodeGroupWithSelection)

        @property
        def fe_entity_group_with_selection(self) -> 'FEEntityGroupWithSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEEntityGroupWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def group(self) -> 'TGroup':
        """TGroup: 'Group' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Group

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(TGroup)(temp) if temp is not None else None

    def add_selection_to_group(self):
        """ 'AddSelectionToGroup' is the original name of this method."""

        self.wrapped.AddSelectionToGroup()

    def delete_group(self):
        """ 'DeleteGroup' is the original name of this method."""

        self.wrapped.DeleteGroup()

    def select_items(self):
        """ 'SelectItems' is the original name of this method."""

        self.wrapped.SelectItems()

    @property
    def cast_to(self) -> 'FEEntityGroupWithSelection._Cast_FEEntityGroupWithSelection':
        return self._Cast_FEEntityGroupWithSelection(self)
