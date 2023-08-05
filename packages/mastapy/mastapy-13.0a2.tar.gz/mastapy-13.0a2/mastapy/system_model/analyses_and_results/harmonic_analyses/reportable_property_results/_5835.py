"""_5835.py

ResultsForMultipleOrdersForGroups
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5828, _5833
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_MULTIPLE_ORDERS_FOR_GROUPS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'ResultsForMultipleOrdersForGroups')


__docformat__ = 'restructuredtext en'
__all__ = ('ResultsForMultipleOrdersForGroups',)


class ResultsForMultipleOrdersForGroups(_5833.ResultsForMultipleOrders):
    """ResultsForMultipleOrdersForGroups

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_MULTIPLE_ORDERS_FOR_GROUPS

    class _Cast_ResultsForMultipleOrdersForGroups:
        """Special nested class for casting ResultsForMultipleOrdersForGroups to subclasses."""

        def __init__(self, parent: 'ResultsForMultipleOrdersForGroups'):
            self._parent = parent

        @property
        def results_for_multiple_orders(self):
            return self._parent._cast(_5833.ResultsForMultipleOrders)

        @property
        def results_for_multiple_orders_for_groups(self) -> 'ResultsForMultipleOrdersForGroups':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ResultsForMultipleOrdersForGroups.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def groups(self) -> 'List[_5828.HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic]':
        """List[HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic]: 'Groups' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Groups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ResultsForMultipleOrdersForGroups._Cast_ResultsForMultipleOrdersForGroups':
        return self._Cast_ResultsForMultipleOrdersForGroups(self)
