"""_5844.py

RootAssemblySingleWhineAnalysisResultsPropertyAccessor
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5837, _5821
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'RootAssemblySingleWhineAnalysisResultsPropertyAccessor')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblySingleWhineAnalysisResultsPropertyAccessor',)


class RootAssemblySingleWhineAnalysisResultsPropertyAccessor(_5821.AbstractSingleWhineAnalysisResultsPropertyAccessor):
    """RootAssemblySingleWhineAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR

    class _Cast_RootAssemblySingleWhineAnalysisResultsPropertyAccessor:
        """Special nested class for casting RootAssemblySingleWhineAnalysisResultsPropertyAccessor to subclasses."""

        def __init__(self, parent: 'RootAssemblySingleWhineAnalysisResultsPropertyAccessor'):
            self._parent = parent

        @property
        def abstract_single_whine_analysis_results_property_accessor(self):
            return self._parent._cast(_5821.AbstractSingleWhineAnalysisResultsPropertyAccessor)

        @property
        def root_assembly_single_whine_analysis_results_property_accessor(self) -> 'RootAssemblySingleWhineAnalysisResultsPropertyAccessor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblySingleWhineAnalysisResultsPropertyAccessor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orders(self) -> 'List[_5837.ResultsForOrderIncludingGroups]':
        """List[ResultsForOrderIncludingGroups]: 'Orders' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Orders

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RootAssemblySingleWhineAnalysisResultsPropertyAccessor._Cast_RootAssemblySingleWhineAnalysisResultsPropertyAccessor':
        return self._Cast_RootAssemblySingleWhineAnalysisResultsPropertyAccessor(self)
