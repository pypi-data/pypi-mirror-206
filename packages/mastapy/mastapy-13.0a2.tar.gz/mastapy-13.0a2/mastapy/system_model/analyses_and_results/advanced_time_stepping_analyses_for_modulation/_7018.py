"""_7018.py

CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation
"""
from mastapy.system_model.connections_and_sockets.cycloidal import _2316
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2715
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6997
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation',)


class CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation(_6997.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation):
    """CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_6997.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7071
            
            return self._parent._cast(_7071.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6972
            
            return self._parent._cast(_6972.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7008
            
            return self._parent._cast(_7008.ConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7503
            
            return self._parent._cast(_7503.ConnectionStaticLoadAnalysisCase)

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
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(self) -> 'CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE'):
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
    def system_deflection_results(self) -> '_2715.CycloidalDiscCentralBearingConnectionSystemDeflection':
        """CycloidalDiscCentralBearingConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation(self)
