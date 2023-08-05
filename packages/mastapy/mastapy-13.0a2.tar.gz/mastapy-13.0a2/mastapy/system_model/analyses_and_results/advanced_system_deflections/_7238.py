"""_7238.py

AdvancedSystemDeflectionSubAnalysis
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2804
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'AdvancedSystemDeflectionSubAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AdvancedSystemDeflectionSubAnalysis',)


class AdvancedSystemDeflectionSubAnalysis(_2804.SystemDeflection):
    """AdvancedSystemDeflectionSubAnalysis

    This is a mastapy class.
    """

    TYPE = _ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS

    class _Cast_AdvancedSystemDeflectionSubAnalysis:
        """Special nested class for casting AdvancedSystemDeflectionSubAnalysis to subclasses."""

        def __init__(self, parent: 'AdvancedSystemDeflectionSubAnalysis'):
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
        def advanced_system_deflection_sub_analysis(self) -> 'AdvancedSystemDeflectionSubAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AdvancedSystemDeflectionSubAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_time(self) -> 'float':
        """float: 'CurrentTime' is the original name of this property."""

        temp = self.wrapped.CurrentTime

        if temp is None:
            return 0.0

        return temp

    @current_time.setter
    def current_time(self, value: 'float'):
        self.wrapped.CurrentTime = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis':
        return self._Cast_AdvancedSystemDeflectionSubAnalysis(self)
