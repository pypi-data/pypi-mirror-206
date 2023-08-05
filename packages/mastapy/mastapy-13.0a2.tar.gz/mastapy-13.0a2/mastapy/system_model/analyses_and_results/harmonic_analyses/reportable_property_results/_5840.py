"""_5840.py

ResultsForResponseOfAComponentOrSurfaceInAHarmonic
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5842, _5822
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_RESPONSE_OF_A_COMPONENT_OR_SURFACE_IN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'ResultsForResponseOfAComponentOrSurfaceInAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('ResultsForResponseOfAComponentOrSurfaceInAHarmonic',)


class ResultsForResponseOfAComponentOrSurfaceInAHarmonic(_0.APIBase):
    """ResultsForResponseOfAComponentOrSurfaceInAHarmonic

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_RESPONSE_OF_A_COMPONENT_OR_SURFACE_IN_A_HARMONIC

    class _Cast_ResultsForResponseOfAComponentOrSurfaceInAHarmonic:
        """Special nested class for casting ResultsForResponseOfAComponentOrSurfaceInAHarmonic to subclasses."""

        def __init__(self, parent: 'ResultsForResponseOfAComponentOrSurfaceInAHarmonic'):
            self._parent = parent

        @property
        def results_for_response_of_a_component_or_surface_in_a_harmonic(self) -> 'ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ResultsForResponseOfAComponentOrSurfaceInAHarmonic.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnitude(self) -> '_5842.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
        """ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic: 'Magnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Magnitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def result_at_reference_speed(self) -> '_5822.DatapointForResponseOfAComponentOrSurfaceAtAFrequencyInAHarmonic':
        """DatapointForResponseOfAComponentOrSurfaceAtAFrequencyInAHarmonic: 'ResultAtReferenceSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultAtReferenceSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def data_points(self) -> 'List[_5822.DatapointForResponseOfAComponentOrSurfaceAtAFrequencyInAHarmonic]':
        """List[DatapointForResponseOfAComponentOrSurfaceAtAFrequencyInAHarmonic]: 'DataPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DataPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ResultsForResponseOfAComponentOrSurfaceInAHarmonic._Cast_ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        return self._Cast_ResultsForResponseOfAComponentOrSurfaceInAHarmonic(self)
