"""_5824.py

FEPartHarmonicAnalysisResultsPropertyAccessor
"""
from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5834, _5825, _5839, _5832
)
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_HARMONIC_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'FEPartHarmonicAnalysisResultsPropertyAccessor')


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartHarmonicAnalysisResultsPropertyAccessor',)


class FEPartHarmonicAnalysisResultsPropertyAccessor(_5832.HarmonicAnalysisResultsPropertyAccessor):
    """FEPartHarmonicAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _FE_PART_HARMONIC_ANALYSIS_RESULTS_PROPERTY_ACCESSOR

    class _Cast_FEPartHarmonicAnalysisResultsPropertyAccessor:
        """Special nested class for casting FEPartHarmonicAnalysisResultsPropertyAccessor to subclasses."""

        def __init__(self, parent: 'FEPartHarmonicAnalysisResultsPropertyAccessor'):
            self._parent = parent

        @property
        def harmonic_analysis_results_property_accessor(self):
            return self._parent._cast(_5832.HarmonicAnalysisResultsPropertyAccessor)

        @property
        def fe_part_harmonic_analysis_results_property_accessor(self) -> 'FEPartHarmonicAnalysisResultsPropertyAccessor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEPartHarmonicAnalysisResultsPropertyAccessor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def combined_orders(self) -> '_5834.ResultsForMultipleOrdersForFESurface':
        """ResultsForMultipleOrdersForFESurface: 'CombinedOrders' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CombinedOrders

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitations(self) -> 'List[_5825.FEPartSingleWhineAnalysisResultsPropertyAccessor]':
        """List[FEPartSingleWhineAnalysisResultsPropertyAccessor]: 'Excitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def orders_for_combined_excitations(self) -> 'List[_5839.ResultsForOrderIncludingSurfaces]':
        """List[ResultsForOrderIncludingSurfaces]: 'OrdersForCombinedExcitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OrdersForCombinedExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def orders_for_combined_excitations_from_same_parts(self) -> 'List[_5839.ResultsForOrderIncludingSurfaces]':
        """List[ResultsForOrderIncludingSurfaces]: 'OrdersForCombinedExcitationsFromSameParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OrdersForCombinedExcitationsFromSameParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FEPartHarmonicAnalysisResultsPropertyAccessor._Cast_FEPartHarmonicAnalysisResultsPropertyAccessor':
        return self._Cast_FEPartHarmonicAnalysisResultsPropertyAccessor(self)
