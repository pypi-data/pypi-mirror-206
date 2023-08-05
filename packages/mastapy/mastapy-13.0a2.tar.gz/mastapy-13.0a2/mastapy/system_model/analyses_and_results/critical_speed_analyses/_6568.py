"""_6568.py

GearCriticalSpeedAnalysis
"""
from mastapy.system_model.part_model.gears import _2509
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6587
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'GearCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCriticalSpeedAnalysis',)


class GearCriticalSpeedAnalysis(_6587.MountableComponentCriticalSpeedAnalysis):
    """GearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_CRITICAL_SPEED_ANALYSIS

    class _Cast_GearCriticalSpeedAnalysis:
        """Special nested class for casting GearCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'GearCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(self):
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
        def agma_gleason_conical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6512
            
            return self._parent._cast(_6512.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6519
            
            return self._parent._cast(_6519.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6522
            
            return self._parent._cast(_6522.BevelDifferentialPlanetGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6523
            
            return self._parent._cast(_6523.BevelDifferentialSunGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6524
            
            return self._parent._cast(_6524.BevelGearCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6537
            
            return self._parent._cast(_6537.ConceptGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6540
            
            return self._parent._cast(_6540.ConicalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6557
            
            return self._parent._cast(_6557.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6560
            
            return self._parent._cast(_6560.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6563
            
            return self._parent._cast(_6563.FaceGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6572
            
            return self._parent._cast(_6572.HypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6576
            
            return self._parent._cast(_6576.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6579
            
            return self._parent._cast(_6579.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6582
            
            return self._parent._cast(_6582.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6609
            
            return self._parent._cast(_6609.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6615
            
            return self._parent._cast(_6615.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6618
            
            return self._parent._cast(_6618.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6621
            
            return self._parent._cast(_6621.StraightBevelPlanetGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6622
            
            return self._parent._cast(_6622.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6633
            
            return self._parent._cast(_6633.WormGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6636
            
            return self._parent._cast(_6636.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(self) -> 'GearCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2509.Gear':
        """Gear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis':
        return self._Cast_GearCriticalSpeedAnalysis(self)
