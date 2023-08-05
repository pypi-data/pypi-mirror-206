"""_1884.py

SKFSettings
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2080
from mastapy.utility import _1583
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SKF_SETTINGS = python_net_import('SMT.MastaAPI.Bearings', 'SKFSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('SKFSettings',)


class SKFSettings(_1583.PerMachineSettings):
    """SKFSettings

    This is a mastapy class.
    """

    TYPE = _SKF_SETTINGS

    class _Cast_SKFSettings:
        """Special nested class for casting SKFSettings to subclasses."""

        def __init__(self, parent: 'SKFSettings'):
            self._parent = parent

        @property
        def per_machine_settings(self):
            return self._parent._cast(_1583.PerMachineSettings)

        @property
        def persistent_singleton(self):
            from mastapy.utility import _1584
            
            return self._parent._cast(_1584.PersistentSingleton)

        @property
        def skf_settings(self) -> 'SKFSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SKFSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def enable_skf_module(self) -> 'bool':
        """bool: 'EnableSKFModule' is the original name of this property."""

        temp = self.wrapped.EnableSKFModule

        if temp is None:
            return False

        return temp

    @enable_skf_module.setter
    def enable_skf_module(self, value: 'bool'):
        self.wrapped.EnableSKFModule = bool(value) if value else False

    @property
    def log_file_path(self) -> 'str':
        """str: 'LogFilePath' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LogFilePath

        if temp is None:
            return ''

        return temp

    @property
    def log_http_requests(self) -> 'bool':
        """bool: 'LogHTTPRequests' is the original name of this property."""

        temp = self.wrapped.LogHTTPRequests

        if temp is None:
            return False

        return temp

    @log_http_requests.setter
    def log_http_requests(self, value: 'bool'):
        self.wrapped.LogHTTPRequests = bool(value) if value else False

    @property
    def skf_authentication(self) -> '_2080.SKFAuthentication':
        """SKFAuthentication: 'SKFAuthentication' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKFAuthentication

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SKFSettings._Cast_SKFSettings':
        return self._Cast_SKFSettings(self)
