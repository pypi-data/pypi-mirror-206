"""_2974.py

BevelDifferentialGearSetSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.part_model.gears import _2495
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6789
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2975, _2973, _2979
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'BevelDifferentialGearSetSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetSteadyStateSynchronousResponse',)


class BevelDifferentialGearSetSteadyStateSynchronousResponse(_2979.BevelGearSetSteadyStateSynchronousResponse):
    """BevelDifferentialGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting BevelDifferentialGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearSetSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def bevel_gear_set_steady_state_synchronous_response(self):
            return self._parent._cast(_2979.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2967
            
            return self._parent._cast(_2967.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse)

        @property
        def conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2995
            
            return self._parent._cast(_2995.ConicalGearSetSteadyStateSynchronousResponse)

        @property
        def gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3022
            
            return self._parent._cast(_3022.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3061
            
            return self._parent._cast(_3061.SpecialisedAssemblySteadyStateSynchronousResponse)

        @property
        def abstract_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2962
            
            return self._parent._cast(_2962.AbstractAssemblySteadyStateSynchronousResponse)

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
        def bevel_differential_gear_set_steady_state_synchronous_response(self) -> 'BevelDifferentialGearSetSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2495.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6789.BevelDifferentialGearSetLoadCase':
        """BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_differential_gears_steady_state_synchronous_response(self) -> 'List[_2975.BevelDifferentialGearSteadyStateSynchronousResponse]':
        """List[BevelDifferentialGearSteadyStateSynchronousResponse]: 'BevelDifferentialGearsSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_steady_state_synchronous_response(self) -> 'List[_2973.BevelDifferentialGearMeshSteadyStateSynchronousResponse]':
        """List[BevelDifferentialGearMeshSteadyStateSynchronousResponse]: 'BevelDifferentialMeshesSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse':
        return self._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse(self)
