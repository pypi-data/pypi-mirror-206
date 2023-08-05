"""_6335.py

RollingRingAssemblyDynamicAnalysis
"""
from mastapy.system_model.part_model.couplings import _2576
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6909
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'RollingRingAssemblyDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingAssemblyDynamicAnalysis',)


class RollingRingAssemblyDynamicAnalysis(_6342.SpecialisedAssemblyDynamicAnalysis):
    """RollingRingAssemblyDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_DYNAMIC_ANALYSIS

    class _Cast_RollingRingAssemblyDynamicAnalysis:
        """Special nested class for casting RollingRingAssemblyDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'RollingRingAssemblyDynamicAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_dynamic_analysis(self):
            return self._parent._cast(_6342.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6243
            
            return self._parent._cast(_6243.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323
            
            return self._parent._cast(_6323.PartDynamicAnalysis)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.PartFEAnalysis)

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
        def rolling_ring_assembly_dynamic_analysis(self) -> 'RollingRingAssemblyDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingRingAssemblyDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2576.RollingRingAssembly':
        """RollingRingAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6909.RollingRingAssemblyLoadCase':
        """RollingRingAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RollingRingAssemblyDynamicAnalysis._Cast_RollingRingAssemblyDynamicAnalysis':
        return self._Cast_RollingRingAssemblyDynamicAnalysis(self)
