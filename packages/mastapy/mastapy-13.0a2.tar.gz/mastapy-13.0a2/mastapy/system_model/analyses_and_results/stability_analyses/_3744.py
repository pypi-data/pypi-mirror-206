"""_3744.py

AbstractShaftStabilityAnalysis
"""
from mastapy.system_model.part_model import _2415
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3743
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'AbstractShaftStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftStabilityAnalysis',)


class AbstractShaftStabilityAnalysis(_3743.AbstractShaftOrHousingStabilityAnalysis):
    """AbstractShaftStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_STABILITY_ANALYSIS

    class _Cast_AbstractShaftStabilityAnalysis:
        """Special nested class for casting AbstractShaftStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftStabilityAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_stability_analysis(self):
            return self._parent._cast(_3743.AbstractShaftOrHousingStabilityAnalysis)

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
        def cycloidal_disc_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3789
            
            return self._parent._cast(_3789.CycloidalDiscStabilityAnalysis)

        @property
        def shaft_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3839
            
            return self._parent._cast(_3839.ShaftStabilityAnalysis)

        @property
        def abstract_shaft_stability_analysis(self) -> 'AbstractShaftStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2415.AbstractShaft':
        """AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis':
        return self._Cast_AbstractShaftStabilityAnalysis(self)
