"""_6604.py

RootAssemblyCriticalSpeedAnalysis
"""
from mastapy.system_model.part_model import _2454
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _2604, _6515
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'RootAssemblyCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCriticalSpeedAnalysis',)


class RootAssemblyCriticalSpeedAnalysis(_6515.AssemblyCriticalSpeedAnalysis):
    """RootAssemblyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_CRITICAL_SPEED_ANALYSIS

    class _Cast_RootAssemblyCriticalSpeedAnalysis:
        """Special nested class for casting RootAssemblyCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'RootAssemblyCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def assembly_critical_speed_analysis(self):
            return self._parent._cast(_6515.AssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6508
            
            return self._parent._cast(_6508.AbstractAssemblyCriticalSpeedAnalysis)

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
        def root_assembly_critical_speed_analysis(self) -> 'RootAssemblyCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def critical_speed_analysis_inputs(self) -> '_2604.CriticalSpeedAnalysis':
        """CriticalSpeedAnalysis: 'CriticalSpeedAnalysisInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalSpeedAnalysisInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RootAssemblyCriticalSpeedAnalysis._Cast_RootAssemblyCriticalSpeedAnalysis':
        return self._Cast_RootAssemblyCriticalSpeedAnalysis(self)
