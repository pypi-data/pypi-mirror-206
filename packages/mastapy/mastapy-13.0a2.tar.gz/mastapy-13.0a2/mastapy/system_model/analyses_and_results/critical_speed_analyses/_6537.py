"""_6537.py

ConceptGearCriticalSpeedAnalysis
"""
from mastapy.system_model.part_model.gears import _2500
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6805
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6568
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'ConceptGearCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearCriticalSpeedAnalysis',)


class ConceptGearCriticalSpeedAnalysis(_6568.GearCriticalSpeedAnalysis):
    """ConceptGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_CRITICAL_SPEED_ANALYSIS

    class _Cast_ConceptGearCriticalSpeedAnalysis:
        """Special nested class for casting ConceptGearCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'ConceptGearCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def gear_critical_speed_analysis(self):
            return self._parent._cast(_6568.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6587
            
            return self._parent._cast(_6587.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6533
            
            return self._parent._cast(_6533.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6589
            
            return self._parent._cast(_6589.PartCriticalSpeedAnalysis)

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
        def concept_gear_critical_speed_analysis(self) -> 'ConceptGearCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2500.ConceptGear':
        """ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6805.ConceptGearLoadCase':
        """ConceptGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConceptGearCriticalSpeedAnalysis._Cast_ConceptGearCriticalSpeedAnalysis':
        return self._Cast_ConceptGearCriticalSpeedAnalysis(self)
