"""_2239.py

SteadyStateSynchronousResponseViewable
"""
from mastapy.system_model.drawing import _2236
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_VIEWABLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'SteadyStateSynchronousResponseViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('SteadyStateSynchronousResponseViewable',)


class SteadyStateSynchronousResponseViewable(_2236.RotorDynamicsViewable):
    """SteadyStateSynchronousResponseViewable

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_VIEWABLE

    class _Cast_SteadyStateSynchronousResponseViewable:
        """Special nested class for casting SteadyStateSynchronousResponseViewable to subclasses."""

        def __init__(self, parent: 'SteadyStateSynchronousResponseViewable'):
            self._parent = parent

        @property
        def rotor_dynamics_viewable(self):
            return self._parent._cast(_2236.RotorDynamicsViewable)

        @property
        def steady_state_synchronous_response_viewable(self) -> 'SteadyStateSynchronousResponseViewable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SteadyStateSynchronousResponseViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SteadyStateSynchronousResponseViewable._Cast_SteadyStateSynchronousResponseViewable':
        return self._Cast_SteadyStateSynchronousResponseViewable(self)
