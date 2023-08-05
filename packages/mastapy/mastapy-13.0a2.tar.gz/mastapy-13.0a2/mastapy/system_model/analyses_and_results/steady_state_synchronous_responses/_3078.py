"""_3078.py

StraightBevelSunGearSteadyStateSynchronousResponse
"""
from mastapy.system_model.part_model.gears import _2529
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3073
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'StraightBevelSunGearSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelSunGearSteadyStateSynchronousResponse',)


class StraightBevelSunGearSteadyStateSynchronousResponse(_3073.StraightBevelDiffGearSteadyStateSynchronousResponse):
    """StraightBevelSunGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_StraightBevelSunGearSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelSunGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'StraightBevelSunGearSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(self):
            return self._parent._cast(_3073.StraightBevelDiffGearSteadyStateSynchronousResponse)

        @property
        def bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2980
            
            return self._parent._cast(_2980.BevelGearSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2968
            
            return self._parent._cast(_2968.AGMAGleasonConicalGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2996
            
            return self._parent._cast(_2996.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3023
            
            return self._parent._cast(_3023.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3040
            
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
        def straight_bevel_sun_gear_steady_state_synchronous_response(self) -> 'StraightBevelSunGearSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelSunGearSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2529.StraightBevelSunGear':
        """StraightBevelSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse':
        return self._Cast_StraightBevelSunGearSteadyStateSynchronousResponse(self)
