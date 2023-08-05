"""_6280.py

CouplingConnectionDynamicAnalysis
"""
from mastapy.system_model.connections_and_sockets.couplings import _2327
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'CouplingConnectionDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionDynamicAnalysis',)


class CouplingConnectionDynamicAnalysis(_6309.InterMountableComponentConnectionDynamicAnalysis):
    """CouplingConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_DYNAMIC_ANALYSIS

    class _Cast_CouplingConnectionDynamicAnalysis:
        """Special nested class for casting CouplingConnectionDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingConnectionDynamicAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_dynamic_analysis(self):
            return self._parent._cast(_6309.InterMountableComponentConnectionDynamicAnalysis)

        @property
        def connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6278
            
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
        def clutch_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6264
            
            return self._parent._cast(_6264.ClutchConnectionDynamicAnalysis)

        @property
        def concept_coupling_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6269
            
            return self._parent._cast(_6269.ConceptCouplingConnectionDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324
            
            return self._parent._cast(_6324.PartToPartShearCouplingConnectionDynamicAnalysis)

        @property
        def spring_damper_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346
            
            return self._parent._cast(_6346.SpringDamperConnectionDynamicAnalysis)

        @property
        def torque_converter_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361
            
            return self._parent._cast(_6361.TorqueConverterConnectionDynamicAnalysis)

        @property
        def coupling_connection_dynamic_analysis(self) -> 'CouplingConnectionDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionDynamicAnalysis.TYPE'):
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
    def cast_to(self) -> 'CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis':
        return self._Cast_CouplingConnectionDynamicAnalysis(self)
