"""_4675.py

TorqueConverterModalAnalysis
"""
from mastapy.system_model.part_model.couplings import _2586
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6937
from mastapy.system_model.analyses_and_results.system_deflections import _2809
from mastapy.system_model.analyses_and_results.modal_analyses import _4587
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'TorqueConverterModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterModalAnalysis',)


class TorqueConverterModalAnalysis(_4587.CouplingModalAnalysis):
    """TorqueConverterModalAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_MODAL_ANALYSIS

    class _Cast_TorqueConverterModalAnalysis:
        """Special nested class for casting TorqueConverterModalAnalysis to subclasses."""

        def __init__(self, parent: 'TorqueConverterModalAnalysis'):
            self._parent = parent

        @property
        def coupling_modal_analysis(self):
            return self._parent._cast(_4587.CouplingModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655
            
            return self._parent._cast(_4655.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4547
            
            return self._parent._cast(_4547.AbstractAssemblyModalAnalysis)

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
        def torque_converter_modal_analysis(self) -> 'TorqueConverterModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2586.TorqueConverter':
        """TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6937.TorqueConverterLoadCase':
        """TorqueConverterLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2809.TorqueConverterSystemDeflection':
        """TorqueConverterSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'TorqueConverterModalAnalysis._Cast_TorqueConverterModalAnalysis':
        return self._Cast_TorqueConverterModalAnalysis(self)
