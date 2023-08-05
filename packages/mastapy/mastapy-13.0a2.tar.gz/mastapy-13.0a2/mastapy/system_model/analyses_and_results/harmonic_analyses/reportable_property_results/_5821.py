"""_5821.py

AbstractSingleWhineAnalysisResultsPropertyAccessor
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'AbstractSingleWhineAnalysisResultsPropertyAccessor')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractSingleWhineAnalysisResultsPropertyAccessor',)


class AbstractSingleWhineAnalysisResultsPropertyAccessor(_0.APIBase):
    """AbstractSingleWhineAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SINGLE_WHINE_ANALYSIS_RESULTS_PROPERTY_ACCESSOR

    class _Cast_AbstractSingleWhineAnalysisResultsPropertyAccessor:
        """Special nested class for casting AbstractSingleWhineAnalysisResultsPropertyAccessor to subclasses."""

        def __init__(self, parent: 'AbstractSingleWhineAnalysisResultsPropertyAccessor'):
            self._parent = parent

        @property
        def fe_part_single_whine_analysis_results_property_accessor(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5825
            
            return self._parent._cast(_5825.FEPartSingleWhineAnalysisResultsPropertyAccessor)

        @property
        def root_assembly_single_whine_analysis_results_property_accessor(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5844
            
            return self._parent._cast(_5844.RootAssemblySingleWhineAnalysisResultsPropertyAccessor)

        @property
        def single_whine_analysis_results_property_accessor(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5845
            
            return self._parent._cast(_5845.SingleWhineAnalysisResultsPropertyAccessor)

        @property
        def abstract_single_whine_analysis_results_property_accessor(self) -> 'AbstractSingleWhineAnalysisResultsPropertyAccessor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractSingleWhineAnalysisResultsPropertyAccessor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'AbstractSingleWhineAnalysisResultsPropertyAccessor._Cast_AbstractSingleWhineAnalysisResultsPropertyAccessor':
        return self._Cast_AbstractSingleWhineAnalysisResultsPropertyAccessor(self)
