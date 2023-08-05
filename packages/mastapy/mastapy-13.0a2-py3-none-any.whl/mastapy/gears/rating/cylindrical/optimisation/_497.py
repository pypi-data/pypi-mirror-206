"""_497.py

OptimisationResultsPair
"""
from typing import TypeVar, Generic

from mastapy.gears.rating.cylindrical.optimisation import _498, _499
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMISATION_RESULTS_PAIR = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation', 'OptimisationResultsPair')


__docformat__ = 'restructuredtext en'
__all__ = ('OptimisationResultsPair',)


T = TypeVar('T', bound='_499.SafetyFactorOptimisationStepResult')


class OptimisationResultsPair(_0.APIBase, Generic[T]):
    """OptimisationResultsPair

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _OPTIMISATION_RESULTS_PAIR

    class _Cast_OptimisationResultsPair:
        """Special nested class for casting OptimisationResultsPair to subclasses."""

        def __init__(self, parent: 'OptimisationResultsPair'):
            self._parent = parent

        @property
        def optimisation_results_pair(self) -> 'OptimisationResultsPair':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OptimisationResultsPair.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def results(self) -> '_498.SafetyFactorOptimisationResults[T]':
        """SafetyFactorOptimisationResults[T]: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp) if temp is not None else None

    @property
    def results_without_warnings(self) -> '_498.SafetyFactorOptimisationResults[T]':
        """SafetyFactorOptimisationResults[T]: 'ResultsWithoutWarnings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsWithoutWarnings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp) if temp is not None else None

    @property
    def cast_to(self) -> 'OptimisationResultsPair._Cast_OptimisationResultsPair':
        return self._Cast_OptimisationResultsPair(self)
