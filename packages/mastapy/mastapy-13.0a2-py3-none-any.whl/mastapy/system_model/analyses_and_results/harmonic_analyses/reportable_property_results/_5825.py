"""_5825.py

FEPartSingleWhineAnalysisResultsPropertyAccessor
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5839, _5845
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'FEPartSingleWhineAnalysisResultsPropertyAccessor')


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartSingleWhineAnalysisResultsPropertyAccessor',)


class FEPartSingleWhineAnalysisResultsPropertyAccessor(_5845.SingleWhineAnalysisResultsPropertyAccessor):
    """FEPartSingleWhineAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _FE_PART_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR

    class _Cast_FEPartSingleWhineAnalysisResultsPropertyAccessor:
        """Special nested class for casting FEPartSingleWhineAnalysisResultsPropertyAccessor to subclasses."""

        def __init__(self, parent: 'FEPartSingleWhineAnalysisResultsPropertyAccessor'):
            self._parent = parent

        @property
        def single_whine_analysis_results_property_accessor(self):
            return self._parent._cast(_5845.SingleWhineAnalysisResultsPropertyAccessor)

        @property
        def abstract_single_whine_analysis_results_property_accessor(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5821
            
            return self._parent._cast(_5821.AbstractSingleWhineAnalysisResultsPropertyAccessor)

        @property
        def fe_part_single_whine_analysis_results_property_accessor(self) -> 'FEPartSingleWhineAnalysisResultsPropertyAccessor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEPartSingleWhineAnalysisResultsPropertyAccessor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orders(self) -> 'List[_5839.ResultsForOrderIncludingSurfaces]':
        """List[ResultsForOrderIncludingSurfaces]: 'Orders' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Orders

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FEPartSingleWhineAnalysisResultsPropertyAccessor._Cast_FEPartSingleWhineAnalysisResultsPropertyAccessor':
        return self._Cast_FEPartSingleWhineAnalysisResultsPropertyAccessor(self)
