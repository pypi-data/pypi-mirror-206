"""_1535.py

ParetoOptimisationFilter
"""
from mastapy.math_utility import _1477
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_FILTER = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'ParetoOptimisationFilter')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoOptimisationFilter',)


class ParetoOptimisationFilter(_0.APIBase):
    """ParetoOptimisationFilter

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_FILTER

    class _Cast_ParetoOptimisationFilter:
        """Special nested class for casting ParetoOptimisationFilter to subclasses."""

        def __init__(self, parent: 'ParetoOptimisationFilter'):
            self._parent = parent

        @property
        def pareto_optimisation_filter(self) -> 'ParetoOptimisationFilter':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoOptimisationFilter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def filter_range(self) -> '_1477.Range':
        """Range: 'FilterRange' is the original name of this property."""

        temp = self.wrapped.FilterRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @filter_range.setter
    def filter_range(self, value: '_1477.Range'):
        value = value.wrapped if value else None
        self.wrapped.FilterRange = value

    @property
    def property_(self) -> 'str':
        """str: 'Property' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Property

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'ParetoOptimisationFilter._Cast_ParetoOptimisationFilter':
        return self._Cast_ParetoOptimisationFilter(self)
