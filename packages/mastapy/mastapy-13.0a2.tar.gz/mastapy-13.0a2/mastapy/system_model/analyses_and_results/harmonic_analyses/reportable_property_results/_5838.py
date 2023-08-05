"""_5838.py

ResultsForOrderIncludingNodes
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5830, _5836
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_ORDER_INCLUDING_NODES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'ResultsForOrderIncludingNodes')


__docformat__ = 'restructuredtext en'
__all__ = ('ResultsForOrderIncludingNodes',)


class ResultsForOrderIncludingNodes(_5836.ResultsForOrder):
    """ResultsForOrderIncludingNodes

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_ORDER_INCLUDING_NODES

    class _Cast_ResultsForOrderIncludingNodes:
        """Special nested class for casting ResultsForOrderIncludingNodes to subclasses."""

        def __init__(self, parent: 'ResultsForOrderIncludingNodes'):
            self._parent = parent

        @property
        def results_for_order(self):
            return self._parent._cast(_5836.ResultsForOrder)

        @property
        def results_for_order_including_surfaces(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5839
            
            return self._parent._cast(_5839.ResultsForOrderIncludingSurfaces)

        @property
        def results_for_order_including_nodes(self) -> 'ResultsForOrderIncludingNodes':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ResultsForOrderIncludingNodes.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def node_results_global_coordinate_system(self) -> 'List[_5830.HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic]':
        """List[HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic]: 'NodeResultsGlobalCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeResultsGlobalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def node_results_local_coordinate_system(self) -> 'List[_5830.HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic]':
        """List[HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic]: 'NodeResultsLocalCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeResultsLocalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ResultsForOrderIncludingNodes._Cast_ResultsForOrderIncludingNodes':
        return self._Cast_ResultsForOrderIncludingNodes(self)
