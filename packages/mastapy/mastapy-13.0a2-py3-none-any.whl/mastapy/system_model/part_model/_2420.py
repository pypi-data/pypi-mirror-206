"""_2420.py

BearingF0InputMethod
"""
from enum import Enum

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_F0_INPUT_METHOD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'BearingF0InputMethod')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingF0InputMethod',)


class BearingF0InputMethod(Enum):
    """BearingF0InputMethod

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _BEARING_F0_INPUT_METHOD

    F0_DIRECTLY = 0
    FORCE_AND_DISPLACEMENT = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


BearingF0InputMethod.__setattr__ = __enum_setattr
BearingF0InputMethod.__delattr__ = __enum_delattr
