"""_5431.py

MBDAnalysisDrawStyle
"""
from mastapy.system_model.drawing import _2227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MBD_ANALYSIS_DRAW_STYLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'MBDAnalysisDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('MBDAnalysisDrawStyle',)


class MBDAnalysisDrawStyle(_2227.ContourDrawStyle):
    """MBDAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _MBD_ANALYSIS_DRAW_STYLE

    class _Cast_MBDAnalysisDrawStyle:
        """Special nested class for casting MBDAnalysisDrawStyle to subclasses."""

        def __init__(self, parent: 'MBDAnalysisDrawStyle'):
            self._parent = parent

        @property
        def contour_draw_style(self):
            return self._parent._cast(_2227.ContourDrawStyle)

        @property
        def draw_style_base(self):
            from mastapy.geometry import _304
            
            return self._parent._cast(_304.DrawStyleBase)

        @property
        def mbd_analysis_draw_style(self) -> 'MBDAnalysisDrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MBDAnalysisDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MBDAnalysisDrawStyle._Cast_MBDAnalysisDrawStyle':
        return self._Cast_MBDAnalysisDrawStyle(self)
