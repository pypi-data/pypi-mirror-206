"""_3859.py

SynchroniserPartStabilityAnalysis
"""
from mastapy.system_model.part_model.couplings import _2584
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3780
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'SynchroniserPartStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserPartStabilityAnalysis',)


class SynchroniserPartStabilityAnalysis(_3780.CouplingHalfStabilityAnalysis):
    """SynchroniserPartStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_STABILITY_ANALYSIS

    class _Cast_SynchroniserPartStabilityAnalysis:
        """Special nested class for casting SynchroniserPartStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'SynchroniserPartStabilityAnalysis'):
            self._parent = parent

        @property
        def coupling_half_stability_analysis(self):
            return self._parent._cast(_3780.CouplingHalfStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3820
            
            return self._parent._cast(_3820.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3767
            
            return self._parent._cast(_3767.ComponentStabilityAnalysis)

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
        def synchroniser_half_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3858
            
            return self._parent._cast(_3858.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3860
            
            return self._parent._cast(_3860.SynchroniserSleeveStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(self) -> 'SynchroniserPartStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserPartStabilityAnalysis.TYPE'):
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
    def cast_to(self) -> 'SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis':
        return self._Cast_SynchroniserPartStabilityAnalysis(self)
