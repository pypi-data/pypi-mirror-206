"""_3848.py

StabilityAnalysisDrawStyle
"""
from mastapy.system_model.analyses_and_results.rotor_dynamics import _4003
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STABILITY_ANALYSIS_DRAW_STYLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'StabilityAnalysisDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('StabilityAnalysisDrawStyle',)


class StabilityAnalysisDrawStyle(_4003.RotorDynamicsDrawStyle):
    """StabilityAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _STABILITY_ANALYSIS_DRAW_STYLE

    class _Cast_StabilityAnalysisDrawStyle:
        """Special nested class for casting StabilityAnalysisDrawStyle to subclasses."""

        def __init__(self, parent: 'StabilityAnalysisDrawStyle'):
            self._parent = parent

        @property
        def rotor_dynamics_draw_style(self):
            return self._parent._cast(_4003.RotorDynamicsDrawStyle)

        @property
        def contour_draw_style(self):
            from mastapy.system_model.drawing import _2227
            
            return self._parent._cast(_2227.ContourDrawStyle)

        @property
        def draw_style_base(self):
            from mastapy.geometry import _304
            
            return self._parent._cast(_304.DrawStyleBase)

        @property
        def stability_analysis_draw_style(self) -> 'StabilityAnalysisDrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StabilityAnalysisDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'StabilityAnalysisDrawStyle._Cast_StabilityAnalysisDrawStyle':
        return self._Cast_StabilityAnalysisDrawStyle(self)
