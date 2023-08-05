"""_5394.py

CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
"""
from mastapy.system_model.connections_and_sockets.cycloidal import _2316
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5374
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis',)


class CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis(_5374.CoaxialConnectionMultibodyDynamicsAnalysis):
    """CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def coaxial_connection_multibody_dynamics_analysis(self):
            return self._parent._cast(_5374.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457
            
            return self._parent._cast(_5457.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5350
            
            return self._parent._cast(_5350.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5385
            
            return self._parent._cast(_5385.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7504
            
            return self._parent._cast(_7504.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7500
            
            return self._parent._cast(_7500.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2628
            
            return self._parent._cast(_2628.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(self) -> 'CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2316.CycloidalDiscCentralBearingConnection':
        """CycloidalDiscCentralBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis':
        return self._Cast_CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis(self)
