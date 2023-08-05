"""_188.py

FEModelStaticAnalysisDrawStyle
"""
from mastapy._internal import constructor
from mastapy.nodal_analysis.dev_tools_analyses import _189
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODEL_STATIC_ANALYSIS_DRAW_STYLE = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'FEModelStaticAnalysisDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('FEModelStaticAnalysisDrawStyle',)


class FEModelStaticAnalysisDrawStyle(_189.FEModelTabDrawStyle):
    """FEModelStaticAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_STATIC_ANALYSIS_DRAW_STYLE

    class _Cast_FEModelStaticAnalysisDrawStyle:
        """Special nested class for casting FEModelStaticAnalysisDrawStyle to subclasses."""

        def __init__(self, parent: 'FEModelStaticAnalysisDrawStyle'):
            self._parent = parent

        @property
        def fe_model_tab_draw_style(self):
            return self._parent._cast(_189.FEModelTabDrawStyle)

        @property
        def fe_model_static_analysis_draw_style(self) -> 'FEModelStaticAnalysisDrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEModelStaticAnalysisDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_force_arrows(self) -> 'bool':
        """bool: 'ShowForceArrows' is the original name of this property."""

        temp = self.wrapped.ShowForceArrows

        if temp is None:
            return False

        return temp

    @show_force_arrows.setter
    def show_force_arrows(self, value: 'bool'):
        self.wrapped.ShowForceArrows = bool(value) if value else False

    @property
    def cast_to(self) -> 'FEModelStaticAnalysisDrawStyle._Cast_FEModelStaticAnalysisDrawStyle':
        return self._Cast_FEModelStaticAnalysisDrawStyle(self)
