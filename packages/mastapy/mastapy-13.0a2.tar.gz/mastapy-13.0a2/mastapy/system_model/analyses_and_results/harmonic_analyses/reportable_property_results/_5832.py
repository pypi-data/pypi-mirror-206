"""_5832.py

HarmonicAnalysisResultsPropertyAccessor
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5845, _5838
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'HarmonicAnalysisResultsPropertyAccessor')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisResultsPropertyAccessor',)


class HarmonicAnalysisResultsPropertyAccessor(_0.APIBase):
    """HarmonicAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_RESULTS_PROPERTY_ACCESSOR

    class _Cast_HarmonicAnalysisResultsPropertyAccessor:
        """Special nested class for casting HarmonicAnalysisResultsPropertyAccessor to subclasses."""

        def __init__(self, parent: 'HarmonicAnalysisResultsPropertyAccessor'):
            self._parent = parent

        @property
        def fe_part_harmonic_analysis_results_property_accessor(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5824
            
            return self._parent._cast(_5824.FEPartHarmonicAnalysisResultsPropertyAccessor)

        @property
        def harmonic_analysis_results_property_accessor(self) -> 'HarmonicAnalysisResultsPropertyAccessor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisResultsPropertyAccessor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitations(self) -> 'List[_5845.SingleWhineAnalysisResultsPropertyAccessor]':
        """List[SingleWhineAnalysisResultsPropertyAccessor]: 'Excitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def orders_for_combined_excitations(self) -> 'List[_5838.ResultsForOrderIncludingNodes]':
        """List[ResultsForOrderIncludingNodes]: 'OrdersForCombinedExcitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OrdersForCombinedExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def orders_for_combined_excitations_from_same_parts(self) -> 'List[_5838.ResultsForOrderIncludingNodes]':
        """List[ResultsForOrderIncludingNodes]: 'OrdersForCombinedExcitationsFromSameParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OrdersForCombinedExcitationsFromSameParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'HarmonicAnalysisResultsPropertyAccessor._Cast_HarmonicAnalysisResultsPropertyAccessor':
        return self._Cast_HarmonicAnalysisResultsPropertyAccessor(self)
