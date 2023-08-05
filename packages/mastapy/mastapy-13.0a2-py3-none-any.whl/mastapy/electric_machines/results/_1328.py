"""_1328.py

IHaveDynamicForceResults
"""
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_I_HAVE_DYNAMIC_FORCE_RESULTS = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'IHaveDynamicForceResults')


__docformat__ = 'restructuredtext en'
__all__ = ('IHaveDynamicForceResults',)


class IHaveDynamicForceResults:
    """This class is a public interface.
    The class body has intentionally been left empty.
    """
