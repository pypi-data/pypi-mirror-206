"""_6246.py

AbstractShaftToMountableComponentConnectionDynamicAnalysis
"""
from mastapy.system_model.connections_and_sockets import _2246
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6278
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'AbstractShaftToMountableComponentConnectionDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionDynamicAnalysis',)


class AbstractShaftToMountableComponentConnectionDynamicAnalysis(_6278.ConnectionDynamicAnalysis):
    """AbstractShaftToMountableComponentConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_DYNAMIC_ANALYSIS

    class _Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionDynamicAnalysis'):
            self._parent = parent

        @property
        def connection_dynamic_analysis(self):
            return self._parent._cast(_6278.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7502
            
            return self._parent._cast(_7502.ConnectionFEAnalysis)

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
        def coaxial_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6267
            
            return self._parent._cast(_6267.CoaxialConnectionDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287
            
            return self._parent._cast(_6287.CycloidalDiscCentralBearingConnectionDynamicAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289
            
            return self._parent._cast(_6289.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis)

        @property
        def planetary_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6327
            
            return self._parent._cast(_6327.PlanetaryConnectionDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341
            
            return self._parent._cast(_6341.ShaftToMountableComponentConnectionDynamicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(self) -> 'AbstractShaftToMountableComponentConnectionDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2246.AbstractShaftToMountableComponentConnection':
        """AbstractShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis':
        return self._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis(self)
