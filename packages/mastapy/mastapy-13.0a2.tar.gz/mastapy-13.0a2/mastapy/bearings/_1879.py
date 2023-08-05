"""_1879.py

RollingBearingKey
"""
from mastapy.utility.databases import _1813
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_BEARING_KEY = python_net_import('SMT.MastaAPI.Bearings', 'RollingBearingKey')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingBearingKey',)


class RollingBearingKey(_1813.DatabaseKey):
    """RollingBearingKey

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING_KEY

    class _Cast_RollingBearingKey:
        """Special nested class for casting RollingBearingKey to subclasses."""

        def __init__(self, parent: 'RollingBearingKey'):
            self._parent = parent

        @property
        def database_key(self):
            return self._parent._cast(_1813.DatabaseKey)

        @property
        def rolling_bearing_key(self) -> 'RollingBearingKey':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingBearingKey.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RollingBearingKey._Cast_RollingBearingKey':
        return self._Cast_RollingBearingKey(self)
