"""_2811.py

TorsionalSystemDeflection
"""
from mastapy.system_model.analyses_and_results.system_deflections import _2804
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORSIONAL_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'TorsionalSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('TorsionalSystemDeflection',)


class TorsionalSystemDeflection(_2804.SystemDeflection):
    """TorsionalSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORSIONAL_SYSTEM_DEFLECTION

    class _Cast_TorsionalSystemDeflection:
        """Special nested class for casting TorsionalSystemDeflection to subclasses."""

        def __init__(self, parent: 'TorsionalSystemDeflection'):
            self._parent = parent

        @property
        def system_deflection(self):
            return self._parent._cast(_2804.SystemDeflection)

        @property
        def fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7506
            
            return self._parent._cast(_7506.FEAnalysis)

        @property
        def static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
            return self._parent._cast(_7512.StaticLoadAnalysisCase)

        @property
        def analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7497
            
            return self._parent._cast(_7497.AnalysisCase)

        @property
        def context(self):
            from mastapy.system_model.analyses_and_results import _2629
            
            return self._parent._cast(_2629.Context)

        @property
        def torsional_system_deflection(self) -> 'TorsionalSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorsionalSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TorsionalSystemDeflection._Cast_TorsionalSystemDeflection':
        return self._Cast_TorsionalSystemDeflection(self)
