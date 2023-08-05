"""_3877.py

AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3745
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3909
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis',)


class AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis(_3909.ConnectionCompoundStabilityAnalysis):
    """AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def connection_compound_stability_analysis(self):
            return self._parent._cast(_3909.ConnectionCompoundStabilityAnalysis)

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
        def coaxial_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3898
            
            return self._parent._cast(_3898.CoaxialConnectionCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3918
            
            return self._parent._cast(_3918.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3920
            
            return self._parent._cast(_3920.CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis)

        @property
        def planetary_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3957
            
            return self._parent._cast(_3957.PlanetaryConnectionCompoundStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3971
            
            return self._parent._cast(_3971.ShaftToMountableComponentConnectionCompoundStabilityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(self) -> 'AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_3745.AbstractShaftToMountableComponentConnectionStabilityAnalysis]':
        """List[AbstractShaftToMountableComponentConnectionStabilityAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3745.AbstractShaftToMountableComponentConnectionStabilityAnalysis]':
        """List[AbstractShaftToMountableComponentConnectionStabilityAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis':
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis(self)
