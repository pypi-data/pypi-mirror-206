"""_3095.py

AbstractAssemblyCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2962
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3174
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'AbstractAssemblyCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblyCompoundSteadyStateSynchronousResponse',)


class AbstractAssemblyCompoundSteadyStateSynchronousResponse(_3174.PartCompoundSteadyStateSynchronousResponse):
    """AbstractAssemblyCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractAssemblyCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'AbstractAssemblyCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def part_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3174.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3101
            
            return self._parent._cast(_3101.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3102
            
            return self._parent._cast(_3102.AssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def belt_drive_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3105
            
            return self._parent._cast(_3105.BeltDriveCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3108
            
            return self._parent._cast(_3108.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3113
            
            return self._parent._cast(_3113.BevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def bolted_joint_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3115
            
            return self._parent._cast(_3115.BoltedJointCompoundSteadyStateSynchronousResponse)

        @property
        def clutch_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3116
            
            return self._parent._cast(_3116.ClutchCompoundSteadyStateSynchronousResponse)

        @property
        def concept_coupling_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3121
            
            return self._parent._cast(_3121.ConceptCouplingCompoundSteadyStateSynchronousResponse)

        @property
        def concept_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3126
            
            return self._parent._cast(_3126.ConceptGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3129
            
            return self._parent._cast(_3129.ConicalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def coupling_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3132
            
            return self._parent._cast(_3132.CouplingCompoundSteadyStateSynchronousResponse)

        @property
        def cvt_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3136
            
            return self._parent._cast(_3136.CVTCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3138
            
            return self._parent._cast(_3138.CycloidalAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3144
            
            return self._parent._cast(_3144.CylindricalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def face_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3150
            
            return self._parent._cast(_3150.FaceGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3152
            
            return self._parent._cast(_3152.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3155
            
            return self._parent._cast(_3155.GearSetCompoundSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3159
            
            return self._parent._cast(_3159.HypoidGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3163
            
            return self._parent._cast(_3163.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3166
            
            return self._parent._cast(_3166.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3169
            
            return self._parent._cast(_3169.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3175
            
            return self._parent._cast(_3175.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse)

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3179
            
            return self._parent._cast(_3179.PlanetaryGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3186
            
            return self._parent._cast(_3186.RollingRingAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def root_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3189
            
            return self._parent._cast(_3189.RootAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3193
            
            return self._parent._cast(_3193.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3196
            
            return self._parent._cast(_3196.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def spring_damper_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3197
            
            return self._parent._cast(_3197.SpringDamperCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3202
            
            return self._parent._cast(_3202.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3205
            
            return self._parent._cast(_3205.StraightBevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def synchroniser_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3208
            
            return self._parent._cast(_3208.SynchroniserCompoundSteadyStateSynchronousResponse)

        @property
        def torque_converter_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3212
            
            return self._parent._cast(_3212.TorqueConverterCompoundSteadyStateSynchronousResponse)

        @property
        def worm_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3220
            
            return self._parent._cast(_3220.WormGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3223
            
            return self._parent._cast(_3223.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(self) -> 'AbstractAssemblyCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssemblyCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_2962.AbstractAssemblySteadyStateSynchronousResponse]':
        """List[AbstractAssemblySteadyStateSynchronousResponse]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2962.AbstractAssemblySteadyStateSynchronousResponse]':
        """List[AbstractAssemblySteadyStateSynchronousResponse]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse':
        return self._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse(self)
