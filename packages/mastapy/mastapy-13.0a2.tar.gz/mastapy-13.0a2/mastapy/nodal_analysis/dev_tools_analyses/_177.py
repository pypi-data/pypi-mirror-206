"""_177.py

ElementFaceGroup
"""
from mastapy.nodal_analysis.dev_tools_analyses import _179
from mastapy.fe_tools.vis_tools_global import _1227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_FACE_GROUP = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'ElementFaceGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementFaceGroup',)


class ElementFaceGroup(_179.FEEntityGroup['_1227.ElementFace']):
    """ElementFaceGroup

    This is a mastapy class.
    """

    TYPE = _ELEMENT_FACE_GROUP

    class _Cast_ElementFaceGroup:
        """Special nested class for casting ElementFaceGroup to subclasses."""

        def __init__(self, parent: 'ElementFaceGroup'):
            self._parent = parent

        @property
        def fe_entity_group(self):
            return self._parent._cast(_179.FEEntityGroup)

        @property
        def cms_element_face_group(self):
            from mastapy.nodal_analysis.component_mode_synthesis import _221
            
            return self._parent._cast(_221.CMSElementFaceGroup)

        @property
        def cms_element_face_group_of_all_free_faces(self):
            from mastapy.nodal_analysis.component_mode_synthesis import _222
            
            return self._parent._cast(_222.CMSElementFaceGroupOfAllFreeFaces)

        @property
        def element_face_group(self) -> 'ElementFaceGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementFaceGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElementFaceGroup._Cast_ElementFaceGroup':
        return self._Cast_ElementFaceGroup(self)
