"""_185.py

FEModelModalAnalysisDrawStyle
"""
from mastapy.nodal_analysis.dev_tools_analyses import _189
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODEL_MODAL_ANALYSIS_DRAW_STYLE = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'FEModelModalAnalysisDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('FEModelModalAnalysisDrawStyle',)


class FEModelModalAnalysisDrawStyle(_189.FEModelTabDrawStyle):
    """FEModelModalAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_MODAL_ANALYSIS_DRAW_STYLE

    class _Cast_FEModelModalAnalysisDrawStyle:
        """Special nested class for casting FEModelModalAnalysisDrawStyle to subclasses."""

        def __init__(self, parent: 'FEModelModalAnalysisDrawStyle'):
            self._parent = parent

        @property
        def fe_model_tab_draw_style(self):
            return self._parent._cast(_189.FEModelTabDrawStyle)

        @property
        def fe_model_modal_analysis_draw_style(self) -> 'FEModelModalAnalysisDrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEModelModalAnalysisDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FEModelModalAnalysisDrawStyle._Cast_FEModelModalAnalysisDrawStyle':
        return self._Cast_FEModelModalAnalysisDrawStyle(self)
