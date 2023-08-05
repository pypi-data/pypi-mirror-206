"""_4676.py

TorqueConverterPumpModalAnalysis
"""
from mastapy.system_model.part_model.couplings import _2587
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6938
from mastapy.system_model.analyses_and_results.system_deflections import _2808
from mastapy.system_model.analyses_and_results.modal_analyses import _4586
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'TorqueConverterPumpModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpModalAnalysis',)


class TorqueConverterPumpModalAnalysis(_4586.CouplingHalfModalAnalysis):
    """TorqueConverterPumpModalAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_MODAL_ANALYSIS

    class _Cast_TorqueConverterPumpModalAnalysis:
        """Special nested class for casting TorqueConverterPumpModalAnalysis to subclasses."""

        def __init__(self, parent: 'TorqueConverterPumpModalAnalysis'):
            self._parent = parent

        @property
        def coupling_half_modal_analysis(self):
            return self._parent._cast(_4586.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631
            
            return self._parent._cast(_4631.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572
            
            return self._parent._cast(_4572.ComponentModalAnalysis)

        @property
        def part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635
            
            return self._parent._cast(_4635.PartModalAnalysis)

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
        def torque_converter_pump_modal_analysis(self) -> 'TorqueConverterPumpModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpModalAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2808.TorqueConverterPumpSystemDeflection':
        """TorqueConverterPumpSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'TorqueConverterPumpModalAnalysis._Cast_TorqueConverterPumpModalAnalysis':
        return self._Cast_TorqueConverterPumpModalAnalysis(self)
