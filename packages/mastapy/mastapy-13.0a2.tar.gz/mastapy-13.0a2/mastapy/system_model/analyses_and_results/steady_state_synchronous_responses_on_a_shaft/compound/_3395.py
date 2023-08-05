"""_3395.py

CVTCompoundSteadyStateSynchronousResponseOnAShaft
"""
from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3266
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3364
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'CVTCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTCompoundSteadyStateSynchronousResponseOnAShaft',)


class CVTCompoundSteadyStateSynchronousResponseOnAShaft(_3364.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft):
    """CVTCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_CVTCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CVTCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'CVTCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def belt_drive_compound_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3364.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3452
            
            return self._parent._cast(_3452.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3354
            
            return self._parent._cast(_3354.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3433
            
            return self._parent._cast(_3433.PartCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def cvt_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'CVTCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3266.CVTSteadyStateSynchronousResponseOnAShaft]':
        """List[CVTSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3266.CVTSteadyStateSynchronousResponseOnAShaft]':
        """List[CVTSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CVTCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_CVTCompoundSteadyStateSynchronousResponseOnAShaft(self)
