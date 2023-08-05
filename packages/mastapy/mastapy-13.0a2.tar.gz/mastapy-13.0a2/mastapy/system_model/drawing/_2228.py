"""_2228.py

CriticalSpeedAnalysisViewable
"""
from mastapy.system_model.drawing import _2236
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CRITICAL_SPEED_ANALYSIS_VIEWABLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'CriticalSpeedAnalysisViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('CriticalSpeedAnalysisViewable',)


class CriticalSpeedAnalysisViewable(_2236.RotorDynamicsViewable):
    """CriticalSpeedAnalysisViewable

    This is a mastapy class.
    """

    TYPE = _CRITICAL_SPEED_ANALYSIS_VIEWABLE

    class _Cast_CriticalSpeedAnalysisViewable:
        """Special nested class for casting CriticalSpeedAnalysisViewable to subclasses."""

        def __init__(self, parent: 'CriticalSpeedAnalysisViewable'):
            self._parent = parent

        @property
        def rotor_dynamics_viewable(self):
            return self._parent._cast(_2236.RotorDynamicsViewable)

        @property
        def critical_speed_analysis_viewable(self) -> 'CriticalSpeedAnalysisViewable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CriticalSpeedAnalysisViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CriticalSpeedAnalysisViewable._Cast_CriticalSpeedAnalysisViewable':
        return self._Cast_CriticalSpeedAnalysisViewable(self)
