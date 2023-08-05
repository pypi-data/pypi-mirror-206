"""_49.py

AnalysisSettingsDatabase
"""
from mastapy.utility.databases import _1815
from mastapy.nodal_analysis import _50
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.NodalAnalysis', 'AnalysisSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('AnalysisSettingsDatabase',)


class AnalysisSettingsDatabase(_1815.NamedDatabase['_50.AnalysisSettingsItem']):
    """AnalysisSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_SETTINGS_DATABASE

    class _Cast_AnalysisSettingsDatabase:
        """Special nested class for casting AnalysisSettingsDatabase to subclasses."""

        def __init__(self, parent: 'AnalysisSettingsDatabase'):
            self._parent = parent

        @property
        def named_database(self):
            return self._parent._cast(_1815.NamedDatabase)

        @property
        def sql_database(self):
            from mastapy.utility.databases import _1818, _1817
            
            return self._parent._cast(_1818.SQLDatabase)

        @property
        def database(self):
            from mastapy.utility.databases import _1811, _1817
            
            return self._parent._cast(_1811.Database)

        @property
        def analysis_settings_database(self) -> 'AnalysisSettingsDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AnalysisSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AnalysisSettingsDatabase._Cast_AnalysisSettingsDatabase':
        return self._Cast_AnalysisSettingsDatabase(self)
