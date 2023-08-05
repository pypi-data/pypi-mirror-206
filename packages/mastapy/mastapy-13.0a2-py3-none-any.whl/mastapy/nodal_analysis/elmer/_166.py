"""_166.py

ContactType
"""
from enum import Enum

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONTACT_TYPE = python_net_import('SMT.MastaAPI.NodalAnalysis.Elmer', 'ContactType')


__docformat__ = 'restructuredtext en'
__all__ = ('ContactType',)


class ContactType(Enum):
    """ContactType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _CONTACT_TYPE

    NONE = 0
    TIED = 1
    FRICTION = 2


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ContactType.__setattr__ = __enum_setattr
ContactType.__delattr__ = __enum_delattr
