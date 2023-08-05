"""_3817.py

KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
"""
from mastapy.system_model.part_model.gears import _2519
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6882
from mastapy.system_model.analyses_and_results.stability_analyses import _3811
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis',)


class KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis(_3811.KlingelnbergCycloPalloidConicalGearStabilityAnalysis):
    """KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_STABILITY_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(self):
            return self._parent._cast(_3811.KlingelnbergCycloPalloidConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3776
            
            return self._parent._cast(_3776.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3803
            
            return self._parent._cast(_3803.GearStabilityAnalysis)

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
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2519.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6882.KlingelnbergCycloPalloidSpiralBevelGearLoadCase':
        """KlingelnbergCycloPalloidSpiralBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis(self)
