"""_5545.py

CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.connections_and_sockets.cycloidal import _2319
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5396
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5502
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis',)


class CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis(_5502.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis):
    """CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5502.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5534
            
            return self._parent._cast(_5534.ConnectionCompoundMultibodyDynamicsAnalysis)

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
        def cycloidal_disc_planetary_bearing_connection_compound_multibody_dynamics_analysis(self) -> 'CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2319.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2319.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5396.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis]':
        """List[CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5396.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis]':
        """List[CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis':
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis(self)
