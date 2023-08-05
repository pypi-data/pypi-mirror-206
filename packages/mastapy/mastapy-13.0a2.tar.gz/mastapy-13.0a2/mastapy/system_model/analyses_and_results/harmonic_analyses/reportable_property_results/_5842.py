"""_5842.py

ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_SINGLE_DEGREE_OF_FREEDOM_OF_RESPONSE_OF_NODE_IN_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic',)


class ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic(_0.APIBase):
    """ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_SINGLE_DEGREE_OF_FREEDOM_OF_RESPONSE_OF_NODE_IN_HARMONIC

    class _Cast_ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic:
        """Special nested class for casting ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic to subclasses."""

        def __init__(self, parent: 'ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic'):
            self._parent = parent

        @property
        def results_for_single_degree_of_freedom_of_response_of_node_in_harmonic(self) -> 'ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def frequency_of_max(self) -> 'float':
        """float: 'FrequencyOfMax' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrequencyOfMax

        if temp is None:
            return 0.0

        return temp

    @property
    def integral(self) -> 'float':
        """float: 'Integral' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Integral

        if temp is None:
            return 0.0

        return temp

    @property
    def max(self) -> 'float':
        """float: 'Max' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Max

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic._Cast_ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
        return self._Cast_ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic(self)
