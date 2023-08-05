"""_6397.py

CoaxialConnectionCompoundDynamicAnalysis
"""
from typing import List

from mastapy.system_model.connections_and_sockets import _2250
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6267
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6470
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'CoaxialConnectionCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionCompoundDynamicAnalysis',)


class CoaxialConnectionCompoundDynamicAnalysis(_6470.ShaftToMountableComponentConnectionCompoundDynamicAnalysis):
    """CoaxialConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_CoaxialConnectionCompoundDynamicAnalysis:
        """Special nested class for casting CoaxialConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'CoaxialConnectionCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(self):
            return self._parent._cast(_6470.ShaftToMountableComponentConnectionCompoundDynamicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6376
            
            return self._parent._cast(_6376.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis)

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
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6417
            
            return self._parent._cast(_6417.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis)

        @property
        def coaxial_connection_compound_dynamic_analysis(self) -> 'CoaxialConnectionCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2250.CoaxialConnection':
        """CoaxialConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2250.CoaxialConnection':
        """CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6267.CoaxialConnectionDynamicAnalysis]':
        """List[CoaxialConnectionDynamicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6267.CoaxialConnectionDynamicAnalysis]':
        """List[CoaxialConnectionDynamicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CoaxialConnectionCompoundDynamicAnalysis._Cast_CoaxialConnectionCompoundDynamicAnalysis':
        return self._Cast_CoaxialConnectionCompoundDynamicAnalysis(self)
