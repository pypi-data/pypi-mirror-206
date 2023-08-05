"""_48.py

AnalysisSettings
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_SETTINGS = python_net_import('SMT.MastaAPI.NodalAnalysis', 'AnalysisSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('AnalysisSettings',)


class AnalysisSettings(_0.APIBase):
    """AnalysisSettings

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_SETTINGS

    class _Cast_AnalysisSettings:
        """Special nested class for casting AnalysisSettings to subclasses."""

        def __init__(self, parent: 'AnalysisSettings'):
            self._parent = parent

        @property
        def analysis_settings(self) -> 'AnalysisSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AnalysisSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AnalysisSettings._Cast_AnalysisSettings':
        return self._Cast_AnalysisSettings(self)
