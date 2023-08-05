"""_5839.py

ResultsForOrderIncludingSurfaces
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5831, _5838
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_ORDER_INCLUDING_SURFACES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'ResultsForOrderIncludingSurfaces')


__docformat__ = 'restructuredtext en'
__all__ = ('ResultsForOrderIncludingSurfaces',)


class ResultsForOrderIncludingSurfaces(_5838.ResultsForOrderIncludingNodes):
    """ResultsForOrderIncludingSurfaces

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_ORDER_INCLUDING_SURFACES

    class _Cast_ResultsForOrderIncludingSurfaces:
        """Special nested class for casting ResultsForOrderIncludingSurfaces to subclasses."""

        def __init__(self, parent: 'ResultsForOrderIncludingSurfaces'):
            self._parent = parent

        @property
        def results_for_order_including_nodes(self):
            return self._parent._cast(_5838.ResultsForOrderIncludingNodes)

        @property
        def results_for_order(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5836
            
            return self._parent._cast(_5836.ResultsForOrder)

        @property
        def results_for_order_including_surfaces(self) -> 'ResultsForOrderIncludingSurfaces':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ResultsForOrderIncludingSurfaces.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_surfaces(self) -> 'List[_5831.HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic]':
        """List[HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic]: 'FESurfaces' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FESurfaces

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ResultsForOrderIncludingSurfaces._Cast_ResultsForOrderIncludingSurfaces':
        return self._Cast_ResultsForOrderIncludingSurfaces(self)
