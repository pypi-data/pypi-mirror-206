"""_6552.py

CVTPulleyCriticalSpeedAnalysis
"""
from mastapy.system_model.part_model.couplings import _2566
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6598
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'CVTPulleyCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleyCriticalSpeedAnalysis',)


class CVTPulleyCriticalSpeedAnalysis(_6598.PulleyCriticalSpeedAnalysis):
    """CVTPulleyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_CRITICAL_SPEED_ANALYSIS

    class _Cast_CVTPulleyCriticalSpeedAnalysis:
        """Special nested class for casting CVTPulleyCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'CVTPulleyCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def pulley_critical_speed_analysis(self):
            return self._parent._cast(_6598.PulleyCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6547
            
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
        def cvt_pulley_critical_speed_analysis(self) -> 'CVTPulleyCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTPulleyCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2566.CVTPulley':
        """CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis':
        return self._Cast_CVTPulleyCriticalSpeedAnalysis(self)
