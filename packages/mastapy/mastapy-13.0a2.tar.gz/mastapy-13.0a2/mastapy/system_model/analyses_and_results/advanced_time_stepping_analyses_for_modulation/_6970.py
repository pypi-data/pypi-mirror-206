"""_6970.py

AbstractShaftAdvancedTimeSteppingAnalysisForModulation
"""
from mastapy.system_model.part_model import _2415
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2666
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6971
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'AbstractShaftAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftAdvancedTimeSteppingAnalysisForModulation',)


class AbstractShaftAdvancedTimeSteppingAnalysisForModulation(_6971.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation):
    """AbstractShaftAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AbstractShaftAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'AbstractShaftAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_6971.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def component_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6998
            
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
        def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7017
            
            return self._parent._cast(_7017.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation)

        @property
        def shaft_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7069
            
            return self._parent._cast(_7069.ShaftAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_advanced_time_stepping_analysis_for_modulation(self) -> 'AbstractShaftAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2415.AbstractShaft':
        """AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2666.AbstractShaftSystemDeflection':
        """AbstractShaftSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_AbstractShaftAdvancedTimeSteppingAnalysisForModulation(self)
