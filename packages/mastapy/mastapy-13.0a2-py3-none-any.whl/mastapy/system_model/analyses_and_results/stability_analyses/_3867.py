"""_3867.py

VirtualComponentStabilityAnalysis
"""
from mastapy.system_model.part_model import _2459
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3820
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'VirtualComponentStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentStabilityAnalysis',)


class VirtualComponentStabilityAnalysis(_3820.MountableComponentStabilityAnalysis):
    """VirtualComponentStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_STABILITY_ANALYSIS

    class _Cast_VirtualComponentStabilityAnalysis:
        """Special nested class for casting VirtualComponentStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'VirtualComponentStabilityAnalysis'):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(self):
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
        def mass_disc_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3818
            
            return self._parent._cast(_3818.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3819
            
            return self._parent._cast(_3819.MeasurementComponentStabilityAnalysis)

        @property
        def point_load_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3829
            
            return self._parent._cast(_3829.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3830
            
            return self._parent._cast(_3830.PowerLoadStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3866
            
            return self._parent._cast(_3866.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(self) -> 'VirtualComponentStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2459.VirtualComponent':
        """VirtualComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis':
        return self._Cast_VirtualComponentStabilityAnalysis(self)
