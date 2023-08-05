"""_1566.py

Command
"""
from mastapy._internal import constructor
from mastapy import _7515
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMMAND = python_net_import('SMT.MastaAPI.Utility', 'Command')


__docformat__ = 'restructuredtext en'
__all__ = ('Command',)


class Command(_7515.MarshalByRefObjectPermanent):
    """Command

    This is a mastapy class.
    """

    TYPE = _COMMAND

    class _Cast_Command:
        """Special nested class for casting Command to subclasses."""

        def __init__(self, parent: 'Command'):
            self._parent = parent

        @property
        def marshal_by_ref_object_permanent(self):
            return self._parent._cast(_7515.MarshalByRefObjectPermanent)

        @property
        def command(self) -> 'Command':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Command.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def run(self):
        """ 'Run' is the original name of this method."""

        self.wrapped.Run()

    @property
    def cast_to(self) -> 'Command._Cast_Command':
        return self._Cast_Command(self)
