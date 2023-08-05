"""_3837.py

RootAssemblyStabilityAnalysis
"""
from mastapy.system_model.part_model import _2454
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _2621, _3749
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'RootAssemblyStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyStabilityAnalysis',)


class RootAssemblyStabilityAnalysis(_3749.AssemblyStabilityAnalysis):
    """RootAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_STABILITY_ANALYSIS

    class _Cast_RootAssemblyStabilityAnalysis:
        """Special nested class for casting RootAssemblyStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'RootAssemblyStabilityAnalysis'):
            self._parent = parent

        @property
        def assembly_stability_analysis(self):
            return self._parent._cast(_3749.AssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3742
            
            return self._parent._cast(_3742.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3822
            
            return self._parent._cast(_3822.PartStabilityAnalysis)

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
        def root_assembly_stability_analysis(self) -> 'RootAssemblyStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyStabilityAnalysis.TYPE'):
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
    def stability_analysis_inputs(self) -> '_2621.StabilityAnalysis':
        """StabilityAnalysis: 'StabilityAnalysisInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StabilityAnalysisInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RootAssemblyStabilityAnalysis._Cast_RootAssemblyStabilityAnalysis':
        return self._Cast_RootAssemblyStabilityAnalysis(self)
