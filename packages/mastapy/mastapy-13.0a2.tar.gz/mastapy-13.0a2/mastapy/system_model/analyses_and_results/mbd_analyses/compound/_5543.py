"""_5543.py

CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5394
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5523
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis',)


class CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis(_5523.CoaxialConnectionCompoundMultibodyDynamicsAnalysis):
    """CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5523.CoaxialConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5596
            
            return self._parent._cast(_5596.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5502
            
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
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(self) -> 'CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5394.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis]':
        """List[CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5394.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis]':
        """List[CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis':
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis(self)
