"""_6413.py

CVTBeltConnectionCompoundDynamicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6382
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'CVTBeltConnectionCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTBeltConnectionCompoundDynamicAnalysis',)


class CVTBeltConnectionCompoundDynamicAnalysis(_6382.BeltConnectionCompoundDynamicAnalysis):
    """CVTBeltConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_CVTBeltConnectionCompoundDynamicAnalysis:
        """Special nested class for casting CVTBeltConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'CVTBeltConnectionCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def belt_connection_compound_dynamic_analysis(self):
            return self._parent._cast(_6382.BeltConnectionCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6438
            
            return self._parent._cast(_6438.InterMountableComponentConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6408
            
            return self._parent._cast(_6408.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_dynamic_analysis(self) -> 'CVTBeltConnectionCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTBeltConnectionCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6283.CVTBeltConnectionDynamicAnalysis]':
        """List[CVTBeltConnectionDynamicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6283.CVTBeltConnectionDynamicAnalysis]':
        """List[CVTBeltConnectionDynamicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTBeltConnectionCompoundDynamicAnalysis._Cast_CVTBeltConnectionCompoundDynamicAnalysis':
        return self._Cast_CVTBeltConnectionCompoundDynamicAnalysis(self)
