"""_7011.py

CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
"""
from mastapy.system_model.connections_and_sockets.couplings import _2327
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2708
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7039
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'CouplingConnectionAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionAdvancedTimeSteppingAnalysisForModulation',)


class CouplingConnectionAdvancedTimeSteppingAnalysisForModulation(_7039.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation):
    """CouplingConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CouplingConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'CouplingConnectionAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7039.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation)

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
        def clutch_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6995
            
            return self._parent._cast(_6995.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_coupling_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7000
            
            return self._parent._cast(_7000.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_to_part_shear_coupling_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7055
            
            return self._parent._cast(_7055.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spring_damper_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7077
            
            return self._parent._cast(_7077.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7092
            
            return self._parent._cast(_7092.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(self) -> 'CouplingConnectionAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE'):
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
    def system_deflection_results(self) -> '_2708.CouplingConnectionSystemDeflection':
        """CouplingConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_CouplingConnectionAdvancedTimeSteppingAnalysisForModulation(self)
