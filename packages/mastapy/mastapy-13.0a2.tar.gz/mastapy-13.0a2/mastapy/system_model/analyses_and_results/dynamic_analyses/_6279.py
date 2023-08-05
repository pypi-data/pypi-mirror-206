"""_6279.py

ConnectorDynamicAnalysis
"""
from mastapy.system_model.part_model import _2427
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'ConnectorDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorDynamicAnalysis',)


class ConnectorDynamicAnalysis(_6321.MountableComponentDynamicAnalysis):
    """ConnectorDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_DYNAMIC_ANALYSIS

    class _Cast_ConnectorDynamicAnalysis:
        """Special nested class for casting ConnectorDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectorDynamicAnalysis'):
            self._parent = parent

        @property
        def mountable_component_dynamic_analysis(self):
            return self._parent._cast(_6321.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6268
            
            return self._parent._cast(_6268.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323
            
            return self._parent._cast(_6323.PartDynamicAnalysis)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def bearing_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6251
            
            return self._parent._cast(_6251.BearingDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322
            
            return self._parent._cast(_6322.OilSealDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340
            
            return self._parent._cast(_6340.ShaftHubConnectionDynamicAnalysis)

        @property
        def connector_dynamic_analysis(self) -> 'ConnectorDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectorDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2427.Connector':
        """Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis':
        return self._Cast_ConnectorDynamicAnalysis(self)
