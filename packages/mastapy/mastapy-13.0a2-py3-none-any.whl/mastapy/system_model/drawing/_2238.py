"""_2238.py

StabilityAnalysisViewable
"""
from mastapy.system_model.drawing import _2236
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STABILITY_ANALYSIS_VIEWABLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'StabilityAnalysisViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('StabilityAnalysisViewable',)


class StabilityAnalysisViewable(_2236.RotorDynamicsViewable):
    """StabilityAnalysisViewable

    This is a mastapy class.
    """

    TYPE = _STABILITY_ANALYSIS_VIEWABLE

    class _Cast_StabilityAnalysisViewable:
        """Special nested class for casting StabilityAnalysisViewable to subclasses."""

        def __init__(self, parent: 'StabilityAnalysisViewable'):
            self._parent = parent

        @property
        def rotor_dynamics_viewable(self):
            return self._parent._cast(_2236.RotorDynamicsViewable)

        @property
        def stability_analysis_viewable(self) -> 'StabilityAnalysisViewable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StabilityAnalysisViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'StabilityAnalysisViewable._Cast_StabilityAnalysisViewable':
        return self._Cast_StabilityAnalysisViewable(self)
