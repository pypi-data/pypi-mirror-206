"""_5481.py

TorqueConverterPumpMultibodyDynamicsAnalysis
"""
from mastapy.system_model.part_model.couplings import _2587
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6938
from mastapy.system_model.analyses_and_results.mbd_analyses import _5388
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'TorqueConverterPumpMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpMultibodyDynamicsAnalysis',)


class TorqueConverterPumpMultibodyDynamicsAnalysis(_5388.CouplingHalfMultibodyDynamicsAnalysis):
    """TorqueConverterPumpMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_TorqueConverterPumpMultibodyDynamicsAnalysis:
        """Special nested class for casting TorqueConverterPumpMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'TorqueConverterPumpMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(self):
            return self._parent._cast(_5388.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435
            
            return self._parent._cast(_5435.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5375
            
            return self._parent._cast(_5375.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437
            
            return self._parent._cast(_5437.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartTimeSeriesLoadAnalysisCase)

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
        def torque_converter_pump_multibody_dynamics_analysis(self) -> 'TorqueConverterPumpMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2587.TorqueConverterPump':
        """TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6938.TorqueConverterPumpLoadCase':
        """TorqueConverterPumpLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'TorqueConverterPumpMultibodyDynamicsAnalysis._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis':
        return self._Cast_TorqueConverterPumpMultibodyDynamicsAnalysis(self)
