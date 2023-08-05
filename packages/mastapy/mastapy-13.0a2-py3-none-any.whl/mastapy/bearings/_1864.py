"""_1864.py

BearingSettings
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_SETTINGS = python_net_import('SMT.MastaAPI.Bearings', 'BearingSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingSettings',)


class BearingSettings(_0.APIBase):
    """BearingSettings

    This is a mastapy class.
    """

    TYPE = _BEARING_SETTINGS

    class _Cast_BearingSettings:
        """Special nested class for casting BearingSettings to subclasses."""

        def __init__(self, parent: 'BearingSettings'):
            self._parent = parent

        @property
        def bearing_settings(self) -> 'BearingSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BearingSettings._Cast_BearingSettings':
        return self._Cast_BearingSettings(self)
