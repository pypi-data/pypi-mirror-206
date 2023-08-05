"""_222.py

CMSElementFaceGroupOfAllFreeFaces
"""
from mastapy.nodal_analysis.component_mode_synthesis import _221
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CMS_ELEMENT_FACE_GROUP_OF_ALL_FREE_FACES = python_net_import('SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis', 'CMSElementFaceGroupOfAllFreeFaces')


__docformat__ = 'restructuredtext en'
__all__ = ('CMSElementFaceGroupOfAllFreeFaces',)


class CMSElementFaceGroupOfAllFreeFaces(_221.CMSElementFaceGroup):
    """CMSElementFaceGroupOfAllFreeFaces

    This is a mastapy class.
    """

    TYPE = _CMS_ELEMENT_FACE_GROUP_OF_ALL_FREE_FACES

    class _Cast_CMSElementFaceGroupOfAllFreeFaces:
        """Special nested class for casting CMSElementFaceGroupOfAllFreeFaces to subclasses."""

        def __init__(self, parent: 'CMSElementFaceGroupOfAllFreeFaces'):
            self._parent = parent

        @property
        def cms_element_face_group(self):
            return self._parent._cast(_221.CMSElementFaceGroup)

        @property
        def element_face_group(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _177
            
            return self._parent._cast(_177.ElementFaceGroup)

        @property
        def fe_entity_group(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _179
            from mastapy.fe_tools.vis_tools_global import _1227
            
            return self._parent._cast(_179.FEEntityGroup)

        @property
        def cms_element_face_group_of_all_free_faces(self) -> 'CMSElementFaceGroupOfAllFreeFaces':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CMSElementFaceGroupOfAllFreeFaces.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CMSElementFaceGroupOfAllFreeFaces._Cast_CMSElementFaceGroupOfAllFreeFaces':
        return self._Cast_CMSElementFaceGroupOfAllFreeFaces(self)
