"""_2400.py

FELinkWithSelection
"""
from mastapy.system_model.fe.links import _2398
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_LINK_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'FELinkWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('FELinkWithSelection',)


class FELinkWithSelection(_0.APIBase):
    """FELinkWithSelection

    This is a mastapy class.
    """

    TYPE = _FE_LINK_WITH_SELECTION

    class _Cast_FELinkWithSelection:
        """Special nested class for casting FELinkWithSelection to subclasses."""

        def __init__(self, parent: 'FELinkWithSelection'):
            self._parent = parent

        @property
        def fe_link_with_selection(self) -> 'FELinkWithSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FELinkWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def link(self) -> '_2398.FELink':
        """FELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def add_selected_nodes(self):
        """ 'AddSelectedNodes' is the original name of this method."""

        self.wrapped.AddSelectedNodes()

    def delete_all_nodes(self):
        """ 'DeleteAllNodes' is the original name of this method."""

        self.wrapped.DeleteAllNodes()

    def select_component(self):
        """ 'SelectComponent' is the original name of this method."""

        self.wrapped.SelectComponent()

    @property
    def cast_to(self) -> 'FELinkWithSelection._Cast_FELinkWithSelection':
        return self._Cast_FELinkWithSelection(self)
