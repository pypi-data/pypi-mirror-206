"""_7514.py

ConsoleProgress
"""
from mastapy._internal import constructor
from mastapy import _7521
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONSOLE_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'ConsoleProgress')


__docformat__ = 'restructuredtext en'
__all__ = ('ConsoleProgress',)


class ConsoleProgress(_7521.TaskProgress):
    """ConsoleProgress

    This is a mastapy class.
    """

    TYPE = _CONSOLE_PROGRESS

    class _Cast_ConsoleProgress:
        """Special nested class for casting ConsoleProgress to subclasses."""

        def __init__(self, parent: 'ConsoleProgress'):
            self._parent = parent

        @property
        def console_progress(self) -> 'ConsoleProgress':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConsoleProgress.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def id(self) -> 'int':
        """int: 'Id' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Id

        if temp is None:
            return 0

        return temp

    def add_error(self, error: 'str'):
        """ 'AddError' is the original name of this method.

        Args:
            error (str)
        """

        error = str(error)
        self.wrapped.AddError(error if error else '')

    def complete(self):
        """ 'Complete' is the original name of this method."""

        self.wrapped.Complete()

    @property
    def cast_to(self) -> 'ConsoleProgress._Cast_ConsoleProgress':
        return self._Cast_ConsoleProgress(self)
