"""_6625.py

SynchroniserPartCriticalSpeedAnalysis
"""
from mastapy.system_model.part_model.couplings import _2584
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6547
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'SynchroniserPartCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserPartCriticalSpeedAnalysis',)


class SynchroniserPartCriticalSpeedAnalysis(_6547.CouplingHalfCriticalSpeedAnalysis):
    """SynchroniserPartCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_CRITICAL_SPEED_ANALYSIS

    class _Cast_SynchroniserPartCriticalSpeedAnalysis:
        """Special nested class for casting SynchroniserPartCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'SynchroniserPartCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def coupling_half_critical_speed_analysis(self):
            return self._parent._cast(_6547.CouplingHalfCriticalSpeedAnalysis)

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
        def synchroniser_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6624
            
            return self._parent._cast(_6624.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6626
            
            return self._parent._cast(_6626.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(self) -> 'SynchroniserPartCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserPartCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2584.SynchroniserPart':
        """SynchroniserPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis':
        return self._Cast_SynchroniserPartCriticalSpeedAnalysis(self)
