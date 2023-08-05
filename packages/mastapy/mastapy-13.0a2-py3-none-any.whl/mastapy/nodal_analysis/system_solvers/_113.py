"""_113.py

SingularVectorAnalysis
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis.system_solvers import _111
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGULAR_VECTOR_ANALYSIS = python_net_import('SMT.MastaAPI.NodalAnalysis.SystemSolvers', 'SingularVectorAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SingularVectorAnalysis',)


class SingularVectorAnalysis(_0.APIBase):
    """SingularVectorAnalysis

    This is a mastapy class.
    """

    TYPE = _SINGULAR_VECTOR_ANALYSIS

    class _Cast_SingularVectorAnalysis:
        """Special nested class for casting SingularVectorAnalysis to subclasses."""

        def __init__(self, parent: 'SingularVectorAnalysis'):
            self._parent = parent

        @property
        def singular_vector_analysis(self) -> 'SingularVectorAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SingularVectorAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def singular_value(self) -> 'float':
        """float: 'SingularValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SingularValue

        if temp is None:
            return 0.0

        return temp

    @property
    def largest_singular_vector_components(self) -> 'List[_111.SingularDegreeOfFreedomAnalysis]':
        """List[SingularDegreeOfFreedomAnalysis]: 'LargestSingularVectorComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LargestSingularVectorComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SingularVectorAnalysis._Cast_SingularVectorAnalysis':
        return self._Cast_SingularVectorAnalysis(self)
