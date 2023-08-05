"""_1307.py

WindingType
"""
from enum import Enum

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WINDING_TYPE = python_net_import('SMT.MastaAPI.ElectricMachines', 'WindingType')


__docformat__ = 'restructuredtext en'
__all__ = ('WindingType',)


class WindingType(Enum):
    """WindingType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _WINDING_TYPE

    ROUND_CONDUCTORS = 0
    HAIRPIN = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


WindingType.__setattr__ = __enum_setattr
WindingType.__delattr__ = __enum_delattr
