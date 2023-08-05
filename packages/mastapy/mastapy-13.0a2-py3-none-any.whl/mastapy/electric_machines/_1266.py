"""_1266.py

IndividualConductorSpecificationSource
"""
from enum import Enum

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDIVIDUAL_CONDUCTOR_SPECIFICATION_SOURCE = python_net_import('SMT.MastaAPI.ElectricMachines', 'IndividualConductorSpecificationSource')


__docformat__ = 'restructuredtext en'
__all__ = ('IndividualConductorSpecificationSource',)


class IndividualConductorSpecificationSource(Enum):
    """IndividualConductorSpecificationSource

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _INDIVIDUAL_CONDUCTOR_SPECIFICATION_SOURCE

    FROM_WINDING_SPECIFICATION = 0
    FROM_CAD_GEOMETRY = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


IndividualConductorSpecificationSource.__setattr__ = __enum_setattr
IndividualConductorSpecificationSource.__delattr__ = __enum_delattr
