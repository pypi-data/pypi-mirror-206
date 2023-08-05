"""_7068.py

RootAssemblyAdvancedTimeSteppingAnalysisForModulation
"""
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _2602, _6979
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2454
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5843
from mastapy.system_model.analyses_and_results.system_deflections import _2779
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'RootAssemblyAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyAdvancedTimeSteppingAnalysisForModulation',)


class RootAssemblyAdvancedTimeSteppingAnalysisForModulation(_6979.AssemblyAdvancedTimeSteppingAnalysisForModulation):
    """RootAssemblyAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting RootAssemblyAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'RootAssemblyAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def assembly_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_6979.AssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6969
            
            return self._parent._cast(_6969.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation)

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
        def root_assembly_advanced_time_stepping_analysis_for_modulation(self) -> 'RootAssemblyAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_time_stepping_analysis_for_modulation_inputs(self) -> '_2602.AdvancedTimeSteppingAnalysisForModulation':
        """AdvancedTimeSteppingAnalysisForModulation: 'AdvancedTimeSteppingAnalysisForModulationInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedTimeSteppingAnalysisForModulationInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2454.RootAssembly':
        """RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results(self) -> '_5843.RootAssemblyHarmonicAnalysisResultsPropertyAccessor':
        """RootAssemblyHarmonicAnalysisResultsPropertyAccessor: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2779.RootAssemblySystemDeflection':
        """RootAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RootAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_RootAssemblyAdvancedTimeSteppingAnalysisForModulation(self)
