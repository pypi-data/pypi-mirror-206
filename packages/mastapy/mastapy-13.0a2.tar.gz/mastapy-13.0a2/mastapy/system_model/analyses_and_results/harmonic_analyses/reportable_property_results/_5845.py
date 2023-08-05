"""_5845.py

SingleWhineAnalysisResultsPropertyAccessor
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5838, _5821
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'SingleWhineAnalysisResultsPropertyAccessor')


__docformat__ = 'restructuredtext en'
__all__ = ('SingleWhineAnalysisResultsPropertyAccessor',)


class SingleWhineAnalysisResultsPropertyAccessor(_5821.AbstractSingleWhineAnalysisResultsPropertyAccessor):
    """SingleWhineAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR

    class _Cast_SingleWhineAnalysisResultsPropertyAccessor:
        """Special nested class for casting SingleWhineAnalysisResultsPropertyAccessor to subclasses."""

        def __init__(self, parent: 'SingleWhineAnalysisResultsPropertyAccessor'):
            self._parent = parent

        @property
        def abstract_single_whine_analysis_results_property_accessor(self):
            return self._parent._cast(_5821.AbstractSingleWhineAnalysisResultsPropertyAccessor)

        @property
        def fe_part_single_whine_analysis_results_property_accessor(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5825
            
            return self._parent._cast(_5825.FEPartSingleWhineAnalysisResultsPropertyAccessor)

        @property
        def single_whine_analysis_results_property_accessor(self) -> 'SingleWhineAnalysisResultsPropertyAccessor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SingleWhineAnalysisResultsPropertyAccessor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orders(self) -> 'List[_5838.ResultsForOrderIncludingNodes]':
        """List[ResultsForOrderIncludingNodes]: 'Orders' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Orders

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SingleWhineAnalysisResultsPropertyAccessor._Cast_SingleWhineAnalysisResultsPropertyAccessor':
        return self._Cast_SingleWhineAnalysisResultsPropertyAccessor(self)
