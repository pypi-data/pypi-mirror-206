"""_7532.py

ScriptingObjectCommand
"""
from typing import TypeVar, Generic

from mastapy._internal import constructor
from mastapy.scripting import _7530
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCRIPTING_OBJECT_COMMAND = python_net_import('SMT.MastaAPIUtility.Scripting', 'ScriptingObjectCommand')


__docformat__ = 'restructuredtext en'
__all__ = ('ScriptingObjectCommand',)


T = TypeVar('T', bound='object')


class ScriptingObjectCommand(_7530.ScriptingCommand, Generic[T]):
    """ScriptingObjectCommand

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _SCRIPTING_OBJECT_COMMAND

    class _Cast_ScriptingObjectCommand:
        """Special nested class for casting ScriptingObjectCommand to subclasses."""

        def __init__(self, parent: 'ScriptingObjectCommand'):
            self._parent = parent

        @property
        def scripting_object_command(self) -> 'ScriptingObjectCommand':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ScriptingObjectCommand.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def execute(self):
        """ 'Execute' is the original name of this method."""

        self.wrapped.Execute()

    @property
    def cast_to(self) -> 'ScriptingObjectCommand._Cast_ScriptingObjectCommand':
        return self._Cast_ScriptingObjectCommand(self)
