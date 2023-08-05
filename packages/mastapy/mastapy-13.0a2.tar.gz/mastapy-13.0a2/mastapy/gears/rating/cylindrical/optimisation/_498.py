"""_498.py

SafetyFactorOptimisationResults
"""
from typing import List, TypeVar, Generic

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy.gears.rating.cylindrical.optimisation import _499
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_OPTIMISATION_RESULTS = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation', 'SafetyFactorOptimisationResults')


__docformat__ = 'restructuredtext en'
__all__ = ('SafetyFactorOptimisationResults',)


T = TypeVar('T', bound='_499.SafetyFactorOptimisationStepResult')


class SafetyFactorOptimisationResults(_0.APIBase, Generic[T]):
    """SafetyFactorOptimisationResults

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _SAFETY_FACTOR_OPTIMISATION_RESULTS

    class _Cast_SafetyFactorOptimisationResults:
        """Special nested class for casting SafetyFactorOptimisationResults to subclasses."""

        def __init__(self, parent: 'SafetyFactorOptimisationResults'):
            self._parent = parent

        @property
        def safety_factor_optimisation_results(self) -> 'SafetyFactorOptimisationResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SafetyFactorOptimisationResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def values(self) -> 'List[T]':
        """List[T]: 'Values' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Values

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SafetyFactorOptimisationResults._Cast_SafetyFactorOptimisationResults':
        return self._Cast_SafetyFactorOptimisationResults(self)
