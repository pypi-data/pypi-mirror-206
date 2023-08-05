"""_183.py

FEModelHarmonicAnalysisDrawStyle
"""
from mastapy.nodal_analysis.dev_tools_analyses import _189
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODEL_HARMONIC_ANALYSIS_DRAW_STYLE = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'FEModelHarmonicAnalysisDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('FEModelHarmonicAnalysisDrawStyle',)


class FEModelHarmonicAnalysisDrawStyle(_189.FEModelTabDrawStyle):
    """FEModelHarmonicAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_HARMONIC_ANALYSIS_DRAW_STYLE

    class _Cast_FEModelHarmonicAnalysisDrawStyle:
        """Special nested class for casting FEModelHarmonicAnalysisDrawStyle to subclasses."""

        def __init__(self, parent: 'FEModelHarmonicAnalysisDrawStyle'):
            self._parent = parent

        @property
        def fe_model_tab_draw_style(self):
            return self._parent._cast(_189.FEModelTabDrawStyle)

        @property
        def fe_model_harmonic_analysis_draw_style(self) -> 'FEModelHarmonicAnalysisDrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEModelHarmonicAnalysisDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FEModelHarmonicAnalysisDrawStyle._Cast_FEModelHarmonicAnalysisDrawStyle':
        return self._Cast_FEModelHarmonicAnalysisDrawStyle(self)
