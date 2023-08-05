"""_6376.py

AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6246
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6408
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis',)


class AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis(_6408.ConnectionCompoundDynamicAnalysis):
    """AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def connection_compound_dynamic_analysis(self):
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
        def coaxial_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6397
            
            return self._parent._cast(_6397.CoaxialConnectionCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6417
            
            return self._parent._cast(_6417.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6419
            
            return self._parent._cast(_6419.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis)

        @property
        def planetary_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6456
            
            return self._parent._cast(_6456.PlanetaryConnectionCompoundDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6470
            
            return self._parent._cast(_6470.ShaftToMountableComponentConnectionCompoundDynamicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(self) -> 'AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6246.AbstractShaftToMountableComponentConnectionDynamicAnalysis]':
        """List[AbstractShaftToMountableComponentConnectionDynamicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6246.AbstractShaftToMountableComponentConnectionDynamicAnalysis]':
        """List[AbstractShaftToMountableComponentConnectionDynamicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis':
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis(self)
