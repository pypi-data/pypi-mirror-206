"""_38.py

ShaftSettings
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SETTINGS = python_net_import('SMT.MastaAPI.Shafts', 'ShaftSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftSettings',)


class ShaftSettings(_0.APIBase):
    """ShaftSettings

    This is a mastapy class.
    """

    TYPE = _SHAFT_SETTINGS

    class _Cast_ShaftSettings:
        """Special nested class for casting ShaftSettings to subclasses."""

        def __init__(self, parent: 'ShaftSettings'):
            self._parent = parent

        @property
        def shaft_settings(self) -> 'ShaftSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ShaftSettings._Cast_ShaftSettings':
        return self._Cast_ShaftSettings(self)
