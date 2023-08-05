"""_2962.py

AbstractAssemblySteadyStateSynchronousResponse
"""
from mastapy.system_model.part_model import _2414
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3042
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'AbstractAssemblySteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblySteadyStateSynchronousResponse',)


class AbstractAssemblySteadyStateSynchronousResponse(_3042.PartSteadyStateSynchronousResponse):
    """AbstractAssemblySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_AbstractAssemblySteadyStateSynchronousResponse:
        """Special nested class for casting AbstractAssemblySteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'AbstractAssemblySteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def part_steady_state_synchronous_response(self):
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
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2967
            
            return self._parent._cast(_2967.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse)

        @property
        def assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2969
            
            return self._parent._cast(_2969.AssemblySteadyStateSynchronousResponse)

        @property
        def belt_drive_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2972
            
            return self._parent._cast(_2972.BeltDriveSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2974
            
            return self._parent._cast(_2974.BevelDifferentialGearSetSteadyStateSynchronousResponse)

        @property
        def bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2979
            
            return self._parent._cast(_2979.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def bolted_joint_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2981
            
            return self._parent._cast(_2981.BoltedJointSteadyStateSynchronousResponse)

        @property
        def clutch_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2985
            
            return self._parent._cast(_2985.ClutchSteadyStateSynchronousResponse)

        @property
        def concept_coupling_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2990
            
            return self._parent._cast(_2990.ConceptCouplingSteadyStateSynchronousResponse)

        @property
        def concept_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2992
            
            return self._parent._cast(_2992.ConceptGearSetSteadyStateSynchronousResponse)

        @property
        def conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2995
            
            return self._parent._cast(_2995.ConicalGearSetSteadyStateSynchronousResponse)

        @property
        def coupling_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3001
            
            return self._parent._cast(_3001.CouplingSteadyStateSynchronousResponse)

        @property
        def cvt_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3004
            
            return self._parent._cast(_3004.CVTSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3005
            
            return self._parent._cast(_3005.CycloidalAssemblySteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3010
            
            return self._parent._cast(_3010.CylindricalGearSetSteadyStateSynchronousResponse)

        @property
        def face_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3017
            
            return self._parent._cast(_3017.FaceGearSetSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3020
            
            return self._parent._cast(_3020.FlexiblePinAssemblySteadyStateSynchronousResponse)

        @property
        def gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3022
            
            return self._parent._cast(_3022.GearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3026
            
            return self._parent._cast(_3026.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3030
            
            return self._parent._cast(_3030.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3033
            
            return self._parent._cast(_3033.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3036
            
            return self._parent._cast(_3036.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3045
            
            return self._parent._cast(_3045.PartToPartShearCouplingSteadyStateSynchronousResponse)

        @property
        def planetary_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3047
            
            return self._parent._cast(_3047.PlanetaryGearSetSteadyStateSynchronousResponse)

        @property
        def rolling_ring_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3054
            
            return self._parent._cast(_3054.RollingRingAssemblySteadyStateSynchronousResponse)

        @property
        def root_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3057
            
            return self._parent._cast(_3057.RootAssemblySteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3061
            
            return self._parent._cast(_3061.SpecialisedAssemblySteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3063
            
            return self._parent._cast(_3063.SpiralBevelGearSetSteadyStateSynchronousResponse)

        @property
        def spring_damper_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3067
            
            return self._parent._cast(_3067.SpringDamperSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3072
            
            return self._parent._cast(_3072.StraightBevelDiffGearSetSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3075
            
            return self._parent._cast(_3075.StraightBevelGearSetSteadyStateSynchronousResponse)

        @property
        def synchroniser_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3082
            
            return self._parent._cast(_3082.SynchroniserSteadyStateSynchronousResponse)

        @property
        def torque_converter_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3085
            
            return self._parent._cast(_3085.TorqueConverterSteadyStateSynchronousResponse)

        @property
        def worm_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3090
            
            return self._parent._cast(_3090.WormGearSetSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3093
            
            return self._parent._cast(_3093.ZerolBevelGearSetSteadyStateSynchronousResponse)

        @property
        def abstract_assembly_steady_state_synchronous_response(self) -> 'AbstractAssemblySteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssemblySteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2414.AbstractAssembly':
        """AbstractAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2414.AbstractAssembly':
        """AbstractAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse':
        return self._Cast_AbstractAssemblySteadyStateSynchronousResponse(self)
