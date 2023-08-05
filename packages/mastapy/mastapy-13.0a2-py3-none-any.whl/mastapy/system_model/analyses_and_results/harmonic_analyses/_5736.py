"""_5736.py

HarmonicAnalysisTorqueInputType
"""
from enum import Enum

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_TORQUE_INPUT_TYPE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'HarmonicAnalysisTorqueInputType')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisTorqueInputType',)


class HarmonicAnalysisTorqueInputType(Enum):
    """HarmonicAnalysisTorqueInputType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _HARMONIC_ANALYSIS_TORQUE_INPUT_TYPE

    LOAD_CASE = 0
    SPECIFIED_TORQUE_SPEED_CURVE = 1
    TORQUE_SPEED_CURVE_FROM_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA = 2


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


HarmonicAnalysisTorqueInputType.__setattr__ = __enum_setattr
HarmonicAnalysisTorqueInputType.__delattr__ = __enum_delattr
