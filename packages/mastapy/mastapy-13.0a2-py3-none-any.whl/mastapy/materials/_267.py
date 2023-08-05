"""_267.py

MaterialsSettings
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIALS_SETTINGS = python_net_import('SMT.MastaAPI.Materials', 'MaterialsSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('MaterialsSettings',)


class MaterialsSettings(_0.APIBase):
    """MaterialsSettings

    This is a mastapy class.
    """

    TYPE = _MATERIALS_SETTINGS

    class _Cast_MaterialsSettings:
        """Special nested class for casting MaterialsSettings to subclasses."""

        def __init__(self, parent: 'MaterialsSettings'):
            self._parent = parent

        @property
        def materials_settings(self) -> 'MaterialsSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MaterialsSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MaterialsSettings._Cast_MaterialsSettings':
        return self._Cast_MaterialsSettings(self)
