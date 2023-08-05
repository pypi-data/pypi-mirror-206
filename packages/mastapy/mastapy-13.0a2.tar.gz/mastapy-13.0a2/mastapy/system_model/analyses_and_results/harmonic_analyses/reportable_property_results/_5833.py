"""_5833.py

ResultsForMultipleOrders
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_MULTIPLE_ORDERS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'ResultsForMultipleOrders')


__docformat__ = 'restructuredtext en'
__all__ = ('ResultsForMultipleOrders',)


class ResultsForMultipleOrders(_0.APIBase):
    """ResultsForMultipleOrders

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_MULTIPLE_ORDERS

    class _Cast_ResultsForMultipleOrders:
        """Special nested class for casting ResultsForMultipleOrders to subclasses."""

        def __init__(self, parent: 'ResultsForMultipleOrders'):
            self._parent = parent

        @property
        def results_for_multiple_orders_for_fe_surface(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5834
            
            return self._parent._cast(_5834.ResultsForMultipleOrdersForFESurface)

        @property
        def results_for_multiple_orders_for_groups(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5835
            
            return self._parent._cast(_5835.ResultsForMultipleOrdersForGroups)

        @property
        def results_for_multiple_orders(self) -> 'ResultsForMultipleOrders':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ResultsForMultipleOrders.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def combined_excitations_harmonics_and_orders(self) -> 'str':
        """str: 'CombinedExcitationsHarmonicsAndOrders' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CombinedExcitationsHarmonicsAndOrders

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'ResultsForMultipleOrders._Cast_ResultsForMultipleOrders':
        return self._Cast_ResultsForMultipleOrders(self)
