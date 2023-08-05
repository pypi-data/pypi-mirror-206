"""_3023.py

GearSteadyStateSynchronousResponse
"""
from mastapy.system_model.part_model.gears import _2509
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3040
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'GearSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSteadyStateSynchronousResponse',)


class GearSteadyStateSynchronousResponse(_3040.MountableComponentSteadyStateSynchronousResponse):
    """GearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_GearSteadyStateSynchronousResponse:
        """Special nested class for casting GearSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'GearSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response(self):
            return self._parent._cast(_3040.MountableComponentSteadyStateSynchronousResponse)

        @property
        def component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2987
            
            return self._parent._cast(_2987.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3042
            
            return self._parent._cast(_3042.PartSteadyStateSynchronousResponse)

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
        def agma_gleason_conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2968
            
            return self._parent._cast(_2968.AGMAGleasonConicalGearSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2975
            
            return self._parent._cast(_2975.BevelDifferentialGearSteadyStateSynchronousResponse)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2976
            
            return self._parent._cast(_2976.BevelDifferentialPlanetGearSteadyStateSynchronousResponse)

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2977
            
            return self._parent._cast(_2977.BevelDifferentialSunGearSteadyStateSynchronousResponse)

        @property
        def bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2980
            
            return self._parent._cast(_2980.BevelGearSteadyStateSynchronousResponse)

        @property
        def concept_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2993
            
            return self._parent._cast(_2993.ConceptGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2996
            
            return self._parent._cast(_2996.ConicalGearSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3011
            
            return self._parent._cast(_3011.CylindricalGearSteadyStateSynchronousResponse)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3012
            
            return self._parent._cast(_3012.CylindricalPlanetGearSteadyStateSynchronousResponse)

        @property
        def face_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3018
            
            return self._parent._cast(_3018.FaceGearSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3027
            
            return self._parent._cast(_3027.HypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3031
            
            return self._parent._cast(_3031.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3034
            
            return self._parent._cast(_3034.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3037
            
            return self._parent._cast(_3037.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3064
            
            return self._parent._cast(_3064.SpiralBevelGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3073
            
            return self._parent._cast(_3073.StraightBevelDiffGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3076
            
            return self._parent._cast(_3076.StraightBevelGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3077
            
            return self._parent._cast(_3077.StraightBevelPlanetGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3078
            
            return self._parent._cast(_3078.StraightBevelSunGearSteadyStateSynchronousResponse)

        @property
        def worm_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3091
            
            return self._parent._cast(_3091.WormGearSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3094
            
            return self._parent._cast(_3094.ZerolBevelGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(self) -> 'GearSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSteadyStateSynchronousResponse.TYPE'):
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
    def cast_to(self) -> 'GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse':
        return self._Cast_GearSteadyStateSynchronousResponse(self)
