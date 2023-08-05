"""_6545.py

CouplingConnectionCriticalSpeedAnalysis
"""
from mastapy.system_model.connections_and_sockets.couplings import _2327
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'CouplingConnectionCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCriticalSpeedAnalysis',)


class CouplingConnectionCriticalSpeedAnalysis(_6575.InterMountableComponentConnectionCriticalSpeedAnalysis):
    """CouplingConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_CRITICAL_SPEED_ANALYSIS

    class _Cast_CouplingConnectionCriticalSpeedAnalysis:
        """Special nested class for casting CouplingConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingConnectionCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_critical_speed_analysis(self):
            return self._parent._cast(_6575.InterMountableComponentConnectionCriticalSpeedAnalysis)

        @property
        def connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6543
            
            return self._parent._cast(_6543.ConnectionCriticalSpeedAnalysis)

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
        def clutch_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6529
            
            return self._parent._cast(_6529.ClutchConnectionCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6534
            
            return self._parent._cast(_6534.ConceptCouplingConnectionCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6590
            
            return self._parent._cast(_6590.PartToPartShearCouplingConnectionCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6612
            
            return self._parent._cast(_6612.SpringDamperConnectionCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6627
            
            return self._parent._cast(_6627.TorqueConverterConnectionCriticalSpeedAnalysis)

        @property
        def coupling_connection_critical_speed_analysis(self) -> 'CouplingConnectionCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2327.CouplingConnection':
        """CouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis':
        return self._Cast_CouplingConnectionCriticalSpeedAnalysis(self)
