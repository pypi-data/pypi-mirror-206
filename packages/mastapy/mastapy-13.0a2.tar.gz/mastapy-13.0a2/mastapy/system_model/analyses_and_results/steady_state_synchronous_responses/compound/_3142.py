"""_3142.py

CylindricalGearCompoundSteadyStateSynchronousResponse
"""
from typing import List

from mastapy.system_model.part_model.gears import _2504
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3011
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3153
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'CylindricalGearCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearCompoundSteadyStateSynchronousResponse',)


class CylindricalGearCompoundSteadyStateSynchronousResponse(_3153.GearCompoundSteadyStateSynchronousResponse):
    """CylindricalGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_CylindricalGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CylindricalGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'CylindricalGearCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def gear_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3153.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3172
            
            return self._parent._cast(_3172.MountableComponentCompoundSteadyStateSynchronousResponse)

        @property
        def component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3120
            
            return self._parent._cast(_3120.ComponentCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3174
            
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
        def cylindrical_planet_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3145
            
            return self._parent._cast(_3145.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response(self) -> 'CylindricalGearCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2504.CylindricalGear':
        """CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3011.CylindricalGearSteadyStateSynchronousResponse]':
        """List[CylindricalGearSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[CylindricalGearCompoundSteadyStateSynchronousResponse]':
        """List[CylindricalGearCompoundSteadyStateSynchronousResponse]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3011.CylindricalGearSteadyStateSynchronousResponse]':
        """List[CylindricalGearSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalGearCompoundSteadyStateSynchronousResponse':
        return self._Cast_CylindricalGearCompoundSteadyStateSynchronousResponse(self)
