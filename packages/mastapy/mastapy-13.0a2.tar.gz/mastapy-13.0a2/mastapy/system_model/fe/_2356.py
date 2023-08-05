"""_2356.py

ElementFaceGroupWithSelection
"""
from mastapy.system_model.fe import _2358
from mastapy.nodal_analysis.component_mode_synthesis import _221
from mastapy.fe_tools.vis_tools_global import _1227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_FACE_GROUP_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE', 'ElementFaceGroupWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementFaceGroupWithSelection',)


class ElementFaceGroupWithSelection(_2358.FEEntityGroupWithSelection['_221.CMSElementFaceGroup', '_1227.ElementFace']):
    """ElementFaceGroupWithSelection

    This is a mastapy class.
    """

    TYPE = _ELEMENT_FACE_GROUP_WITH_SELECTION

    class _Cast_ElementFaceGroupWithSelection:
        """Special nested class for casting ElementFaceGroupWithSelection to subclasses."""

        def __init__(self, parent: 'ElementFaceGroupWithSelection'):
            self._parent = parent

        @property
        def fe_entity_group_with_selection(self):
            return self._parent._cast(_2358.FEEntityGroupWithSelection)

        @property
        def element_face_group_with_selection(self) -> 'ElementFaceGroupWithSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementFaceGroupWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElementFaceGroupWithSelection._Cast_ElementFaceGroupWithSelection':
        return self._Cast_ElementFaceGroupWithSelection(self)
