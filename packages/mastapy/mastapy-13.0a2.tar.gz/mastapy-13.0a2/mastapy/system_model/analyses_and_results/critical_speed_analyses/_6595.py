"""_6595.py

PlanetCarrierCriticalSpeedAnalysis
"""
from mastapy.system_model.part_model import _2449
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6899
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6587
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'PlanetCarrierCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierCriticalSpeedAnalysis',)


class PlanetCarrierCriticalSpeedAnalysis(_6587.MountableComponentCriticalSpeedAnalysis):
    """PlanetCarrierCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_CRITICAL_SPEED_ANALYSIS

    class _Cast_PlanetCarrierCriticalSpeedAnalysis:
        """Special nested class for casting PlanetCarrierCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'PlanetCarrierCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(self):
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
        def planet_carrier_critical_speed_analysis(self) -> 'PlanetCarrierCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetCarrierCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2449.PlanetCarrier':
        """PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6899.PlanetCarrierLoadCase':
        """PlanetCarrierLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis':
        return self._Cast_PlanetCarrierCriticalSpeedAnalysis(self)
