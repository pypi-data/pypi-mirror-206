"""_7034.py

GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
"""
from mastapy.system_model.part_model import _2435
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6860
from mastapy.system_model.analyses_and_results.system_deflections import _2741
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6998
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'GuideDxfModelAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelAdvancedTimeSteppingAnalysisForModulation',)


class GuideDxfModelAdvancedTimeSteppingAnalysisForModulation(_6998.ComponentAdvancedTimeSteppingAnalysisForModulation):
    """GuideDxfModelAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting GuideDxfModelAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'GuideDxfModelAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def component_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_6998.ComponentAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7053
            
            return self._parent._cast(_7053.PartAdvancedTimeSteppingAnalysisForModulation)

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
        def guide_dxf_model_advanced_time_stepping_analysis_for_modulation(self) -> 'GuideDxfModelAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GuideDxfModelAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2435.GuideDxfModel':
        """GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6860.GuideDxfModelLoadCase':
        """GuideDxfModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2741.GuideDxfModelSystemDeflection':
        """GuideDxfModelSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GuideDxfModelAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_GuideDxfModelAdvancedTimeSteppingAnalysisForModulation(self)
