"""_4607.py

FlexiblePinAssemblyModalAnalysis
"""
from mastapy.system_model.part_model import _2434
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6852
from mastapy.system_model.analyses_and_results.system_deflections import _2737
from mastapy.system_model.analyses_and_results.modal_analyses import _4655
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'FlexiblePinAssemblyModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblyModalAnalysis',)


class FlexiblePinAssemblyModalAnalysis(_4655.SpecialisedAssemblyModalAnalysis):
    """FlexiblePinAssemblyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_MODAL_ANALYSIS

    class _Cast_FlexiblePinAssemblyModalAnalysis:
        """Special nested class for casting FlexiblePinAssemblyModalAnalysis to subclasses."""

        def __init__(self, parent: 'FlexiblePinAssemblyModalAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis(self):
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
        def flexible_pin_assembly_modal_analysis(self) -> 'FlexiblePinAssemblyModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblyModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2434.FlexiblePinAssembly':
        """FlexiblePinAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6852.FlexiblePinAssemblyLoadCase':
        """FlexiblePinAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2737.FlexiblePinAssemblySystemDeflection':
        """FlexiblePinAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'FlexiblePinAssemblyModalAnalysis._Cast_FlexiblePinAssemblyModalAnalysis':
        return self._Cast_FlexiblePinAssemblyModalAnalysis(self)
