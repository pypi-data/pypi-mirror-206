"""_4602.py

ExternalCADModelModalAnalysis
"""
from mastapy.system_model.part_model import _2432
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6847
from mastapy.system_model.analyses_and_results.system_deflections import _2731
from mastapy.system_model.analyses_and_results.modal_analyses import _4572
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ExternalCADModelModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelModalAnalysis',)


class ExternalCADModelModalAnalysis(_4572.ComponentModalAnalysis):
    """ExternalCADModelModalAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_MODAL_ANALYSIS

    class _Cast_ExternalCADModelModalAnalysis:
        """Special nested class for casting ExternalCADModelModalAnalysis to subclasses."""

        def __init__(self, parent: 'ExternalCADModelModalAnalysis'):
            self._parent = parent

        @property
        def component_modal_analysis(self):
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
        def external_cad_model_modal_analysis(self) -> 'ExternalCADModelModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ExternalCADModelModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2432.ExternalCADModel':
        """ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6847.ExternalCADModelLoadCase':
        """ExternalCADModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2731.ExternalCADModelSystemDeflection':
        """ExternalCADModelSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ExternalCADModelModalAnalysis._Cast_ExternalCADModelModalAnalysis':
        return self._Cast_ExternalCADModelModalAnalysis(self)
