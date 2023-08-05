"""_4692.py

DesignEntityModalAnalysisGroupResults
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY_MODAL_ANALYSIS_GROUP_RESULTS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting', 'DesignEntityModalAnalysisGroupResults')


__docformat__ = 'restructuredtext en'
__all__ = ('DesignEntityModalAnalysisGroupResults',)


class DesignEntityModalAnalysisGroupResults(_0.APIBase):
    """DesignEntityModalAnalysisGroupResults

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY_MODAL_ANALYSIS_GROUP_RESULTS

    class _Cast_DesignEntityModalAnalysisGroupResults:
        """Special nested class for casting DesignEntityModalAnalysisGroupResults to subclasses."""

        def __init__(self, parent: 'DesignEntityModalAnalysisGroupResults'):
            self._parent = parent

        @property
        def single_excitation_results_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4699
            
            return self._parent._cast(_4699.SingleExcitationResultsModalAnalysis)

        @property
        def single_mode_results(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4700
            
            return self._parent._cast(_4700.SingleModeResults)

        @property
        def design_entity_modal_analysis_group_results(self) -> 'DesignEntityModalAnalysisGroupResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DesignEntityModalAnalysisGroupResults.TYPE'):
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
    def cast_to(self) -> 'DesignEntityModalAnalysisGroupResults._Cast_DesignEntityModalAnalysisGroupResults':
        return self._Cast_DesignEntityModalAnalysisGroupResults(self)
