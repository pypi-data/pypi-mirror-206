"""_6275.py

ConicalGearDynamicAnalysis
"""
from typing import List

from mastapy.system_model.part_model.gears import _2502
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'ConicalGearDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearDynamicAnalysis',)


class ConicalGearDynamicAnalysis(_6302.GearDynamicAnalysis):
    """ConicalGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_DYNAMIC_ANALYSIS

    class _Cast_ConicalGearDynamicAnalysis:
        """Special nested class for casting ConicalGearDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearDynamicAnalysis'):
            self._parent = parent

        @property
        def gear_dynamic_analysis(self):
            return self._parent._cast(_6302.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321
            
            return self._parent._cast(_6321.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6268
            
            return self._parent._cast(_6268.ComponentDynamicAnalysis)

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
        def agma_gleason_conical_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6247
            
            return self._parent._cast(_6247.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6254
            
            return self._parent._cast(_6254.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6257
            
            return self._parent._cast(_6257.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6258
            
            return self._parent._cast(_6258.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6259
            
            return self._parent._cast(_6259.BevelGearDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306
            
            return self._parent._cast(_6306.HypoidGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310
            
            return self._parent._cast(_6310.KlingelnbergCycloPalloidConicalGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313
            
            return self._parent._cast(_6313.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316
            
            return self._parent._cast(_6316.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343
            
            return self._parent._cast(_6343.SpiralBevelGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349
            
            return self._parent._cast(_6349.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352
            
            return self._parent._cast(_6352.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355
            
            return self._parent._cast(_6355.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356
            
            return self._parent._cast(_6356.StraightBevelSunGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370
            
            return self._parent._cast(_6370.ZerolBevelGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(self) -> 'ConicalGearDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2502.ConicalGear':
        """ConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ConicalGearDynamicAnalysis]':
        """List[ConicalGearDynamicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearDynamicAnalysis._Cast_ConicalGearDynamicAnalysis':
        return self._Cast_ConicalGearDynamicAnalysis(self)
