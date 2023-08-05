"""_6606.py

ShaftHubConnectionCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2577
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6913
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'ShaftHubConnectionCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionCriticalSpeedAnalysis',)


class ShaftHubConnectionCriticalSpeedAnalysis(_6544.ConnectorCriticalSpeedAnalysis):
    """ShaftHubConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_CRITICAL_SPEED_ANALYSIS

    class _Cast_ShaftHubConnectionCriticalSpeedAnalysis:
        """Special nested class for casting ShaftHubConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'ShaftHubConnectionCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def connector_critical_speed_analysis(self):
            return self._parent._cast(_6544.ConnectorCriticalSpeedAnalysis)

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
        def shaft_hub_connection_critical_speed_analysis(self) -> 'ShaftHubConnectionCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2577.ShaftHubConnection':
        """ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6913.ShaftHubConnectionLoadCase':
        """ShaftHubConnectionLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ShaftHubConnectionCriticalSpeedAnalysis]':
        """List[ShaftHubConnectionCriticalSpeedAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftHubConnectionCriticalSpeedAnalysis._Cast_ShaftHubConnectionCriticalSpeedAnalysis':
        return self._Cast_ShaftHubConnectionCriticalSpeedAnalysis(self)
