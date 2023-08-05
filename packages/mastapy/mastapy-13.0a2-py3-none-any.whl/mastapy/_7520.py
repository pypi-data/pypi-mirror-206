"""_7520.py

SimpleTaskProgress
"""
from mastapy._internal import constructor
from mastapy import _7514
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SIMPLE_TASK_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'SimpleTaskProgress')


__docformat__ = 'restructuredtext en'
__all__ = ('SimpleTaskProgress',)


class SimpleTaskProgress(_7514.ConsoleProgress):
    """SimpleTaskProgress

    This is a mastapy class.
    """

    TYPE = _SIMPLE_TASK_PROGRESS

    class _Cast_SimpleTaskProgress:
        """Special nested class for casting SimpleTaskProgress to subclasses."""

        def __init__(self, parent: 'SimpleTaskProgress'):
            self._parent = parent

        @property
        def simple_task_progress(self) -> 'SimpleTaskProgress':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SimpleTaskProgress.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def complete(self):
        """ 'Complete' is the original name of this method."""

        self.wrapped.Complete()

    @property
    def cast_to(self) -> 'SimpleTaskProgress._Cast_SimpleTaskProgress':
        return self._Cast_SimpleTaskProgress(self)
